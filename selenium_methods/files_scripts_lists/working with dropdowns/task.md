<h2>Работа со списками</h2>

<p>На веб-страницах мы также встречаем&nbsp;раскрывающиеся (выпадающие) списки. У таких списков есть несколько важных&nbsp;особенностей:</p>

<ol>
	<li>У каждого элемента списка обычно есть уникальное значение атрибута&nbsp;value</li>
	<li>В списках может&nbsp;быть разрешено выбирать как только один, так и&nbsp;несколько вариантов, в зависимости от типа списка</li>
	<li>Визуально списки могут различаться тем, что в одном случае все варианты скрыты в выпадающем меню (<a href="http://suninjuly.github.io/selects1.html" rel="nofollow noopener noreferrer" target="_blank">http://suninjuly.github.io/selects1.html</a>), а в другом все варианты или их часть видны&nbsp;(<a href="http://suninjuly.github.io/selects2.html" rel="nofollow noopener noreferrer" target="_blank">http://suninjuly.github.io/selects2.html</a>)</li>
</ol>

<p>Но для взаимодействия&nbsp;с любым вариантом списка&nbsp;мы будем использовать одни и те же методы Selenium.</p>

<p>&nbsp;</p>

<p>Посмотрим, как выглядит html для списка:</p>

<pre>
<code class="language-html">
&lt;label for="dropdown"&gt;Выберите язык программирования:&lt;/label&gt;
&lt;select id="dropdown" class="custom-select"&gt;
 &lt;option selected&gt;--&lt;/option&gt;
 &lt;option value="1"&gt;Python&lt;/option&gt;
 &lt;option value="2"&gt;Java&lt;/option&gt;
 &lt;option value="3"&gt;JavaScript&lt;/option&gt;
&lt;/select&gt;</code></pre>

<p>Варианты ответа задаются тегом option, значение value может отсутствовать.&nbsp;Можно отмечать варианты с помощью обычного метода click(). Для этого сначала нужно применить метод click() для элемента с тегом select, чтобы список раскрылся, а затем кликнуть на нужный вариант ответа:</p>

<pre>
<code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get(link)


browser.find_element(By.TAG_NAME, "select").click()
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
</code></pre>

<p>Последняя строчка может выглядеть и так:</p>

<pre>
<code class="language-python">browser.find_element(By.CSS_SELECTOR, "[value='1']").click()</code></pre>

<p>Это не самый удобный способ, так как&nbsp;нам приходится делать лишний клик для открытия списка.</p>

<p>Есть более удобный способ, для которого используется специальный класс&nbsp;<strong>Select</strong> из библиотеки WebDriver. Вначале мы должны инициализировать новый объект, передав в него WebElement с тегом select. Далее можно найти любой вариант из списка с помощью метода <strong>select_by_value(value):</strong></p>

<pre>
<code>from selenium.webdriver.support.ui import Select
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
</code></pre>

<p>Можно использовать еще два метода: <strong>select.select_by_visible_text(&quot;text&quot;)</strong> и <strong>select.select_by_index(index)</strong>. Первый способ ищет элемент по видимому тексту, например,<strong> select.select_by_visible_text(&quot;Python&quot;)</strong>&nbsp;найдёт &quot;Python&quot; для нашего примера.</p>

<p>Второй способ ищет элемент по его&nbsp;индексу или порядковому номеру. Индексация начинается с нуля. Для того чтобы найти элемент с текстом &quot;Python&quot;, нужно использовать <strong>select.select_by_index(1)</strong>, так как&nbsp;опция с индексом 0 в данном примере имеет значение по умолчанию равное &quot;--&quot;.</p>
