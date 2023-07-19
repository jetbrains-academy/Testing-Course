<h2>Let's fix it quickly: time.sleep()</h2>

<p>Now that we know that the button is displayed with a delay,
we can add a wait before the element search starts.
We have already used the <strong>time</strong> library before. 
Let's apply it again:</p>

<pre><code class="language-python">import time

Expand All
	@@ -21,13 +21,13 @@ try:
finally:
    browser.quit()</code></pre>

<p>Now the test passes.
However, what if the message element also has a delay?
Shall we add another <strong>time.sleep()</strong> before the message search? 
And what if the delay time of the button display changes? 
Shall we increase the wait?
Besides, different computers with different internet speed may display
the button with different time lag.
Of course, we can add a wait before each step, 
but then a considerable part of the testing time will be consumed by fruitless waiting,
and with the increasing number of tests this problem will just get worse. </p>