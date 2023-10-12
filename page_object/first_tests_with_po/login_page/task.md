<h2>Реализация LoginPage</h2>

<p>Если вы хорошо ориентируетесь в тест-дизайне,
вы заметили что в тесте с переходом к логину нет никаких проверок.&nbsp;Давайте&nbsp;проверим,&nbsp;что мы действительно перешли на страницу логина. Для этого нам&nbsp;будет нужен&nbsp;новый Page Object. Заодно разберемся, как между ними переключаться в ходе теста.&nbsp;</p>

<p> Откройте файл LoginPage в папке pages.  Внутри есть методы проверок:&nbsp;</p>

<pre>
<code>should_be_login_url
should_be_login_form
should_be_register_form</code></pre>

<p>Реализуйте их самостоятельно:&nbsp;</p>

<p>1. В файле locators.py создайте класс&nbsp;LoginPageLocators&nbsp;</p>

<p>2. Подберите селекторы к формам регистрации и логина, добавьте их в класс&nbsp;LoginPageLocators</p>

<p>3. Напишите проверки, используя эти селекторы. Не забудьте через запятую указать адекватное сообщение об ошибке. Напишите сначала красный тест, чтобы убедиться в понятности вывода.&nbsp;</p>

<p>4. В методе should_be_login_url реализуйте проверку, что подстрока &quot;login&quot; есть в текущем url&nbsp;браузера. Для этого используйте соответствующее&nbsp;<a href="https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.current_url" rel="noopener noreferrer nofollow">свойство Webdriver</a>.</p>

<p>Теперь посмотрим,&nbsp;как можно осуществлять переход между страницами.&nbsp;</p>
