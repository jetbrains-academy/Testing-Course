<h2>Page Object для главной страницы сайта</h2>

<p>Теперь реализуем Page Object, который будет связан с главной страницей интернет-магазина. </p>

<p>1. Откройте файл <code>main_page.py</code> </p>

<p>2. В нем создайте класс  <code>MainPage</code>. Его нужно сделать наследником класса <code>BasePage</code>. Класс-предок в Python указывается в скобках: </p>

<pre><code>class MainPage(BasePage): </code></pre>

<p>таким образом, класс MainPage будет иметь доступ ко всем атрибутам и методам своего класса-предка. </p>

<p>3. Перенесите метод из предыдущего урока в класс <code>MainPage</code>:</p>

<pre><code>def go_to_login_page(browser):
   login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
   login_link.click() </code></pre>

<p>Чтобы все работало, надо слегка видоизменить его. В аргументы больше не надо передавать экземпляр браузера, мы его передаем и сохраняем на этапе создания Page Object. Вместо него нужно указать аргумент <code>self</code> , чтобы иметь доступ к атрибутам и методам класса: </p>

<p><code>def go_to_login_page(self):</code></p>

<p>Так как браузер у нас хранится как аргумент класса <code>BasePage</code>, обращаться к нему нужно соответствующим образом с помощью <code>self</code>: </p>

<pre><code class="language-python">self.browser.find_element(By.CSS_SELECTOR, "#login_link")</code></pre>
