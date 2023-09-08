<h2>PyTest — pros and cons</h2>

Additional links: 

https://realpython.com/pytest-python-testing/

https://www.guru99.com/pytest-tutorial.html

<p>Let's consider the advantages of using PyTest:</p>

<p>1) PyTest is fully backwards compatible with the unittest and nosetest frameworks. That means that if you initially wrote your tests using unittest, you can instantly switch to PyTest. To do that, make sure that the PyTest package is installed in your virtual environment. Don't forget to activate your virtual environment and install PyTest.</p>

<p><strong>In Windows:</strong></p>

<pre><code>&gt; selenium_env\Scripts\activate.bat 
(selenium_env) С:\Users\user\environments&gt;  pip install pytest==7.1.2</code></pre>

<p><strong>In Linux and macOS:</strong></p>

<pre><code class="language-bash">​​​​​​​$ source selenium_env/bin/activate 

(selenium_env) $ pip install pytest==7.1.2</code></pre>

<p>Now we can run the tests in our <em>test_abs_project.py </em>file with PyTest without modifying the file. PyTest will find the tests in the folder you run them from and will execute them:</p>

<pre><code class="language-bash">pytest test_abs_project.py</code></pre>

<p>2) A detailed report supporting color schemes out of the box.</p>

<p>3) Unlike unittest, PyTest does not require writing additional specific constructs in test (no boilerplate).</p>

<p>4) Python's standard assert is used in checks.</p>

<p>5) It's possible to create dynamic fixtures (special functions setting up test environments and preparing test data).</p>

<p>6) Additional features in setting up fixtures.</p>

<p>7) Test parametrization – you can set up different parameters for the same test (the test will be run several times with different test data).</p>

<p>8) Availability of marks, which mark tests for selective launching.</p>

<p>9) Possibility to pass additional parameters in the command line to set up test environments.</p>

<p>10) A large number of plugins, which expand the capacity of PyTest and allow solving specific problems and save time.</p>

<p>Let's look at the disadvantages of PyTest:</p>

<p>1) Unlike unittest, PyTest is not included in Python's standard library package and has to be installed separately. Don't forget about that when you set up automated test runs with the CI server.</p>

<p><br>
2) The use of PyTest requires a deeper understanding of Python, which is needed, for example, in applying fixtures, parametrization, and other PyTest features.</p>
