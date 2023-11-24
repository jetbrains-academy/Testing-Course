<h2>Task: Data Independence</h2>

<p>Good automated tests should be as independent of data as possible. The worst thing you can do in a test is to "hardcode" checks for objects that exist only in your specific instance. Why? Because the data will constantly change, and with each such change, you'll have to fix the automated tests. It also hinders method reuse; for example, if you want to run a test for multiple products, you'll have to write a large number of checks: one for each product. Ultimately, this affects the product's quality, as such tests operate on a narrow selection of pages.</p>

<p>General recommendation: your tests should not depend on things you cannot control. This could be information already stored in the database or third-party services used by your application. You can check specific data only when using a specially prepared test database initiated before each test run, or when adding the necessary data directly to the database or through the application's API.&nbsp;</p>

<p>Try running the automated test we wrote in the previous step on the page&nbsp;<a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019" rel="noopener noreferrer nofollow" style="font-size: inherit; font-weight: inherit;">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019</a>.</p>

<p>If in the previous test, after adding the product to the cart, you checked for a fixed string &quot;The shellcoder&#39;s handbook&quot; in the site's message, the test will fail because we've now added a different product. If the test passes, you've done well, and you can simply insert the new validation code into this task..&nbsp;</p>

<p>To make the test independent of content:&nbsp;</p>

<ul>
	<li>Modify the verification methods to accept the product name and price as arguments.</li>
	<li>Create a method that extracts the text—the product name—from an element and returns it.</li>
	<li>Create a similar method for the price.</li>
	<li>Now, check that the product name in the message matches the product header.</li>
</ul>
