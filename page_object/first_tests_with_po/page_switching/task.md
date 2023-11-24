<h2>Switching between pages</h2>

<p>Switching can be implemented in two different ways. </p>

<p>The first way is to return the required Page Object.</p>

<p>To do this, you need to import the login page in the main_page.py file: </p>

<pre><code class="language-python">from .login_page import LoginPage</code></pre>

<p>Then, in the method that navigates to the login page, initialize a new Page object and return it: </p>

<pre><code class="language-python">def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    return LoginPage(browser=self.browser, url=self.browser.current_url) </code></pre>

<p>Pay attention! When creating the object, we must pass the same driver object for interacting with the browser, and as the URL, we pass the current address.</p>

<p>Now, in the test, we don't need to worry about page initialization; it's already created. By saving the returned value in a variable, we can use the methods of the new page in the test:</p>

<pre><code>def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()</code></pre>

<p>Pros of this approach: </p>

<ul>
	<li>The test looks neater—no need to initialize the page in the test body.</li>
	<li>We explicitly return the page—the page type is associated with the method.</li>
	<li>No need to think about page initialization in different tests—code duplication is reduced.</li>
</ul>

<p>Cons: </p>

<ul>
	<li>If there is a large number of pages and transitions, there will be many cross-imports.</li>
	<li>Higher code cohesion—changing the logic requires changing the returned value.</li>
	<li>Harder to understand the code since the page is initialized implicitly.</li>
	<li>Circular dependencies are formed, often leading to errors.</li>
</ul>

<p>The second approach is implicit transition; the page is initialized in the test body: </p>

<p>1. Comment out the line with the returned value </p>

<pre><code class="language-python">def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    # return LoginPage(browser=self.browser, url=self.browser.current_url) </code></pre>

<p>2. Initialize LoginPage in the test body (don't forget to import the required class): </p>

<pre><code>from .pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()</code></pre>

<p>Pros:</p>

<ul>
	<li>Less code cohesion.</li>
	<li>Fewer imports, no cross-imports.</li>
	<li>More flexibility.</li>
	<li>Clearer understanding of what is happening in the test, as we explicitly initialize the page.</li>
</ul>

<p>Cons:</p>

<ul>
	<li>An extra step is added to the test case.</li>
	<li>Every time a test is written, you need to think about correct transitions.</li>
	<li>Code duplication.</li>
</ul>

<p>Both approaches can be successfully applied in your projects; the key is to do it wisely. For now, let's stick with the second option with explicit page initialization in the test body to avoid unnecessary complexities with circular dependencies. </p>
