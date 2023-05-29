<h2>Task: test parametrization</h2>

<p>Aliens leave mysterious messages on Stepik as feedback for correctly solved tasks. We managed to localize several task URLs where fragments of these messages appear. Your task is to implement an automated test with the following steps:</p>

<ul>
	<li>open page </li>
	<li>authorise with your credentials (use code from previous step) </li>
	<li>enter correct answer to the task</li>
	<li>press 'Submit' button </li>
	<li>wait until correct feedback is presented </li>
	<li>check that text in feedback is <strong>"Correct!"</strong></li>
</ul>

<p>Feedback is this text on dark background </p>

![img.png](img.png)

<p>Correct anser to the task is the number:</p>

<pre><code>
import time
import math

answer = math.log(int(time.time()))
</code></pre>

<p>Use <strong>pytest</strong> parametrisation and pass this links as parameters to your test case: </p>

<p>https://stepik.org/lesson/236895/step/1<br>
https://stepik.org/lesson/236896/step/1<br>
https://stepik.org/lesson/236897/step/1<br>
https://stepik.org/lesson/236898/step/1<br>
https://stepik.org/lesson/236899/step/1<br>
https://stepik.org/lesson/236903/step/1<br>
https://stepik.org/lesson/236904/step/1<br>
https://stepik.org/lesson/236905/step/1</p>

<p>Use correct error messages in assertions and configure waits. </p>

<p>In the failed tests, find fragments of the aliens message. The test should fail if the text in the optional feedback does not match the string "Correct!".
Collect the fragments of text into one sentence and submit it as the string in answer.py file. </p>

<p><strong>Important! </strong>
To complete this task, make sure you have the correct local time set (<a href="https://time.is/" rel="noopener noreferrer nofollow">https://time.is/</a>). Additionally, each task's answer needs to be recalculated separately, as they become outdated otherwise. </p>
