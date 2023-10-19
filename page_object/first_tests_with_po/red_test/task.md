<h2>Verification methods in Page Object</h2>

<p>Let's now automate another test case and see, through an example, how to create verification methods. </p>

<p>Suppose we need to check the following scenario: </p>

<ol>
	<li>Open the main page. </li>
	<li>Check if there is a link leading to login. </li>
</ol>

<p>For this, in the MainPage class, we need to implement a method that will check the presence of the link. Typically, all such verification methods are named similarly; we will call them should_be_(element name). </p>

<p>So, in the MainPage class, create the method <code>should_be_login_link</code>. </p>

<p>For the first attempt, you can implement it in the simplest way: </p>

<pre><code>def should_be_login_link(self):
    self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")</code></pre>

<p>Currently, we intentionally made the selector incorrect to see what the test will report when it catches a bug. This is a good practice: writing red tests first and only then making them green. </p>

<p>Let's add a new test to the test case file: </p>

<pre><code class="language-python">def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()</code></pre>

<p>Run the resulting test: </p>

<pre><code>pytest -v --tb=line --language=en test_main_page.py</code></pre>

<p>The error output is not very clear, right? It's quite challenging to understand what went wrong exactly. Therefore, in the next step, we will need to handle the exception thrown by the WebDriver. </p>
