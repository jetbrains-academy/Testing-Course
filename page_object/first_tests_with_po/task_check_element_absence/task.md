<h2>Task: negative checks</h2>

<p>Add functions from the previous step to your project and implement several simple tests: </p>

<pre><strong>test_guest_cant_see_success_message_after_adding_product_to_basket: </strong></pre>

<ol>
	<li>Open the product page. </li>
	<li>Add the product to the cart. </li>
	<li>Check that there is no success message using <strong>is_not_element_present</strong>.</li>
</ol>

<p> </p>

<pre><strong>test_guest_cant_see_success_message</strong><strong>: </strong></pre>

<ol>
	<li>Open the product page. </li>
	<li>Check that there is no success message using <strong>is_not_element_present</strong>.</li>
</ol>

<p> </p>

<pre><strong>test_message_disappeared_after_adding_product_to_basket: </strong></pre>

<ol>
	<li>Open the product page.</li>
	<li>Add the product to the cart.</li>
	<li>Check that there is no success message using <strong>is_disappeared</strong></li>
</ol>

<p> </p>

<p><strong>Run all three tests and 
pay attention to the time it takes for each test.</strong></p>
