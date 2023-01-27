<h2>Пример задачи для execute_script</h2>

<p>Давайте теперь рассмотрим реальную ситуацию, когда пользователь должен кликнуть на элемент, который внезапно оказывается перекрыт другим элементом на странице.</p>

<p>Для клика в WebDriver мы используем метод click(). Если элемент оказывается перекрыт другим элементом, то наша программа вызовет следующую ошибку:</p>

<pre><code>selenium.common.exceptions.WebDriverException: Message: unknown error: Element &lt;button type="submit" class="btn btn-default" style="margin-bottom: 1000px;"&gt;...&lt;/button&gt; is not clickable at point (87, 420). Other element would receive the click: &lt;p&gt;...&lt;/p&gt;
</code></pre>

<p>Из описания ошибки можно понять, что указанный нами элемент нельзя кликнуть в данной точке, т.к. клик произойдёт на другом элементе с тегом &lt;p&gt;.</p>

<p>Чтобы увидеть пример данной ошибки, запустите следующий скрипт:</p>

<pre><code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()</code></pre>

<p>Теперь вы можете сами посмотреть на эту <a href="https://SunInJuly.github.io/execute_script.html" rel="nofollow noopener noreferrer">страницу</a> и увидеть, что огромный футер действительно перекрывает нужную нам кнопку. Футером (footer) называется нижний блок, который обычно одинаков для всех страниц сайта. Чтобы понять, как решить эту проблему, нужно разобраться, как работает метод <strong>click()</strong>.</p>

<p>В первую очередь WebDriver проверит, что ширина и высота элемента больше 0, чтобы по нему можно было кликнуть.</p>

<p>Затем, если элемент находится за границей окна браузера, WebDriver автоматически проскроллит страницу, чтобы элемент попал в область видимости, то есть не находился за границей экрана. Но это не гарантирует того, что элемент не перекрыт другим элементом, который тоже находится в области видимости.</p>

<p>А в какую точку элемента будет происходить клик? Selenium рассчитывает координаты центра элемента и производит клик в вычисленную точку. Это тоже приведёт к ошибке, если часть элемента всё-таки видна, но элемент перекрыт больше чем на половину своей высоты или ширины.</p>

<p>Если мы столкнулись с такой ситуацией, мы можем заставить браузер дополнительно проскроллить нужный элемент, чтобы он точно стал видимым.<br>
Делается это с помощью следующего скрипта:</p>

<pre><code>"return arguments[0].scrollIntoView(true);"</code></pre>

<p>Мы дополнительно передали в метод scrollIntoView аргумент <code>true</code>, чтобы элемент после скролла оказался в области видимости. Другие возможные параметры метода можно посмотреть здесь: <a href="https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView" rel="noopener noreferrer nofollow">https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView</a></p>

<p>В итоге, чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды в коде:</p>

<pre><code class="language-python">button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()</code></pre>

<p>В метод execute_script мы передали текст js-скрипта и найденный элемент button, к которому нужно будет проскроллить страницу. После выполнения кода элемент button должен оказаться в верхней части страницы. Подробнее о методе см <a href="https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView" rel="noopener noreferrer nofollow">https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView</a> .</p>

<p>Также можно проскроллить всю страницу целиком на строго заданное количество пикселей. Эта команда проскроллит страницу на 100 пикселей вниз:</p>

<pre><code class="language-python">browser.execute_script("window.scrollBy(0, 100);")</code></pre>

<p><span style="color: #ff4363;">!Важно.</span> Мы не будем в этом курсе изучать, как работает JavaScript, и обойдемся только приведенным выше примером скрипта с прокруткой страницы. Для сравнения приведем скрипт на этом языке, который делает то же, что приведенный выше пример для WebDriver:</p>

<pre><code class="language-javascript">// javascript
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);</code></pre>

<p>Можете попробовать исполнить его в консоли браузера на странице <a href="http://suninjuly.github.io/execute_script.html" rel="noopener noreferrer nofollow">http://suninjuly.github.io/execute_script.html</a>. Для этого откройте инструменты разработчика в браузере, перейдите на вкладку <strong>консоль (console)</strong>, скопируйте туда этот код и нажмите Enter. Таким образом можно протестировать кусочки js кода прежде чем внедрять его в свои тесты на python. </p>

<p>Обратите внимание, что в коде в WebDriver нужно использовать ключевое слово <strong>return</strong>. Также его нужно будет использовать, когда вы захотите получить какие-то данные после выполнения скрипта. При этом при тестировании скрипта в консоли браузера слово <strong>return</strong> использовать не надо.</p>
