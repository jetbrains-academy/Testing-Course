<h2>Fixtures returning a value</h2>

<p>We've discussed the basic approach to creating fixtures, with test data being set up and cleaned up in the setup and teardown methods. PyTest offers an advanced approach to fixtures, within which fixtures may be defined globally and passed to test methods as parameters; besides, there is a set of built-in fixtures. It's a more flexible and convenient way of working with auxiliary functions, and now you will see why. </p>

<p><strong>Returned value</strong></p>

<p>Fixtures may return a value, which may be later used in tests. Let's rewrite our previous example with PyTest fixtures. We'll create a <strong>browser</strong> fixture, which will create a WebDriver object. We will be able to use that object in tests to interact with the browser. To do that, we'll write a browser method and will indicate that it is a fixture with the help of the <strong>@pytest.fixture</strong> decorator. After that, we'll be able to call the fixture in tests by passing it as a parameter.By default, the fixture will be created for each test method,i.e., for each test there will be a separate browser copy.</p>

<pre><code class="language-python">pytest -s -v test_fixture2.py</code></pre>

<p><strong>test_fixture2.py:</strong></p>

<pre><code class="language-python">import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # calling fixture, using its name as an argument
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")
</code></pre>
