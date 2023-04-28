<h2>Fixture autouse</h2>

<p>While describing a fixture, we can indicate an additional parameter <strong>autouse=True,</strong> which shows that the fixture should be run for each test even without an explicit call: </p>

<p>test_fixture_autouse.py</p>

<pre><code class="language-python">import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")


class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        # the prepare_data fixture is not passed as a parameter but it's executed anyway
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")
</code></pre>

<p><img alt="" src="https://ucarecdn.com/0b70e723-548a-4b94-b01c-f5ff19ae3bfb/"></p>

<p>Try running that code, and you will see that the data preparation fixture is executed for each test without an explicit call. You need to be careful with this parameter because the fixture is run for all tests. Without an obvious necessity, fixture autouse should be avoided. </p>

<p><strong>Conclusion</strong></p>

<p>An auxiliary function is a powerful tool that solves numerous problems when working with automated tests. The major advantage is that they can be used in any tests without code duplication. </p>

<p>We strongly recommend reading additional material on fixtures:</p>

<p><a href="https://habr.com/ru/company/yandex/blog/242795/" rel="noopener noreferrer nofollow">https://habr.com/ru/company/yandex/blog/242795/</a></p>

<p><a href="https://docs.pytest.org/en/stable/fixture.html" rel="noopener noreferrer nofollow">https://docs.pytest.org/en/stable/fixture.html</a></p>