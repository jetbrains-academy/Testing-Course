<h2>Test marking: part 1</h2>

<p>When the number of tests becomes large, it's a good idea to identify them not only by names but also by some other defined categories. For example, we can select a small number of smoke tests, which need to be run after each new commit from the developers, and define the rest as regression tests, which should be run only before the release. Or, we can have tests specific to a certain browser (e.g., Internet Explorer 11), and we want to run them only on that browser. To selectively launch such tests, PyTest uses test <strong>marks</strong>. To mark tests, you need to write a decorator like <strong>@pytest.mark.mark_name</strong>, where mark_name is an arbitrary string.</p>

<p>Let's divide the tests from one of our previous examples into smoke and regression ones.</p>

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

<p>To run a test with a given mark, we need to pass the <strong>-m</strong> parameter and the required mark in the command line:</p>

<pre><code class="language-python">pytest -s -v -m smoke test_fixture8.py</code></pre>

<p>If everything is correct, only the test with the smoke mark will be launched.</p>

<p>You will also see a warning:</p>

<pre><code class="language-bash">PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,</code></pre>

<p>The warning is displayed because the latest versions of PyTest insistently recommend to explicitly register marks before use. That allows avoiding typos – situations where you erroneously used a non-existent test mark and the test ends up being skipped.</p>

<h3>How are marks registered?</h3>

<p>Create a file pytest.ini in the root directory of your test project and add the following lines to the file:</p>

<pre><code class="language-no-highlight">[pytest]
markers =
    smoke: marker for smoke tests
    regression: marker for regression tests</code></pre>

<p>The text following the ":" sign is a commentary and may be skipped.</p>

<p>Run the tests again:</p>

<pre><code class="language-python">pytest -s -v -m smoke test_fixture8.py</code></pre>

<p>Now, there should be no warnings.</p>

<p> </p>

<p>You can also mark a whole test class. In that case, marking will be applied to all test methods included in the class.</p>
