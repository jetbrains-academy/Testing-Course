<h2>Conftest.py and passing parameters in command line</h2>

<p>The built-in <strong>request</strong> fixture can receive data about currently running tests, which allows saving additional data in reports as well as doing many other interesting things. In this step, we want to show how you can set up test environments by passing parameters in the command line.</p>

<p>You can do that with the help of the built-in pytest_addoption function and the request fixture. First, in the conftest file, we'll add an option handler in the pytest_addoption function; then we'll write a fixture that will process the data passed in the option. You can find details here: <a href="https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption" rel="nofollow noopener noreferrer" target="_blank">https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption</a>.</p>

<p>Let's add the logic of command line handling to conftest.py. To request a parameter value, we can call the command:</p>

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

<p>If you launch your tests without a parameter now, you'll get an error:</p>

<pre><code>pytest -s -v test_parser.py</code></pre>

<pre><code class="language-no-highlight">_pytest.config.UsageError: --browser_name should be chrome or firefox</code></pre>

<p>The parameter value may be set by default so that you don't need to indicate the <em>--browser_name</em> parameter in the command line. You can do it, for example, this way:</p>

<pre><code class="language-python">parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")</code></pre>

<p>Let's define the parameter:</p>

<pre><code class="language-python">pytest -s -v --browser_name=chrome test_parser.py</code></pre>

<p>Now, let's launch the tests in Firefox:</p>

<pre><code class="language-python">pytest -s -v --browser_name=firefox test_parser.py</code></pre>

<p>You should see the tests starting first in Chrome and then in Firefox.</p>
