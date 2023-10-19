<p><strong>Important! </strong>In this lesson, we will write a simple implementation of the Page Object pattern.
In the following lessons, we will explore existing frameworks and the ways
they can make our lives easier. Right now, the most crucial task
is to understand the principles of their work.&nbsp;</p>


<p>To start, let's create a base page from which all other classes will be inherited. 
In it, we will describe auxiliary methods for working with the web driver.</p>

<p>1. In the <code>base_page.py</code> file, create a class named <code>BasePage</code>.&nbsp;</p>

<p>In Python, such things are done using the following construct:&nbsp;</p>

<pre>
<code>class BasePage:</code></pre>

<p>2. Now we need to add methods to our class.
First of all, let's add a <em>constructor &mdash;&nbsp;</em>a method that is called when we create an object. A constructor is declared with the keyword <code>__init__</code>. As parameters, we pass an instance of the driver and the URL address. Inside the constructor, we save this data as attributes of our class. It looks like this:&nbsp;</p>

<pre>
<code class="language-python">def __init__(self, browser, url):
    self.browser = browser
    self.url = url</code></pre>

<p>3. Now let's add another method, open. It should open the required page in the browser using the get() method.</p>


<p>4. In conftest.py move browser fixture that we implemented in previous steps.</p>
<p>Declare the following in the same class:</p>
<pre>
<code class="language-python">def open(self):</code></pre>

<p>And implement this method: it only needs one line.
&nbsp;</p>
