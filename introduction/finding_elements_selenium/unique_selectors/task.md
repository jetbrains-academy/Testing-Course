<h2>Unique selectors: part 2</h2>

<p>Let's try to realize one of the automated tests from the previous step. You are given a <a href="http://suninjuly.github.io/registration1.html" rel="nofollow noopener noreferrer">page</a> with a registration form. Check if it's possible to get registered at the site having filled in the mandatory fields only – those marked with the * symbol: first name, last name, email. The text in the fields may be arbitrary. The success of registration is checked by the comparison of the expected text &quot;Congratulations! You have successfully registered!&quot; with the text on the page opened after the registration. To compare the texts, let's use Python's standard&nbsp;"assert" construct.</p>

<p>Below you have a template of the code that you need to use for the test. Remember that selectors must be unique.</p>

<p>Let's talk more about the "assert" construct from the example. If the result of comparing "Congratulations! You have successfully registered!" == welcome_text returns False, the <strong>assert False</strong><strong> </strong> code will be executed next. It will throw an exception&nbsp;AssertionError and the number of the line where the error occurred. If the code was written correctly and previously worked, such a result would mean that our automated test has discovered a bug in the web application. If the test returns True, the <strong>assert True</strong> statement will be executed. In such a case, no error will be thrown and the test will pass successfully. We will talk in more detail about using "assert" in code in the third module of our course.</p>

<p>This task does not contain automated checks of your code. Just make sure your test runs successfully and you don't get an AssertionError in the results of your code.</p>

<p><strong>Comment</strong></p>

<p>In this example, we used the <strong>time.sleep(1)</strong> method to wait till the next page is loaded before running the tests. If you start your code without this method, your code may suddenly fail, even if it ran smoothly before. Without such a pause,&nbsp;WebDriver&nbsp;may proceed to searching for the h1 tag too early, before the new page has loaded. In such a case, we'll see the following error in the terminal:</p>

<pre>
<code class="language-python">NoSuchElementException... Unable to locate element: {"method":"tag name","selector":"h1"}</code></pre>

<p>The time.sleep(1)&nbsp;method tells Python to wait for 1 second before executing the next code line. If you see the error anyway, just increase the number of waiting time seconds.</p>

<p>The problem of timely element search is one of the major problems one needs to solve when developing automated UI tests. When the internet connection speed keeps changing and the server load is uneven, the time of page loading may significantly vary. Another factor affecting test stability is the principle of asynchronous execution of JavaScript code. You may not notice it on simple pages, but in functionally rich pages the time of page elements' loading may be unpredictable. Tests should be organized so that to avoid the situation when they fail due to unstable internet connection or other reasons beyond your control.</p>

<p>Solving this problem with time.sleep()&nbsp;is considered bad practice because it is difficult to know the necessary waiting time beforehand. If the set waiting time is too long, the tests will take unnecessarily long time. In the following lessons, we will discuss more elegant and efficient ways of solving this problem. Meanwhile, we'll use time.sleep() for the sake of clarity and simplicity.</p>
