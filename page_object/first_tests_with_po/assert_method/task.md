<h2>Checking an element on a page</h2>

<p>To display an appropriate error message, we will perform all checks using assert and catch the exceptions.</p>

<p>For this purpose, let's write a helper method to find an element on our BasePage, which will return either <code>True</code> or <code>False</code>. This can be done in various ways (with explicit or implicit waits). For now, let's use implicit waiting.</p>

<p>1. In the constructor of BasePage, let's add a command for implicit waiting with a default value of 10:</p>

<pre><code class="language-python">def __init__(self, browser, url, timeout=10):
    self.browser = browser
    self.url = url
    self.browser.implicitly_wait(timeout)</code></pre>

<p>2. Now, in the same class, we'll implement the <code>is_element_present</code> method, where we will catch the exception. We will pass two arguments to it: <em>how </em>to search (css, id, xpath, etc.) and <em>what </em>to search for (the selector string). </p>

<p>To catch the exception, we need a <code>try/except</code> construct: </p>

<pre><code class="language-python">def is_element_present(self, how, what):
    try:
        self.browser.find_element(how, what)
    except (name of exception):
        return False
    return True</code></pre>

<p>To import the required exception, you need to specify the following at the very top of the file: </p>

<pre><code>from selenium.common.exceptions import exception_name</code></pre>

<p>Great! Now, we can use this method for all checks on the presence of an element on the page. </p>

<p>3. Now, let's modify the method for checking the login link so that it provides an appropriate error message: </p>

<pre><code>def should_be_login_link(self):
    assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"</code></pre>

<p>Run the tests and see that the error output has become more understandable: </p>

<pre><code>pytest -v --tb=line --language=en test_main_page.py</code></pre>
