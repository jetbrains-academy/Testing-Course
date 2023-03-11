<h2>Finding all necessary elements with find_elements</h2>

<p>We have already mentioned that the method <strong>find_element</strong> returns only the first of all possible elements matching the search conditions. In some situations, there may be several identical elements on a page: for example, the item icons in the shopping cart of an online store. In our test, we need to check that all selected goods are displayed. To do that, we can use the&nbsp;<strong>find_elements</strong> method, which, unlike <strong>find_element</strong>, returns the list of all the elements found according to the search condition. Having checked the list length, we can make sure the shopping cart contains the right number of items. Here's a sample code (the code is just an illustration, the site fake-shop.com most probably does not exist):</p>

<pre>
<code class="language-python"># test preparation
# opening the page of the first merchandise item
# the site does not exist, the code is just an example
browser.get("https://fake-shop.com/book1.html")

# adding the item to the cart
add_button = browser.find_element(By.CSS_SELECTOR, ".add")
add_button.click()

# opening the page of the second item
browser.get("https://fake-shop.com/book2.html")

# adding the item to the cart
add_button = browser.find_element(By.CSS_SELECTOR, ".add")
add_button.click()

# test scenario
# opening the cart
browser.get("https://fake-shop.com/basket.html")

# searching for added items
goods = browser.find_elements(By.CSS_SELECTOR, ".good")

# checking that the number of items equals 2
assert len(goods) == 2</code></pre>

<p><span style="color:#ff4363">!Important.</span> Note the important difference in the results returned by the methods <strong>find_element</strong> and <strong>find_elements</strong>. If the former method cannot find an element on a page, it throws the <strong>NoSuchElementException</strong> error, which interrupts code execution. The latter method always returns valid results: if nothing has been found, it returns an empty list and your program proceeds to executing its next code step.</p>
