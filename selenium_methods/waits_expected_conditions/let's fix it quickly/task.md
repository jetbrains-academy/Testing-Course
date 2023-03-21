<h2>Давайте быстрее это починим: time.sleep()</h2>

<p>Теперь, когда мы уже знаем, что кнопка появляется с задержкой,
мы можем добавить паузу до начала поиска элемента.
Мы уже использовали библиотеку <strong>time</strong> ранее. 
Давайте применим ее и сейчас:</p>

<pre><code class="language-python">import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/wait1.html")
    time.sleep(3)
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")
    assert "successful" in message.text
finally:
    browser.quit()</code></pre>

<p>Теперь тест проходит.
Но что если элемент с сообщением тоже будет появляться с задержкой?
Добавить еще один <strong>time.sleep()</strong> перед поиском сообщения? 
А если изменится время задержки при появлении кнопки? 
Увеличим длительность паузы? 
А еще на разных машинах с разной скоростью интернета
кнопка может появляться через разные промежутки времени.
Можно перед каждым действием добавить задержку, 
но тогда значительную часть времени прогона тестов будут занимать бесполезные ожидания, 
при этом с увеличением количества тестов эта проблема будет только расти. </p>
