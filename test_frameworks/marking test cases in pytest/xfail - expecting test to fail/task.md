<h2>XFail: marking tests expected to fail</h2>

<p><strong>Mark a test as failing</strong></p>

<p>Now, let's add a new test to our test class – it checks for the "Favorite" button:</p>

<pre><code class="language-python">def test_guest_should_see_search_button_on_the_main_page(self, browser): 
     browser.get(link)
     browser.find_element(By.CSS_SELECTOR, "button.favorite")</code></pre>

<p>Let's assume that such a button does exist but has disappeared because of code changes. While developers are fixing the bug, we want to make sure that all our tests pass successively but the failing test gets a special mark so that we don't forget about it. We'll add the <strong>@pytest.mark.xfail </strong>mark for the failing test.</p>

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

<p>Let's run our tests:</p>

<pre><code class="language-no-highlight">pytest -v test_fixture10.py</code></pre>

<p>Now, the failed test is marked <strong>xfail</strong>, but the result of running all tests is successful:</p>

<p><img alt="" src="https://ucarecdn.com/929c02c8-d2ab-4ecd-a8db-e94d93caecaa/"></p>

<p>When the bug gets fixed, we'll see it, as our test will be marked <strong>XPASS </strong>(“unexpectedly passing”). Then, the <strong>xfail </strong>mark for the test may be deleted. Actually, you can add the <strong>reason</strong> parameter to the <strong>xfail</strong> mark. To see the message in the console, add the pytest <strong>-rx</strong> parameter at launch time.</p>

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

<p>Let's run our tests:</p>

<pre><code class="language-no-highlight">pytest -rx -v test_fixture10a.py</code></pre>

<p> </p>

<p>Compare the test results for both cases.</p>

<p><img alt="" src="https://ucarecdn.com/0bf951ab-4bad-4d1f-9856-6e0090714627/"></p>

<p><strong>XPASS tests</strong></p>

<p>Let's change the selector in the latter test so that the test would pass.</p>

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

<p>Run the tests. We've added the X symbol to the -r parameter to get detailed information on XPASS tests:</p>

<pre><code class="language-bash">pytest -rX -v test_fixture10b.py</code></pre>

<p>See the report: </p>

<p><img alt="" src="https://ucarecdn.com/727f6e0f-ef30-4f61-b3ab-65d8d2f7e8d3/"></p>

<p>You can find additional information on using these marks in the documentation: <a href="https://pytest.org/en/stable/skipping.html" rel="noopener noreferrer nofollow">Skip and xfail: dealing with tests that cannot succeed</a>.  There you can find many interesting features: for example, how to skip a test only when a certain condition is met, how to make an unexpectedly passed xfailed test appear red in the report, etc. </p>