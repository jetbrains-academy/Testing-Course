<h2>XFail: помечать тест как ожидаемо падающий</h2>

<p><strong>Отметить тест как падающий</strong></p>

<p>Теперь добавим в наш тестовый класс тест, который проверяет наличие кнопки "Избранное":</p>

<pre><code class="language-python">def test_guest_should_see_search_button_on_the_main_page(self, browser): 
     browser.get(link)
     browser.find_element(By.CSS_SELECTOR, "button.favorite")</code></pre>

<p>Предположим, что такая кнопка должна быть, но из-за изменений в коде она пропала. Пока разработчики исправляют баг, мы хотим, чтобы результат прогона ﻿всех ﻿наших тестов был успешен, но падающий тест помечался соответствующим образом, чтобы про него не забыть. Добавим маркировку <strong>@pytest.mark.xfail </strong>для падающего теста.</p>

<p><strong>test_fixture10.py:</strong></p>

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


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

</code></pre>

<p>Запустим наши тесты:</p>

<pre><code class="language-no-highlight">pytest -v test_fixture10.py</code></pre>

<p>Наш упавший тест теперь отмечен как <strong>xfail</strong>, но результат прогона тестов помечен как успешный:</p>

<p><img alt="" src="https://ucarecdn.com/929c02c8-d2ab-4ecd-a8db-e94d93caecaa/"></p>

<p>Когда баг починят, мы это узнаем, ﻿﻿так как теперь тест будет отмечен как <strong>XPASS </strong>(“unexpectedly passing” — неожиданно проходит). После этого маркировку <strong>xfail </strong>для теста можно удалить. Кстати, к маркировке <strong>xfail</strong> можно добавлять параметр <strong>reason</strong>. Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest <strong>-rx</strong>.</p>

<p><strong>test_fixture10a.py:</strong></p>

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


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

</code></pre>

<p>Запустим наши тесты:</p>

<pre><code class="language-no-highlight">pytest -rx -v test_fixture10a.py</code></pre>

<p> </p>

<p>Сравните вывод в первом и во втором случае.</p>

<p><img alt="" src="https://ucarecdn.com/0bf951ab-4bad-4d1f-9856-6e0090714627/"></p>

<p><strong>XPASS-тесты</strong></p>

<p>Поменяем селектор в последнем тесте, чтобы тест начал проходить.</p>

<p><strong>test_fixture10b.py:</strong></p>

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


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "input.btn.btn-default")

</code></pre>

<p>Запустите тесты. Здесь мы добавили символ X в параметр -r, чтобы получить подробную информацию по XPASS-тестам:</p>

<pre><code class="language-bash">pytest -rX -v test_fixture10b.py</code></pre>

<p>И изучите отчёт: </p>

<p><img alt="" src="https://ucarecdn.com/727f6e0f-ef30-4f61-b3ab-65d8d2f7e8d3/"></p>

<p>Дополнительно об использовании этих меток можно почитать в документации: <a href="https://pytest.org/en/stable/skipping.html" rel="noopener noreferrer nofollow">Skip and xfail: dealing with tests that cannot succeed</a>.  Там есть много разных интересных особенностей, например, как пропускать тест только при выполнении условия, как сделать так, чтобы внезапно прошедший xfailed тест в отчете стал красным, и так далее. </p>