<h2>The execute_script method</h2>

<p>Let's talk about one more helpful and powerful method, which requires at least basic understanding of JavaScript. With the help of the execute_script method, you can run a program written in JavaScript as part of the automated test scenario in your browser. You may wonder why we need that, as in automated tests we try to interact with the site interface as a common user – clicking buttons, selecting menu items, and entering text in text fields.</p>

<p>The reason is that standard methods available in Selenium cannot cover all possible situations in the work of a web application. Internet sites may solve a range of tasks – from a simple blog to complex financial or graphical applications. Implementing business scenarios, developers have access to a great number of libraries, which results in web pages with non-standard text editors, unique menus, original video players, etc. Consequently, in order to press a seemingly common button, testers need to write a real JavaScript scenario. If you find yourself in such a situation, first address your frontend developers, who may suggest a sample of the required script. Before using the script in your tests, you can check its work right in your browser – run the code in the browser console. Then, you can add it to your automated test: execute_script(javascript_code).</p>

<p>Let's try to trigger an alert in the browser with the help of WebDriver. Here's a sample scenario:</p>

<pre><code class="language-python">from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
</code></pre>

<p>Notice that the executable JavaScript should be put in quotes (single or double). If you also need to use quotes within the script and you have already used double quotes to mark the script, use single quotes inside the script:</p>

<pre><code class="language-python">browser.execute_script("document.title='Script executing';")</code></pre>

<p>The following format will also work:</p>

<pre><code class="language-python">browser.execute_script('document.title="Script executing";')</code></pre>

<p>With this method, we can execute multiple instructions at a time – list them separated by semicolons. Let's first change the page title and then trigger an alert:</p>

<pre><code class="language-python">browser.execute_script("document.title='Script executing';alert('Robots at work');")</code></pre>
