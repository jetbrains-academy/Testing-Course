<h2>Finding elements with&nbsp;Selenium</h2>

<p>To find web page elements, Selenium WebDriver uses several strategies, which allow searching by element attributes, link text, CSS selectors, and XPath selectors. Selenium provides a search method find_element, which takes two arguments – locator type and locator value. The available search methods are the following:</p>

<ul>
	<li><strong>find_element(By.ID, value)</strong>&nbsp;&mdash; search by the unique id attribute of the element. If the developers provide a unique id to each application element, you are lucky and in most cases you will use this method, as it is the most stable;</li>
	<li><strong>find_element(By.CSS_SELECTOR, value)</strong>&nbsp;&mdash; search by CSS rules. This is a universal search method, as most web applications use CSS for page coding and designing. If you cannot use find_element_by_id due to the absence of element ids, you will most probably use this method in your tests;</li>
	<li><strong>find_element(By.XPATH, value)</strong>&nbsp;&mdash; search with the query language XPath, which offers great search flexibility;</li>
	<li><strong>find_element(By.NAME, value)</strong>&nbsp;&mdash; search by the element's name attribute;</li>
	<li><strong>find_element(By.TAG_NAME, value)</strong>&nbsp;&mdash; search by the element's tag name;</li>
	<li><strong>find_element(By.CLASS_NAME, value)</strong>&nbsp;&mdash; search by the value of the class attribute;</li>
	<li><strong>find_element(By.LINK_TEXT, value)&nbsp;</strong>&mdash; search for the exact match of a link;</li>
	<li><strong>find_element(By.PARTIAL_LINK_TEXT, value)&nbsp;</strong>&mdash; search for a link in case the selector text partly matches the link text.</li>
</ul>

<p>For example, we want to find a button with the id value id=&quot;submit_button&quot;:</p>

<pre>
<code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit")</code></pre>

<p>Notice that we imported the By class, which contains all possible locators.</p>

<p>If the page opened but nothing happens, return to the console where you ran the script. Most probably, you will see the <strong>NoSuchElementException</strong> error. It will look like this:</p>

<pre>
<code class="language-no-highlight">selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"submit"}</code></pre>

<p>The mistake is obvious: we identified the locator incorrectly and there is no button with such id on the page.</p>

<p>Let's fix the locator so that our code will not throw errors:</p>

<pre>
<code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")</code></pre>

<h3>Search for several elements</h3>

<p>You may face a situation when several page elements match your search parameters. In such a case, WebDriver&nbsp;will return only the first element it encounters in the HTML search. In case you rather need the second or further element, you either have to use a more specific search selector or use the <strong>find_element<span style="color:#ff4363"><u>s</u></span></strong> method,&nbsp;which we will discuss a bit later.</p>

<p>Sometimes, articles on Selenium WebDriver will use the term "locators", which refers to search strategies and the values by which the search is performed. For example, you can search by the locator By.ID with the value &quot;send_button&quot;.</p>
