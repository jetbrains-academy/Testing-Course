<h2>Scope</h2>

<p>For fixtures, we can define scope. The possible values are: “<strong>function</strong>”, “<strong>class</strong>”, “<strong>module</strong>”, and “<strong>session</strong>”. Consequently, the fixture will be executed once for a test method, once for a class, once for a module, or once for all the tests run in the current session. </p>

<p>Let's run all our tests from the <strong>TestMainPage1</strong> class in one browser to save time. In the browser fixture, we'll set scope="class":</p>

<p>test_fixture5.py</p>

<pre><code class="language-python">import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # calling the fixture in the test by passing it as a parameter
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")
        print("finish test2")
</code></pre>

<p>We see that in the above example, the browser opened once, and the tests ran one-at-a-time in that browser. We've done that for the sake of an example, but we strongly recommend launching a separate browser copy for each test to improve test stability. Fixtures that require a long launching time and lots of resources (usually, it's about working with databases), may be also called just once within a test run session.</p>