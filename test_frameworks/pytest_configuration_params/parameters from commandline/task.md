<h2>Conftest.py и передача параметров в командной строке</h2>

<p>Встроенная фикстура <strong>request</strong> может получать данные о текущем запущенном тесте, что позволяет, например, сохранять дополнительные данные в отчёт, а также делать многие другие интересные вещи. В этом шаге мы хотим показать, как можно настраивать тестовые окружения с помощью передачи параметров через командную строку.</p>

<p>Это делается с помощью встроенной функции pytest_addoption и фикстуры request. Сначала добавляем в файле conftest обработчик опции в функции pytest_addoption, затем напишем фикстуру, которая будет обрабатывать переданные в опции данные. Подробнее можно ознакомиться здесь: <a href="https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption" rel="nofollow noopener noreferrer" target="_blank">https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption</a></p>

<p>Добавим логику обработки командной строки в conftest.py. Для запроса значения параметра мы можем вызвать команду:</p>

<pre><code>browser_name = request.config.getoption("browser_name")</code></pre>

<p><strong>conftest.py:</strong></p>

<pre><code class="language-python">import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

</code></pre>

<p><strong>test_parser.py:</strong></p>

<pre><code class="language-python">link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")</code></pre>

<p>Если вы теперь запустите тесты без параметра, то получите ошибку:</p>

<pre><code>pytest -s -v test_parser.py</code></pre>

<pre><code class="language-no-highlight">_pytest.config.UsageError: --browser_name should be chrome or firefox</code></pre>

<p>Можно задать значение параметра по умолчанию, чтобы в командной строке не обязательно было указывать параметр <em>--browser_name</em>, например, так:</p>

<pre><code class="language-python">parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")</code></pre>

<p>Давайте укажем параметр:</p>

<pre><code class="language-python">pytest -s -v --browser_name=chrome test_parser.py</code></pre>

<p>А теперь запустим тесты на Firefox:</p>

<pre><code class="language-python">pytest -s -v --browser_name=firefox test_parser.py</code></pre>

<p>Вы должны увидеть, как сначала тесты запустятся в браузере Chrome, а затем — в Firefox.</p>