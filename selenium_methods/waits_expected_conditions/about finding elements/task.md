<h2>Как работают методы get и find_element</h2>

<p>Разберем еще один простой тест на WebDriver, проверяющий работу кнопки.</p>

<p>Тестовый сценарий выглядит так:</p>

<ol>
	<li>Открыть страницу <a href="http://suninjuly.github.io/wait1.html" rel="noopener noreferrer nofollow">http://suninjuly.github.io/wait1.html</a></li>
	<li>Нажать на кнопку "Verify"</li>
	<li>Проверить, что появилась надпись "Verification was successful!"</li>
</ol>

<p>Для открытия страницы мы используем метод get, затем находим нужную кнопку с помощью одного из методов find_element_by_ и нажимаем на нее с помощью метода click. Далее находим новый элемент с текстом и проверяем соответствие текста на странице ожидаемому тексту.</p>

<p>Вот как выглядит код автотеста:</p>

<pre><code class="language-python">
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/wait1.html")
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message") 
    assert "successful" in message.text
finally: 
    browser.quit()
    
</code></pre>

<p>Попробуйте запустить автотест.
Aвтотест упадет с сообщением NoSuchElementException для элемента 
c <strong>id="verify"</strong>. Почему так происходит?</p>
<p>Команды в Python выполняются синхронно, то есть, строго последовательно. Пока не завершится команда get, не начнется поиск кнопки. Пока кнопка не найдена, не будет сделан клик по кнопке и так далее.</p>

<p>Но тест будет работать абсолютно стабильно,
только если в данной веб-странице не используется JavaScript
(что маловероятно для современного веба). 
<br>
Метод get дожидается информации от браузера о том, что страница загружена,
и только после этого наш тест переходит к поиску кнопки. 
Если страница интерактивная, то браузер будет считать, что страница загружена, 
при этом продолжат выполняться загруженные браузером скрипты. 
Скрипт может управлять появлением кнопки на странице и показывать ее, 
например, с задержкой, чтобы кнопка красиво и медленно возникала на странице. 
В этом случае наш тест упадет с уже известной нам ошибкой NoSuchElementException, 
так как в момент выполнения команды
<code>button = browser.find_element(By.ID, "verify")</code> элемент с <strong>id="verify"</strong> еще не отображается на странице. 
На данной странице пауза перед появлением кнопки установлена на 1 секунду, 
метод <strong>find_element()</strong> сделает только одну попытку найти элемент и в
случае неудачи уронит наш тест.</p>
