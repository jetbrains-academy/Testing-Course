<h2>Convenience of test maintenance—encapsulation of business logic in methods</h2>

<p>What should you do if the logic of interaction with a page used in several of our tests changes? For instance, suppose we need to verify the ability to navigate to the login page through the navbar link for each page on the site. Let's assume there are 20 such pages, and consequently, we have 20 tests using the <strong>go_to_login_page</strong> methods in the MainPage class. Then, developers added an alert triggered by clicking the link we're interested in. We'll notice that all 20 tests fail because the go_to_login_page method lacks a step to handle the alert, meaning the should_be_login_page method won't work. By adding alert handling to the <strong>go_to_login_page</strong> method, we can restore the functionality of all tests without modifying the tests themselves:</p>

<pre>
<code class="language-python">def go_to_login_page(self):
   link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
   link.click()
   alert = self.browser.switch_to.alert
   alert.accept()</code></pre>

<p>This is another advantage of using the Page Object pattern—it separates the test itself from the page interaction logic. The test becomes more readable and is easier to maintain in case of changes in the application code.</p>
