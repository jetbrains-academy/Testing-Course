<h2>Test marking: part 2</h2>

<h3><strong>Inversion</strong></h3>

<p>To launch all the tests that do not have a given mark, you can use inversion. To run all the tests that are not marked as smoke ones, execute the following command:</p>

<pre><code class="language-bash">pytest -s -v -m "not smoke" test_fixture8.py</code></pre>

<h3><strong>Combining tests with different marks</strong></h3>

<p>To run tests with different marks, you can use the logical OR operator. Let's launch smoke and regression tests:</p>

<pre><code class="language-bash">pytest -s -v -m "smoke or regression" test_fixture8.py</code></pre>

<h3><strong>Choosing tests with several marks</strong></h3>

<p>Let's say we have smoke tests that need to be run only for a specific operating system, for example, Windows 10. We'll register the mark win10 in the file pytest.ini and add that mark to one of the tests.</p>

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

<p>To launch only the smoke tests for Windows 10, we need to use the logical AND operator:</p>

<pre><code class="language-bash">pytest -s -v -m "smoke and win10" test_fixture81.py</code></pre>

<p>The test_guest_should_see_basket_link_on_the_main_page test will be launched. </p>