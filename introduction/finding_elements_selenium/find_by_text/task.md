<h2>Задание: поиск элемента по тексту в ссылке</h2>

<p>В этой задаче мы попробуем искать элементы по тексту ссылки, для этого воспользуемся методом find_element_by_link_text:</p>

<pre><code>link = browser.find_element(By.LINK_TEXT, text)</code></pre>

<p>В качестве аргумента в метод передается такой текст, ссылку с которым мы хотим найти. Это тот самый текст, который содержится между открывающим и закрывающим тегом &lt;a&gt; вот тут &lt;/a&gt;</p>

<p>Допустим, на странице <a href="https://www.degreesymbol.net/" rel="noopener noreferrer nofollow">https://www.degreesymbol.net/</a> мы хотим найти ссылку с текстом "Degree symbol in Math" и перейти по ней. Если хотим найти элемент по полному соответствию текста, то нам подойдет такой код: </p>

<pre><code>link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
link.click()</code></pre>

<ol>
</ol>

<p>А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код: </p>

<pre><code>link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
link.click()</code></pre>

<p>Обычно поиск по подстроке чуть более удобный и гибкий, но с ним надо быть вдвойне аккуратными и проверять, что находится нужный элемент. </p>

<h3>Задание</h3>

<p>На указанной ниже странице вам нужно найти зашифрованную ссылку и кликнуть по ней:</p>

<ol>
	<li>Добавьте в самый верх своего кода import math</li>
	<li>Добавьте в код команду, которая откроет страницу: <a href="http://suninjuly.github.io/find_link_text" rel="noopener noreferrer nofollow">http://suninjuly.github.io/find_link_text</a></li>
	<li>Добавьте команду, которая найдет ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой: 
	<pre><code>str(math.ceil(math.pow(math.pi, math.e)*10000))</code></pre>
	<p>(можно вставить данное выражение в свой код, а можно выполнить в интерпретаторе, скопировать оттуда результат и уже его использовать в вашем коде) </p>
	</li>
	<li>
	<p>Добавьте команду для клика по найденной ссылке: она перенесет вас на форму регистрации</p>
	</li>
	<li>
	<p>Заполните скриптом форму так же как вы делали в предыдущем шаге урока</p>
	</li>
</ol>

<p><strong>Важно! </strong>Поиск по тексту ссылки бывает очень удобным, так часто тексты меняются реже, чем атрибуты элементов. Но лучше избегать такого метода поиска. Например, если приложение имеет несколько языков интерфейса, ваши тесты будут проходить только с определенным языком интерфейса. Применяйте этот метод с осторожностью и помните про возможные ограничения. </p>

<p>Читать больше: </p>

<p><a href="https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text" rel="noopener noreferrer nofollow">https://selenium-python.readthedocs.io/locating-elements.html#locating-hyperlinks-by-link-text</a></p>
