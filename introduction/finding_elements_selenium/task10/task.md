<h2>Task: unique selectors</h2>

<p>We already have a simple test from the previous step, which checks the possibility of registering at a site. However, developers decided to slightly modify the coding of the page to make it look more up-to-date. The updated page is available at a different&nbsp;<a href="http://suninjuly.github.io/registration2.html" rel="nofollow noopener noreferrer" target="_blank" title="Link: http://suninjuly.github.io/registration2.html">link</a>. Unfortunately, while modifying the page, the developers accidentally left a bug in the registration form.</p>

<p>Try running the code from the previous step with the new&nbsp;<a href="http://suninjuly.github.io/registration2.html" rel="nofollow noopener noreferrer" target="_blank" title="Link: http://suninjuly.github.io/registration2.html">link</a> as the start page. If your test crashes with the NoSuchElementException error, it means that you have chosen the right selectors and found the bug left by the developers. That's good. It means that your tests did work. Don't get scared, it's an error in the application you're testing, not in your test.&nbsp;</p>

<p>If your test ran successfully, it means that the test has overlooked a serious bug. In such a case, try changing the selectors and making them unique. After the change, make sure that the test runs well on the old version of the&nbsp;<a href="http://suninjuly.github.io/registration1.html" rel="nofollow noopener noreferrer" target="_blank" title="Link: http://suninjuly.github.io/registration1.html">page</a>.</p>

<ol>
	<li>
	<p>The test runs successfully on the page&nbsp;<a href="http://suninjuly.github.io/registration1.html" rel="noopener noreferrer nofollow" title="Link: http://suninjuly.github.io/registration1.html">http://suninjuly.github.io/registration1.html</a>.﻿</p>
	</li>
	<li>
	<p>The test crashes with NoSuchElementException&nbsp;<a href="http://suninjuly.github.io/registration2.html" rel="nofollow noopener noreferrer" title="Link: http://suninjuly.github.io/registration2.html">http://suninjuly.github.io/registration2.html</a>.</p>
	</li>
	<li>
	<p>The used selectors must be unique.</p>
	</li>
</ol>
