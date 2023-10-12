<h2>Переходы между страницами</h2>

<p>Переход можно реализовать двумя разными способами. </p>

<p>Первый способ: возвращать нужный Page Object.</p>

<p>Для этого в файле main_page.py нужно сделать импорт страницы с логином: </p>

<pre><code class="language-python">from .login_page import LoginPage</code></pre>

<p>Затем в методе, который осуществляет переход к странице логина, проинициализировать новый объект Page и вернуть его: </p>

<pre><code class="language-python">def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    return LoginPage(browser=self.browser, url=self.browser.current_url) </code></pre>

<p>Обратите внимание! При создании объекта мы обязательно передаем ему тот же самый объект драйвера для работы с браузером, а в качестве url передаем текущий адрес.</p>

<p>Теперь в тесте нам не нужно думать про инициализацию страницы: она уже создана. Сохранив возвращаемое значение в переменную, мы можем использовать методы новой страницы в тесте:</p>

<pre><code>def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()</code></pre>

<p>Плюсы такого подхода: </p>

<ul>
	<li>тест выглядит аккуратнее — не нужно инициализировать страницу в теле теста;</li>
	<li>явно возвращаем страницу — тип страницы ассоциирован с методом;</li>
	<li>не нужно каждый раз думать в разных тестах про инициализацию страницы — уменьшаем дублирование кода;</li>
</ul>

<p>минусы: </p>

<ul>
	<li>если у нас копится большое количество страниц и переходов — образуется много перекрестных импортов;</li>
	<li>большая связность кода — при изменении логики придется менять возвращаемое значение;</li>
	<li>сложнее понимать код, так как страница инициализируется неявно;</li>
	<li>образуются циклические зависимости, что часто приводит к ошибкам.</li>
</ul>

<p>Второй подход: переход происходит неявно, страницу инициализируем в теле теста: </p>

<p>1. Закомментируйте строку с возвращаемым значением </p>

<pre><code class="language-python">def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    # return LoginPage(browser=self.browser, url=self.browser.current_url) </code></pre>

<p>2. Инициализируем LoginPage в теле теста (не забудьте импортировать в файл нужный класс): </p>

<pre><code>from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()</code></pre>

<p>Плюсы:</p>

<ul>
	<li>меньше связность кода;</li>
	<li>меньше импортов, нет перекрестных импортов;</li>
	<li>больше гибкость;</li>
	<li>в тесте понятнее что происходит, т.к. явно инициализируем страницу.</li>
</ul>

<p>Минусы:</p>

<ul>
	<li>появляется лишний шаг в тест-кейсе;</li>
	<li>каждый раз при написании теста нужно думать про корректные переходы;</li>
	<li>дублируется код.</li>
</ul>

<p>И тот и другой подход можно успешно применять в своих проектах, главное делать это с умом. Сейчас оставьте второй вариант с явной инициализацией страниц в теле теста, чтобы избежать лишних сложностей с циклическими зависимостями. </p>