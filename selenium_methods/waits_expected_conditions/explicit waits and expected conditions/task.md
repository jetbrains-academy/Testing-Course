<h2>Explicit Waits (WebDriverWait и expected_conditions)</h2>

<p>В предыдущем шаге мы решили проблему с ожиданием элементов на странице. Однако методы <strong>find_element</strong> проверяют только то, что элемент появился на странице. В то же время элемент может иметь дополнительные свойства, которые могут быть важны для наших тестов. Рассмотрим пример с кнопкой, которая отправляет данные:</p>

<ul>
	<li>Кнопка может быть неактивной, то есть её нельзя кликнуть;</li>
	<li>Кнопка может содержать текст, который меняется в зависимости от действий пользователя. Например, текст "Отправить" после нажатия кнопки поменяется на "Отправлено";</li>
	<li>Кнопка может быть перекрыта каким-то другим элементом или быть невидимой.</li>
</ul>

<p>Если мы хотим в тесте кликнуть на кнопку, а она в этот момент неактивна, то WebDriver все равно проэмулирует действие нажатия на кнопку, но данные не будут отправлены.</p>

<p>Давайте попробуем запустить следующий тест:</p>

<pre><code class="language-python">from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait2.html")
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    browser.quit()</code></pre>

<p>Мы видим, что WebDriver смог найти кнопку с<strong> id="verify" </strong>и кликнуть по ней, но тест упал на поиске элемента "<strong>verify_message</strong>" с итоговым сообщением:</p>

<pre><code>no such element: Unable to locate element: {"method":"id","selector":"verify_message"}</code></pre>

<p>Это произошло из-за того, что WebDriver быстро нашел кнопку и кликнул по ней, хотя кнопка была еще неактивной. На странице мы специально задали программно паузу в 1 секунду после загрузки сайта перед активированием кнопки, но неактивная кнопка в момент загрузки — обычное дело для реального сайта.</p>

<p>Чтобы тест был надежным, нам нужно не только найти кнопку на странице, но и дождаться, когда кнопка станет кликабельной. Для реализации подобных ожиданий в Selenium WebDriver существует понятие <strong>явных</strong> ожиданий (<strong>Explicit Waits</strong>), которые позволяют задать специальное ожидание для конкретного элемента. Задание явных ожиданий реализуется с помощью инструментов WebDriverWait и <strong>expected_conditions</strong>. Улучшим наш тест:</p>

<pre><code class="language-python">
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/wait2.html")
    button = browser.find_element(By.ID, "verify")  
    # waiting for 5 seconds until button will be enabled
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
finally:
    browser.quit()
</code></pre>

<p><strong>element_to_be_clickable </strong>вернет элемент, когда он станет кликабельным, или вернет <strong>False </strong>в ином случае.</p>

<p>Обратите внимание, что в объекте WebDriverWait используется функция <strong>until</strong>, в которую передается правило ожидания, элемент, а также значение, по которому мы будем искать элемент. В модуле <strong>expected_conditions</strong> есть много других правил, которые позволяют реализовать необходимые ожидания:</p>

<ul>
	<li>title_is</li>
	<li>title_contains</li>
	<li>presence_of_element_located</li>
	<li>visibility_of_element_located</li>
	<li>visibility_of</li>
	<li>presence_of_all_elements_located</li>
	<li>text_to_be_present_in_element</li>
	<li>text_to_be_present_in_element_value</li>
	<li>frame_to_be_available_and_switch_to_it</li>
	<li>invisibility_of_element_located</li>
	<li>element_to_be_clickable</li>
	<li>staleness_of</li>
	<li>element_to_be_selected</li>
	<li>element_located_to_be_selected</li>
	<li>element_selection_state_to_be</li>
	<li>element_located_selection_state_to_be</li>
	<li>alert_is_present</li>
</ul>

<p>Описание каждого правила можно найти на <a href="https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions" rel="noopener noreferrer nofollow">сайте</a>.</p>

<p>Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода <strong>until_not</strong>:</p>

<pre><code class="language-python"># говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )</code></pre>
