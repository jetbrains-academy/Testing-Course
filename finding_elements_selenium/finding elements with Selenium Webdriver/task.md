<h2>Поиск элементов с помощью&nbsp;Selenium</h2>

<p>Для поиска элементов на странице в Selenium WebDriver используются несколько стратегий, позволяющих&nbsp;искать по&nbsp;атрибутам элементов, текстам в ссылках,&nbsp;CSS-селекторам и&nbsp;XPath-селекторам. Для поиска Selenium предоставляет метод find_element, который принимает два аргумента - тип локатора и значение локатора. Существуют следующие методы&nbsp;поиска элементов:</p>

<ul>
	<li><strong>find_element(By.ID, value)</strong>&nbsp;&mdash; поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло,&nbsp;и вы чаще всего будет использовать этот метод, так как&nbsp;он наиболее стабильный;</li>
	<li><strong>find_element(By.CSS_SELECTOR, value)</strong>&nbsp;&mdash; поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;</li>
	<li><strong>find_element(By.XPATH, value)</strong>&nbsp;&mdash; поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;</li>
	<li><strong>find_element(By.NAME, value)</strong>&nbsp;&mdash; поиск по атрибуту name элемента;</li>
	<li><strong>find_element(By.TAG_NAME, value)</strong>&nbsp;&mdash; поиск элемента по названию тега элемента;</li>
	<li><strong>find_element(By.CLASS_NAME, value)</strong>&nbsp;&mdash; поиск по значению атрибута class;</li>
	<li><strong>find_element(By.LINK_TEXT, value)&nbsp;</strong>&mdash; поиск ссылки на странице по полному совпадению;</li>
	<li><strong>find_element(By.PARTIAL_LINK_TEXT, value)&nbsp;</strong>&mdash; поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.</li>
</ul>

<p>Например, мы хотим найти кнопку со значением id=&quot;submit_button&quot;:</p>

<pre>
<code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit")</code></pre>

<p>Обратите внимание, что мы импортировали класс By, который содержит все возможные локаторы.</p>

<p>Если страница у вас загрузилась, но дальше ничего не происходит, вернитесь обратно в консоль, в которой вы запускали ваш скрипт. Скорее всего,&nbsp;вы увидите там ошибку <strong>NoSuchElementException</strong>. Она будет выглядеть следующим образом:</p>

<pre>
<code class="language-no-highlight">selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"submit"}</code></pre>

<p>Ошибка очевидна: мы неправильно указали локатор&nbsp;&mdash; значит, кнопки с таким id на странице нет.</p>

<p>Исправим локатор, чтобы наш код проходил без ошибок:</p>

<pre>
<code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")</code></pre>

<h3>Поиск нескольких элементов</h3>

<p>Вы можете столкнуться с ситуацией, когда на странице будет несколько элементов, подходящих под заданные вами параметры поиска. В этом случае WebDriver&nbsp;вернет вам только первый элемент, который встретит во время поиска по HTML. Если вам нужен не первый, а второй или следующие&nbsp;элементы, вам нужно либо задать более точный селектор для поиска, либо&nbsp;использовать методы <strong>find_element<span style="color:#ff4363"><u>s</u></span></strong>,&nbsp;которые мы рассмотрим чуть позже.</p>

<p>Иногда в статьях про Selenium WebDriver вы также будете встречать термин &quot;локаторы&quot;, под которым&nbsp;подразумеваются стратегии поиска и значения, по которым должен выполняться поиск. Например, можно искать по локатору By.ID со значением &quot;send_button&quot;.</p>
