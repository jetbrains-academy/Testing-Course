<h2>Test Grouping: setup </h2>

<p>Now, let's leverage the magic of OOP for organizing the code of the test cases themselves. PyTest allows us to combine multiple test cases into one class. Why do this, and why is it convenient?</p>

<p><strong>Firstly,</strong> we can logically group tests into one class simply for the sake of more structured code. It's convenient when tests related to one component are in one class, and with <strong>pytest.mark</strong>, you can mark the entire class at once. The main rule is that the class name should start with <strong>Test</strong> so that PyTest can detect and run it.</p>

<p>For example, let's group two tests in the <em>test_main_page.py</em> file and mark it with the label <strong>login_guest</strong>:</p>

<pre><code class="language-python">
class TestLoginFromMainPage():
    # don't forget to pass self as the first argument                      
    def test_guest_can_go_to_login_page(self, browser):     
         # test implementation

    def test_guest_should_see_login_link(self, browser):
         # test implementation</code></pre>

<p>Try running the tests in this file indicating the <code>pytest test_main_page.py::TestLoginFromMainPage</code> class ( more details here: <a href="https://docs.pytest.org/en/7.1.x/how-to/usage.html">PyTest - usage </a> ). You'll notice that both tests have run, even though there's only one label. </p>

<p><strong>Secondly</strong>, for different test cases, you can use common functions to avoid repeating code. These functions are called <strong>setup —</strong> a function that will run before each test in the class, usually involving data preparation — and <strong>teardown —</strong> a function that runs AFTER each test in the class, typically handling the removal of data created during the test. A good automated test should work even on a clean database and clean up the data generated during the test. These functions are implemented using fixtures, which we covered in the previous module. To have a function run automatically before each test case, you need to mark it as <strong>@pytest.fixture</strong> with parameters <strong>scope="function"</strong>,meaning it runs for each function, and <strong>autouse=True</strong>,meaning it runs automatically without explicit fixture invocation.</p>

<p>We've already talked a bit about content independence in previous steps — an ideal solution would be to create a new product in our online store before each test where we work with the product page and delete it upon test completion. Unfortunately, our online store currently doesn't have the ability to create objects via an API. Still, in an ideal world, we would write a test class in the <em>test_product_page.py</em> as follows:</p>

<pre><code class="language-python">
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title = "Best book created by robot")
        # create a product with HTTP API
        self.link = self.product.link
        yield
        # after this keyword, teardown starts
        # executed after each test in the class
        # delete the data we created 
        self.product.delete()
        

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # next, common test implementation

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # next, common test implementation</code></pre>

<p>Working with an API is beyond the scope of this course, but the understanding that you can group tests and extract preparatory steps into unified functions for all tests is important for every automation engineer.</p>
