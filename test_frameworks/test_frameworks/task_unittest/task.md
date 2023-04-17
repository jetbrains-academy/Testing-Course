<h2>Task: writing tests in the unittest style</h2>

<p>Try to rewrite the tests from the first module in the unittest style.</p>

Take the [step](course://introduction/finding_elements_selenium/task10)  from the first 
section and rewrite your tests in the unittest style.



<ul>
	<li>In test.py, create a class with tests which will inherit from <strong>unittest.TestCase</strong> like in the previous step.</li>
	<li>Rewrite the test for the page <a href="http://suninjuly.github.io/registration1.html" rel="noopener noreferrer nofollow" target="_blank" title="Link: http://suninjuly.github.io/registration1.html">http://suninjuly.github.io/registration1.html</a> in the unittest style.</li>
	<li>Rewrite the second test for the page <a href="http://suninjuly.github.io/registration2.html" rel="noopener noreferrer nofollow" target="_blank" title="Link: http://suninjuly.github.io/registration1.html">http://suninjuly.github.io/registration2.html</a> in the unittest style.</li>
	<li>Format the final checks in the tests in the unittest style: for example, use the <a href="https://docs.python.org/3/library/unittest.html#assert-methods" rel="noopener noreferrer nofollow">assertEqual</a> method.</li>
	<li>Run the tests.</li> 
	<li>Look through the test report and find the last line.</li> 
</ul>

Insert the line into [answer.txt](file://test_frameworks/test_frameworks/task_unittest/answer.txt). 

<p>Notice that the second test is supposed to throw NoSuchElementException. If you use the try/except construct, you need to run the test without it here. You don't need to catch exceptions (at least, in this case)!</p>

<p>All that is supposed to illustrate that unittest will execute tests and summarize the results even if an unexpected exception is thrown. </p>

<p>Do not delete your code after completing the task – you will need it in the following lesson. </p>
