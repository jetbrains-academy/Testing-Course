<h2>Task: run autotests for different interface languages</h2>

<p>We want our internet store to work equally well for users from any country.
To make sure that our solution for supporting multiple languages works,
we will run a set of autotests for each language. 
As autotest developer, you need to implement a solution that will allow running autotests for different user languages
and passing the needed language from the command line at launch time.</p>

<ol>
	<li>Add a handler that reads the language parameter from the command line to the conftest.py file.</li>
	<li>In the conftest.py file, implement the logic of launching the browser with the chosen user language. The browser has to be declared in the browser fixture and passed as a parameter to the test.</li>
	<li>In the test_items.py file, write a test with the following scenario: 
        <ul> - Open the page with the merchandise item <a href="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/" rel="noopener noreferrer nofollow">http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/</a>.</ul>
        <ul> - Find the button for adding the item to the cart.</ul>
        <ul> - Check that after clicking the button, there appears an element signifying that the item was added successfully.</ul> </li>
	<li>The test needs to be launched with the language parameter by the following command:
	<pre>
<code class="language-bash">pytest --language=es test_items.py</code></pre>
	It has to pass successfully. It will be enough if the test works for the Сhrome browser only.</li>
