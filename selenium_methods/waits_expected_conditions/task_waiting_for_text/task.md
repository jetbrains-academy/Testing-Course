<h2>Task: waiting for the required text on the page</h2>

<p>Let's now try to write a program that will make a vacation cabin reservation at a strictly defined price. Higher prices are unacceptable, while in the case of a lower price, the cabin will be immediately rented by someone else.</p>

<p>In this task, you need to write a program according to the following scenario:</p>

<ol>
	<li>Open the page <a href="http://suninjuly.github.io/explicit_wait2.html" rel="noopener noreferrer nofollow">http://suninjuly.github.io/explicit_wait2.html</a>.</li>
	<li>Wait till the cabin rent goes down to $100 (set the wait no lower than 12 seconds).</li>
	<li>Click the "Book" button.</li>
	<li>Solve a familiar arithmetical problem (use the previously written code)</li>
</ol>

<p>To find the moment when the rent drops to $100, use the <strong>text_to_be_present_in_element</strong> method from the <strong>expected_conditions</strong> library.</p>

<p>If you do it all correctly and fast enough, you'll see a window with a number in it. Submit this number as an answer for the task.</p>
