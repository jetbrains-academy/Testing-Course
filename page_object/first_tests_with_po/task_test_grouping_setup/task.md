<h2>Task: test grouping and setup</h2>

<p><span style="color: #ff4363;"><strong>Important! </strong></span>Generally, manipulating the browser in the setup, especially performing checks, is bad practice. It's better not to do this without special necessity. Here, this example is purely for educational purposes, for you to try writing setups for tests. In real life, we would implement all these manipulations using an API or directly through the database.</p>

<p>In this task, we want to add test scenarios not only for website visitors but also for registered users. To achieve this:</p>

<ol>
	<li>In the <em>test_product_page.py</em> file, add a new class for tests named <strong>TestUserAddToBasketFromProductPage.</strong></li>
	<li>Add the already written tests <strong>test_guest_cant_see_success_message</strong> and <strong>test_guest_can_add_product_to_basket</strong> to this class and rename them, replacing <strong>guest</strong> with <strong>user</strong>. The test steps will remain the same; only registration will be added before the tests. Parameterization is not needed here; do not add it. </li>
	<li>Add a method <strong>register_new_user(email, password),</strong> to the <strong>LoginPage</strong>, which takes two strings and registers a user. Implement it by describing the corresponding page elements.</li>
	<li>In <strong>BasePage</strong>, add a check that the user is logged in:
	<pre><code>def should_be_authorized_user(self)</code>	</li>
	<li>Add a selector, accordingly, to <strong>BasePageLocators</strong>:
	<pre><code class="language-python">USER_ICON = (By.CSS_SELECTOR, "your selector")</code></pre>
	</li>
	<li>Add the setup fixture to the class. In this function, you need to:
	<ul>
		<li>Open the registration page.</li>
		<li>Register a new user.</li>
		<li>Check that the user is logged in.</li>
	</ul>
	</li>
	<li>Run both tests and make sure they pass and indeed register new users.</li>
</ol>

<p><strong>Note: </strong></p>

<p>You don't need to write <strong>yield</strong> — we don't know how to delete users. You can generate email addresses for users in different ways. One option, to avoid repetition, is to use the current time with the help of the <strong>time</strong> module:</p>

<pre><code class="language-python">import time # at the top of the file

email = str(time.time()) + "@fakemail.org"</code></pre>

<p> </p>

<ol>
</ol>
