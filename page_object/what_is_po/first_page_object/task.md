<h2>Task: writing abstract methods </h2>


Now let's rewrite our script from [waiting task](course://selenium_methods/waits_expected_conditions/task_waiting_for_text)
in pytest style and using abstract methods to make test more human-readable.
Firstly, implement methods in step.py, using your code from [waiting task](course://selenium_methods/waits_expected_conditions/task_waiting_for_text)
Then, implement test in task.py using these methods. 

<li>Open the page <a href="http://suninjuly.github.io/explicit_wait2.html" rel="noopener noreferrer nofollow">http://suninjuly.github.io/explicit_wait2.html</a>.</li>
<li>Wait till the cabin rent goes down to $100 (set the wait no lower than 12 seconds).</li>
<li>Click the "Book" button.</li>
<li>Assert an element with text "Math is a real magic!" element is presented</li>
<li>Solve a familiar arithmetical problem</li>