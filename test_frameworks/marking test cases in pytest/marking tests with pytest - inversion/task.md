<h2>Маркировка тестов часть 2</h2>

<h3><strong>Инверсия</strong></h3>

<p>Чтобы запустить все тесты, не имеющие заданную маркировку, можно использовать инверсию. Для запуска всех тестов, не отмеченных как smoke, нужно выполнить команду:</p>

<pre><code class="language-bash">pytest -s -v -m "not smoke" test_fixture8.py</code></pre>

<h3><strong>Объединение тестов с разными маркировками</strong></h3>

<p>Для запуска тестов с разными метками можно использовать логическое ИЛИ. Запустим smoke и regression-тесты:</p>

<pre><code class="language-bash">pytest -s -v -m "smoke or regression" test_fixture8.py</code></pre>

<h3><strong>Выбор тестов, имеющих несколько маркировок</strong></h3>

<p>Предположим, у нас есть smoke-тесты, которые нужно запускать только для определенной операционной системы, например, для Windows 10. Зарегистрируем метку win10 в файле pytest.ini, а также добавим к одному из тестов эту метку.</p>

<p><strong>pytest.ini:</strong></p>

<pre><code class="language-no-highlight">[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests
    win10</code></pre>

<p><strong>test_fixture81.py:</strong></p>

<pre><code class="language-python">import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")

</code></pre>

<p>Чтобы запустить только smoke-тесты для Windows 10, нужно использовать логическое И:</p>

<pre><code class="language-bash">pytest -s -v -m "smoke and win10" test_fixture81.py</code></pre>

<p>Должен выполнится тест test_guest_should_see_basket_link_on_the_main_page. </p>