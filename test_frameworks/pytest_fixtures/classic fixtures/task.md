<h2>Classic fixtures</h2>

<p>An important aspect of working with PyTest is the concept of fixture. In the context of PyTest, fixtures are auxiliary functions that are not part of the test scenario.</p>

<p>The purposes of fixtures may be different. One of the most popular uses of fixtures is preparing the test environment and cleaning up the test environment and data after test completion. However, fixtures may be used for a wide range of purposes: connecting to a database the tests work with, creating test files, or preparing data in the current environment with the help of API methods. You can read about fixtures in the general sense in more detail in <a href="https://en.wikipedia.org/wiki/Test_fixture#Software" rel="nofollow noopener noreferrer">Wikipedia</a>.</p>

<p>A classic way of working with fixtures is creating setup and teardown methods in a file with tests (<a href="https://docs.pytest.org/en/latest/how-to/xunit_setup.html?highlight=teardown" rel="nofollow noopener noreferrer">PyTest documentation</a>).</p>

<p>We can create fixtures for modules, classes, and separate functions. Let's try to write a fixture for browser initialization, which we can later use in our tests. After test completion, we will automatically close the browser with the <strong> browser.quit()</strong> command to avoid having a number of open browser windows in our system. We'll leave browser initializing and closing to fixtures so that we don't need to write that code for each test.</p>

<p>We'll start combining our tests into test suites; classes will function as suites in which we store our tests.</p>

<p>Let's consider two examples: creating a copy of a browser and closing it once for all the tests of the first test suite, and creating a browser for each test of the second test suite. Save the below code in the file <strong> test_fixture1.py</strong> and run it with PyTest. Don't forget to indicate the parameter <strong>-s</strong> to see the text displayed by the print() command.</p>

<pre><code class="language-python">pytest -s test_fixture1.py</code></pre>

<p><strong>test_fixture1.py:</strong></p>

<pre><code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser for test suite..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")



</code></pre>

<p>In the console, we see:  </p>

<p><img alt="" src="https://ucarecdn.com/e4d862f8-8d75-4a59-9387-f967790f8d09/"></p>

<p>We see that in the first test suite, the browser was launched once, while in the second one – twice.</p>

<p>The data and the cache left from the previous test run may affect the results of subsequent tests, so it's a good idea to launch a separate browser for each test to ensure test stability. Besides, if the browser suddenly hangs in one of the tests, the rest of the tests won't be affected if they are run in a separate browser each.</p>

<p>The disadvantages of launching a browser for each test are the following: opening and closing the browser takes time, so your tests will be longer. You may want to optimize the time of the test run, but it's better to do that with other tools, which we will discuss later.</p>

<p>Usually, such fixtures migrate together with tests written with unittest, and we need to support them. However, everybody now writes more flexible fixtures with <strong>@pytest.fixture</strong>, which we will discuss in the next step. </p>
