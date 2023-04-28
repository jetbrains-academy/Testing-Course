<h2>Task: exceptions</h2>

<p>Now we know how to set up waits in element search. 
While searching, WebDriver checks every 0.5 second whether
the required element has appeared in the browser's DOM model
(Document Object Model  is an "object model of a document", an interface for accessing the HTML content of the site).
If an error occurs, WebDriver will throw one of the following
<strong>exceptions</strong>:</p>

<ul>
	<li>If the element has not been found within the allocated time, we will receive <strong>NoSuchElementException.</strong></li>
	<li>If the element was found during the search but the DOM was changed at a later access attempt, we'll receive <strong>StaleElementReferenceException</strong>. For example, we found the <strong>Button</strong> element and in a while decided to apply the familiar click method to it. If the button got overlapped by the script over that time, there's no use applying the method — the element became "stale", and we'll see an exception.</li>
	<li>If the element was found during the search but the element itself is invisible (e.g., it has zero dimensions) and a real user wouldn't be able to interact with it, we'll receive  <strong>ElementNotVisibleException</strong>.</li>
</ul>

<p>Understanding the reasons behind the exceptions will help you in tweaking tests
and locating bugs in programs.</p>

<p><strong>Task:</strong></p>

<p>What error will you see in the console if you try executing the <strong> browser.find_element(By.ID,</strong> <strong>"button")</strong> command after opening the page <a href="http://suninjuly.github.io/cats.html" rel="noopener noreferrer nofollow">http://suninjuly.github.io/cats.html</a>?</p>
