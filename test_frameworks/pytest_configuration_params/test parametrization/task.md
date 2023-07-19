<h2>Test parametrization</h2>

<p>PyTest allows running the same test with different input parameters. To do that, use the <strong>@pytest.mark.parametrize()</strong> decorator. Our site is available in various languages. Let's write a test that checks that the Russian- and English-language site displays a link to the log-in form. We'll pass the links to the Russian and English versions of our site's front page to our tests.</p>

<p>We need to pass the parameter that may change and the list of parameter values to <strong>@pytest.mark.parametrize()</strong>. In the test itself, the parameter should also be passed as an argument. Notice that inside the decorator, the name of the parameter is put in quotes, while the list of test arguments does not require quotes.</p>

<p><strong>test_fixture7.py: </strong></p>

<pre><code class="language-python">import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")</code></pre>

<p>Let's run the test:</p>

<pre><code class="language-bash">pytest -s -v test_fixture7.py</code></pre>

<p>You'll see that two tests have been started. The name of each test contains the used parameter in square brackets. Thus, we can quickly and without code duplication increase the number of checks for similar scenarios.</p>

<p><img alt="" src="https://ucarecdn.com/9dd11f43-4180-4e16-850d-28095f139da3/"></p>

<p>We can also use parametrization for the whole test class so that all the tests in the class would run with the set parameters. In that case, the parametrization mark must precede the declaration of the class: </p>

<pre>
<code>@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        # this test will be launched 2 times

    def test_guest_should_see_navbar_element(self, browser, language):
        #this test will be launched 2 times
</code></pre>

<p>Here's a helpful additional tutorial from the documentation: <a href="https://docs.pytest.org/en/latest/how-to/parametrize.html?highlight=parametrize" rel="noopener noreferrer nofollow">Parametrizing fixtures and test functions</a>.</p>