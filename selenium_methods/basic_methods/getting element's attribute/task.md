<h2>Метод get_attribute</h2>

<p>Мы уже знаем, как найти нужный элемент на странице и как получить видимый пользователю текст. Для более детальных проверок в тесте нам может понадобиться узнать значение атрибута элемента. Атрибуты могут быть стандартными свойствами, которые понимает и использует браузер для отображения и вёрстки элементов или для хранения служебной информации, например, name, width, height, color и многие <a href="https://www.w3schools.com/tags/ref_attributes.asp" rel="nofollow noopener noreferrer">другие</a>. Также атрибуты могут быть созданы разработчиками проекта для задания собственных стилей или правил.</p>

<p>Значение атрибута представляет собой&nbsp;строку. Если значение атрибута отсутствует, то это равносильно значению атрибута равному &quot;false&quot;.&nbsp;Давайте еще раз взглянем на страницу <a href="http://suninjuly.github.io/math.html" rel="nofollow noopener noreferrer">http://suninjuly.github.io/math.html</a>. На ней есть radiobuttons, для которых выбрано значение по умолчанию. В автотесте нам может понадобиться&nbsp;проверить, что для одного из&nbsp;radiobutton&nbsp;по умолчанию уже выбрано значение. Для этого мы можем проверить значение атрибута checked у&nbsp;этого элемента. Вот&nbsp;HTML-код элемента:</p>

<pre>
<code class="language-python">&lt;input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked&gt;</code></pre>

<p>Найдём этот элемент с помощью WebDriver:</p>

<pre>
<code class="language-python">people_radio = browser.find_element(By.ID, "peopleRule")</code></pre>

<p>Найдём атрибут &quot;checked&quot; с помощью встроенного метода get_attribute и проверим его значение:</p>

<pre>
<code class="language-python">people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"</code></pre>

<p>Т.к. у данного&nbsp;атрибута значение не указано явно, то метод get_attribute вернёт &quot;true&quot;. Возможно, вы заметили, что &quot;true&quot; написано с маленькой буквы, &mdash; все методы WebDriver&nbsp;взаимодействуют с браузером с помощью JavaScript, в котором булевые&nbsp;значения пишутся с маленькой буквы, а не с большой,&nbsp;как в Python.</p>

<p>Мы можем написать проверку другим способом, сравнив строки:</p>

<pre>
<code class="language-python">assert people_checked == "true", "People radio is not selected by default"
</code></pre>

<p>Если атрибута нет, то метод get_attribute вернёт значение <strong>None</strong>. Применим&nbsp;метод get_attribute&nbsp;ко второму radiobutton, и убедимся, что атрибут отсутствует.</p>

<pre>
<code class="language-python">robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None</code></pre>

<p>Так же мы можем проверять наличие атрибута disabled, который определяет, может ли пользователь взаимодействовать с элементом. Например, в&nbsp;предыдущем задании на странице с капчей для роботов JavaScript&nbsp;устанавливает&nbsp;атрибут disabled у&nbsp;кнопки <strong>Submit</strong>, когда истекает время, отведенное на решение задачи.</p>

<pre>
<code class="language-html">&lt;button type="submit" class="btn btn-default" disabled&gt;Submit&lt;/button&gt;</code></pre>
