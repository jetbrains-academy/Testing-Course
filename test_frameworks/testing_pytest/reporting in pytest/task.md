<h2>PyTest — reports</h2>

<p>You might have noticed that PyTest allows generating a detailed report supporting color schemes and formatting right out of the box.</p>

<p>Let's run our tests with unittest and PyTest once again and compare the outputted result.</p>

<p>We can see that in the PyTest report, the failed test is highlighted with a red font, which facilitates the process of log analysis.</p>

<p><strong>unittest:</strong></p>

<p><img alt="" src="https://ucarecdn.com/7cb1723f-3a3b-4fb6-a6bd-6a2e1904d02f/"></p>

<p><strong>PyTest: </strong></p>

<p><img alt="" src="https://ucarecdn.com/81ceab3c-0d25-4beb-ab87-09d110294d63/"></p>

<p>If we run PyTest with the parameter <strong>-v</strong> (<strong>verbose</strong>), the report will be supplemented with additional information – the list of tests and their execution statuses: </p>

<p><img alt="" src="https://ucarecdn.com/6a53144b-e083-410f-92ef-404511fc6c07/"></p>

<p>You can find other commands for manipulating the output of PyTest tests here: <a href="https://gist.github.com/amatellanes/12136508b816469678c2" rel="noopener noreferrer nofollow">Useful py.test commands.</a></p>