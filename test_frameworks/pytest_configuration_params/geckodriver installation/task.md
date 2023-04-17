<h2>Installing Firefox and Selenium geckodriver</h2>

<p>So far, we've launched our tests only in Chrome, but what if we need to test our web application in other browsers, too? We will run the same tests, but when launching them, we will indicate what browser they need to be run on. Let's take Firefox as the second browser, as it is the second most popular browser and it may be run on any platform. We will launch our tests with the parameter browser_name using the following command:</p>

<pre><code>pytest -s -v --browser_name=firefox test_cmd.py</code></pre>

<p>Now we'll need to remember all the pains of installing chromedriver from the lesson <a href="https://stepik.org/lesson/25969/" rel="noopener noreferrer nofollow">https://stepik.org/lesson/25969/</a> and execute a similar scenario for installing Firefox and a Selenium driver for it.</p>

<p>To install Firefox, download it from the official site and run the installation program in your OS: <a href="https://www.mozilla.org/firefox/new/" rel="noopener noreferrer nofollow">https://www.mozilla.org/firefox/new/</a>.</p>

<p>The Selenium driver for Firefox is called geckodriver. Download its latest version from the site <a href="https://github.com/mozilla/geckodriver/releases" rel="noopener noreferrer nofollow">https://github.com/mozilla/geckodriver/releases</a> and unpack it into the C:\geckodriver folder in Windows or /usr/local/bin in Ubuntu and macOS. You can find detailed installation instructions here: <a href="https://selenium-python.com/install-geckodriver" rel="noopener noreferrer nofollow">https://selenium-python.com/install-geckodriver</a>. In Windows, don't forget to add the folder C:\geckodriver to the PATH system variable and restart the command line to make the path available.</p>

<p>To make sure that geckodriver was installed correctly, run the following commands in the Python interpreter:</p>

<pre><code class="language-python">from selenium import webdriver

# initializing the browser driver. After running this command, you will see a new browser window
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")

</code></pre>

<p>If you see a new browser window and the link opened in it, you can proceed to the next step.</p>

<p>If you see the following message while running the code:</p>

<pre><code class="language-python">selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. </code></pre>

<p>it means that geckodriver hasn't been installed and its path isn't defined in the system. Repeat all the installation steps. If Firefox still doesn't launch, describe all your actions and add a detailed error log in the comments so that we could help you.</p>