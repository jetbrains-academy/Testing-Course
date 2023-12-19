<h2><strong>Benefits of inheritance: example</strong></h2>

<p>In the previous lesson, we wrote a test "a guest can go to the login page from the main store page." However, if you look closely at the other pages, you'll notice that the link to the login page is present on every page. If we want to add a test "a guest can go to the login page from the product page," to avoid duplication, it makes sense to move the relevant methods to the BasePage class. Let's do just that: </p>

<p>In the <em>locators.py</em> file, create a new class <strong>BasePageLocators</strong><em> </em>and move the corresponding elements there:</p>

<pre><code>class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")</code></pre>

<p>Move the corresponding methods to the <em>base_page.py</em> file, replacing the locator class with BasePageLocators:  </p>

<pre><code>from .locators import BasePageLocators


class BasePage():
...
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
... </code></pre>

<p><em>Note: It's best to describe methods in the class in alphabetical order, making it easier to navigate and find them.</em></p>

<p>In the <strong>MainPage</strong><em> </em>class, we have no methods left, so let's add a placeholder: </p>

<pre><code>class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)</code></pre>

<p>As you already know, the<strong> __init__ </strong>method is called when an object is created. The constructor above with the <strong>super </strong>keyword actually only calls the constructor of the parent class and passes to it all the arguments that we passed to the <strong>MainPage</strong> constructor. </p>

<p>Now we can easily add tests like "a guest can go to the login page from page X." </p>

<p>Add new tests to the <em>test_product_page.py</em> file: </p>

<pre><code>def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()</code></pre>

<p>Add the second test on your own </p>

<pre><strong>test_guest_can_go_to_login_page_from_product_page</strong> 
</pre>

<p>Run the tests and make sure they pass. </p>
