<h2>Working with the browser in Selenium</h2>

<p>If you have already tried running sample scripts, you might have noticed that the browser does not always close after executing the code. Thus, make sure to explicitly close the browser window in code using the command <strong>browser.quit().</strong> Each time you open the browser <code>browser = webdriver.Chrome()</code>, the system launches a process which will remain there unless you manually close the browser window. In order not to run out of RAM after launching several scripts, always add the closing command to your scripts:</p>

<pre><code>from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()

# closing the browser after all operations
browser.quit()</code></pre>

<p>It's also important to clarify the difference between the two commands:<strong> browser.close()</strong> and<strong> browser.quit()</strong>. They both seem to do the same thing, so what's the difference? </p>

<p>Actually, <strong>browser.close() </strong>closes the current browser window. Thus, if your script has initiated a pop-up window or opened something in a new window or tab, only the current window will close and the rest will remain open. Meanwhile, <strong>browser.quit() </strong>closes all windows, tabs, and WebDriver processes launched during the testing session. You can find more details here: <a href="https://stackoverflow.com/questions/15067107/difference-between-webdriver-dispose-close-and-quit" rel="noopener noreferrer nofollow">Difference between webdriver.Dispose(), .Close() and .Quit()</a>. Be cautious with these methods and use <strong>browser.quit()</strong> in general cases.</p>

<p>Now, what if the script does not proceed as far as executing that final step and crashes with an error at some point earlier? </p>

<p>In order to guarantee closing, even if there occurred an error in the preceding lines, the <strong>try/finally</strong> construct is the easiest solution:</p>

<pre><code>from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # closing the browser after all operations
    browser.quit()</code></pre>

<p>You can try launching both examples. Notice the difference.</p>

<p>We won't talk about exception processing in detail now. You just need to understand that even if an error occurs inside the <strong>try</strong> block, the code in the <strong>finally</strong> block will be executed anyway. We suggest adding such processing to all your scripts when doing the tasks of this module and the next one; in the third module, we'll discuss more concise constructs.</p>

<p>If you want to learn more about exceptions – how they are thrown, caught, and handled – we recommend studying the lesson <a href="https://stepik.org/lesson/24463/step/1?unit=6771" rel="noopener noreferrer nofollow">Errors and exceptions</a>.</p>

<p>(Thanks to our student <a href="https://stepik.org/users/41632287" rel="noopener noreferrer nofollow">Mikhail λ</a> for his comments and suggestions.)</p>
