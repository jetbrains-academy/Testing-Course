<h2>Маркировка тестов часть 1</h2>

<p>Когда тестов становится много, хорошо иметь способ разделять тесты не только по названиям, но также по каким-нибудь заданным нами категориям. Например, мы можем выбрать небольшое количество критичных тестов (smoke), которые нужно запускать на каждый коммит разработчиков, а остальные тесты обозначить как регрессионные (regression) и запускать их только перед релизом. Или у нас могут быть тесты, специфичные для конкретного браузера (internet explorer 11), и мы хотим запускать эти тесты только под данный браузер. Для выборочного запуска таких тестов в PyTest используется маркировка тестов или <strong>метки (marks)</strong>. Для маркировки теста нужно написать декоратор вида <strong>@pytest.mark.mark_name</strong>, где mark_name — произвольная строка.</p>

<p>Давайте разделим тесты в одном из предыдущих примеров на smoke и regression.</p>

<p><strong>test_fixture8.py:</strong></p>

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

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")

</code></pre>

<p>Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр <strong>-m</strong> и нужную метку:</p>

<pre><code class="language-python">pytest -s -v -m smoke test_fixture8.py</code></pre>

<p>Если всё сделано правильно, то должен запуститься только тест с маркировкой smoke.</p>

<p>При этом вы увидите warning, то есть предупреждение:</p>

<pre><code class="language-bash">PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,</code></pre>

<p>Это предупреждение появилось потому, что в последних версиях PyTest настоятельно рекомендуется регистрировать метки явно перед использованием. Это, например, позволяет избегать опечаток, когда вы можете ошибочно пометить ваш тест несуществующей меткой, и он будет пропускаться при прогоне тестов.</p>

<h3>Как же регистрировать метки?</h3>

<p>Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл следующие строки:</p>

<pre><code class="language-no-highlight">[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests</code></pre>

<p>Текст после знака ":" является поясняющим — его можно не писать.</p>

<p>Снова запустите тесты:</p>

<pre><code class="language-python">pytest -s -v -m smoke test_fixture8.py</code></pre>

<p>Теперь предупреждений быть не должно.</p>

<p> </p>

<p>Так же можно маркировать целый тестовый класс. В этом случае маркировка будет применена ко всем тестовым методам, входящим в класс.</p>