<h2>Page Object for the main page of the website</h2>

<p>Now let's implement a Page Object that will be associated with the main page of the online store. </p>

<p>1. Open the file <code>main_page.py</code> </p>

<p>2. In it, create a class <code>MainPage</code>. It needs to inherit from the <code>BasePage</code> class. The parent class in Python is specified in parentheses: </p>

<pre><code>class MainPage(BasePage): </code></pre>

<p>This way, the MainPage class will have access to all the attributes and methods of its parent class. </p>

<p>3. Copy the method from the previous lesson into the <code>MainPage</code> class:</p>

<pre><code>def go_to_login_page(browser):
   login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
   login_link.click() </code></pre>

<p>To make everything work, we need to modify it slightly. There is no need to pass the browser instance as an argument anymore; we pass and save it during the creation of the Page Object. Instead, we need to specify the <code>self</code> argument to have access to the attributes and methods of the class: </p>

<p><code>def go_to_login_page(self):</code></p>

<p>Since our browser is stored as an argument of the <code>BasePage</code> class, you should access it appropriately using <code>self</code>: </p>

<pre><code class="language-python">self.browser.find_element(By.CSS_SELECTOR, "#login_link")</code></pre>
