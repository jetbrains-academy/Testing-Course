<h2>Why exactly Page Object?</h2>

<p>We can, of course, save all the logic of our tests in a single file named, for example, steps.py, and for starters, that's not too bad. However, if we are testing a large web product with numerous states and transitions, that file may grow to an enormous size and it will be hard to find the needed method in it. Besides, there are situations when logically the same method has different realizations in different pages. For example, our web store may have a method "add to the cart", and the user can add merchandise to the cart both from the catalogue page and from the specific merchandise page.</p>

<p>It might be convenient to separate the methods logically related to one web page of our product into a specific class in our code. Hence the name — Page Object. It is an abstract object containing the methods of working with a certain web page.</p>

<p><strong>Important! </strong>Usually, Page Object methods are of two kinds: <em>do something</em> and <em>check something.</em></p>

<p>Let's consider a merchandise page in a web store: <a href="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/</a>.</p>

<p>What methods could a Page Object associated with such a page have? Let's list the main scenarios: </p>

<ul>
	<li>add an item to the cart;</li>
	<li>check if there is a message about successfully adding it to the cart;</li>
	<li>proceed to writing feedback;</li>
	<li>check the presence of the item's name, price, and description;</li>
	<li>return to the main page.</li>
</ul>

<p>Notice that all the checks also turn into separate methods. The test case itself doesn't have any supplemental words, like assert, any more; only the description of steps is left. Just like in our test documentation. </p>

<p>The tests will look more or less as follows:</p>

<pre><code class="language-python">def test_add_to_cart(browser):
    page = ProductPage(url="", browser)   # initializing page object
    page.open()                           # opening page in the browser
    page.should_be_add_to_cart_button()   # asserting button is on the page
    page.add_product_to_cart()            # pressing button
    page.should_be_success_message()      # asserting message with text is on the page
</code></pre>

Thus, tests become more abstract and straightforward. All the details of abstract method realization are hidden inside the Page Object methods and, if necessary, may be reused in different tests.
