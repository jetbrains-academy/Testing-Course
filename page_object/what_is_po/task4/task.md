<h2>What is Page Object Model?</h2>

<p><strong>Page Object Model</strong> or just Page Object is a programming pattern that is very popular in test automation and is one of the standards of web product test automation. Besides, it is one of handy methods of structuring your code to make it easier to maintain, modify, and work with.</p>

<p>The main point is that each page of a web application may be described as a class object. The user's interactions with the page may be described with class methods. In the ideal case, the test using a Page Object needs to describe the business logic of the test scenario and hide Selenium's methods of interaction with the browser and the page. If the page coding changes, we won't need to fix the tests connected with the page. Instead, we'll only need to fix the class describing the page.</p>

<p>Thus, we use the same principles as in development: we want to improve code readability and move all details to abstract methods. Tests need to be written in a simple and understandable way, and recurring pieces of code need to go to separate functions. In the Page Object, we separate the logic of actions (e.g., authorizing the user) from the specific realization (find the email field, insert the data, find the password field, insert the data, find the button, etc.). </p>

<p>Let's consider a simple test case:</p>

<ol>
	<li>Open the main page</li>
	<li>Go to the log-in page</li>
</ol>

<p>The expected result:</p>

<p>The log-in page is opened</p>

<p> </p>

<p>Let's look at a piece of code from the test from the previous module, which implements the first part of our test:</p>

<p><em>test_main_page.py:</em></p>

<pre><code class="language-python">link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
</code></pre>

<p>What happens here?</p>

<p>We open the link, find the element with a certain selector, and click the element.</p>

<p>What do we actually mean in terms of semantics?</p>

<p>We want to open the log-in page. 
Let's isolate this action into a separate function with a meaningful name, in the same file <em>test_main_page.py</em> for now:</p>

<pre><code class="language-python">def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()</code></pre>

<p>Our test becomes simpler:</p>

<pre><code>def test_guest_can_go_to_login_page(browser): 
   browser.get(link) 
   go_to_login_page(browser) </code></pre>

<p>In subsequent tests, when we will need to go from the main page to the log-in page, we won't need to copy this piece of code again – we can use the already written method.</p>

<p> At the moment, we have just isolated the logical action of the user that may be reused into an abstract method.
In the following steps, we'll see how to create a Page Object from that. </p>

<p>You can find additional information about Page Object here:</p>

<p><a href="https://github.com/SeleniumHQ/selenium/wiki/PageObjects" rel="noopener noreferrer nofollow">https://github.com/SeleniumHQ/selenium/wiki/PageObjects</a></p>

<p><a href="https://martinfowler.com/bliki/PageObject.html" rel="noopener noreferrer nofollow">https://martinfowler.com/bliki/PageObject.html</a></p>


<p><a href="https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b" rel="nofollow noopener noreferrer">https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b</a></p>

