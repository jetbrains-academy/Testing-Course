<h2>Task: Inheritance and negative checks</h2>

<p>In the<em> test_main_page.py</em> file, add a test with the following description:</p>

<p><samp><strong> test_guest_cant_see_product_in_basket_opened_from_main_page:</strong></samp></p>

<ol>
	<li>A visitor opens the main page. </li>
	<li>They navigate to the cart using the button in the site header.</li>
	<li>We expect that there are no items in the cart.</li>
	<li>We expect that there is a text indicating that the cart is empty. </li>
</ol>

<p>In the <em>test_product_page.py </em>file, add a test with the following description:</p>

<p><strong><samp>test_guest_cant_see_product_in_basket_opened_from_product_page:</samp></strong></p>

<ol>
	<li>A visitor opens the product page.</li>
	<li>They navigate to the cart using the button in the site header. </li>
	<li>We expect that there are no items in the cart.</li>
	<li>We expect that there is a text indicating that the cart is empty. </li>
</ol>

<p>In the <strong>BasePage</strong> class, implement the corresponding method for navigating to the cart. Create a file named <em>basket_page.py</em> and define the <strong>BasketPage</strong> class in it. Implement the necessary checks there, including the negative check that we discussed in the previous steps. </p>
