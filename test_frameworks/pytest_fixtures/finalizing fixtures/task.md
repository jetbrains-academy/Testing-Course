<h2>Finalizers — closing the browser</h2>

<p>You may have noticed that in our example we didn't use the <strong>browser.quit()</strong> command. As a result, several browser windows remained open after the test was over and closed only after the completion of all tests. The browsers were closed thanks to a built-in fixture – garbage collector. However, if we had several dozens of tests, the open browser windows could have eaten all RAM. That's why it's important to explicitly close browsers after each test. To do that, we can use <strong>finalizers</strong>. One of possible finalizers is the use of Python's key word <strong>yield</strong>. After the test that called the fixture is complete, the fixture will be executed starting with the line that follows the line with the <strong>yield</strong> word:</p>

<p>test_fixture3.py</p>

<pre><code class="language-python">import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # this code will run after the test is completed
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # calling the fixture in the test by passing it as a parameter
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")
</code></pre>

<p>There's an alternative way to call the teardown code – with the built-in <strong>request</strong> fixture and its method <strong>addfinalizer</strong>. You can study it on your own in the PyTest <a href="https://docs.pytest.org/en/latest/how-to/fixtures.html#adding-finalizers-directly" rel="nofollow noopener noreferrer">documentation</a>. </p>

<p>We also recommend leaving data and memory cleaning up to the fixture instead of writing it in test steps: the finalizer will be executed even when the test fails with an error. </p>