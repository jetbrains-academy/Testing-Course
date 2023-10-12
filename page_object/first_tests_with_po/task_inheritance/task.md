<h2><strong>Плюсы наследования: пример</strong></h2>

<p>В предыдущем уроке, мы написали тест "гость может перейти на страницу логина с главной страницы магазина". Но если вы внимательно посмотрите на остальные страницы, то заметите, что ссылка на страницу логина присутствует на каждой странице. Если мы хотим добавить тест "гость может перейти на страницу логина со страницы товара", то для избежания дублирования, логично перенести соответствующие методы в класс <strong>BasePage</strong>. Давайте так и поступим: </p>

<p>В файле <em>locators.py</em> создаем новый класс <strong>BasePageLocators</strong><em> </em>и переносим туда соответствующие элементы:</p>

<pre><code>class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")</code></pre>

<p>В файл <em>base_page.py</em> переносим соответствующие методы, заменяя класс с локаторами на BasePageLocators:  </p>

<pre><code>from .locators import BasePageLocators


class BasePage():
...
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
... </code></pre>

<p><em>Примечание: методы лучше всего описывать в классе в алфавитном порядке, так проще ориентироваться и находить.</em></p>

<p>В классе <strong>MainPage</strong><em> </em>у нас не осталось никаких методов, поэтому добавим туда заглушку: </p>

<pre><code>class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)</code></pre>

<p>Как вы уже знаете, метод<strong> __init__ </strong>вызывается при создании объекта. Конструктор выше с ключевым словом <strong>super </strong>на самом деле только вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор <strong>MainPage</strong>. </p>

<p>Теперь мы можем легко добавлять тесты вида "гость может перейти на страницу логина со страницы Х". </p>

<p>Добавляем в файл c тестами <em>test_product_page.py</em> новые тесты: </p>

<pre><code>def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()</code></pre>

<p>Добавьте самостоятельно второй тест </p>

<pre><strong>test_guest_can_go_to_login_page_from_product_page</strong> 
</pre>

<p>Запустите тесты и убедитесь, что они проходят. </p>

<p>Зафиксируйте изменения коммитом. </p>