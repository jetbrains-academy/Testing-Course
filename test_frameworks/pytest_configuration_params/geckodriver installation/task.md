<h2>Установка Firefox и Selenium-драйвера geckodriver</h2>

<p>До этого момента мы запускали наши тесты только в браузере Chrome, но что делать, если нужно тестировать наше веб-приложение и в других браузерах? При этом мы будем запускать те же тесты, но при запуске тестов указывать, на каком браузере нужно запускать тесты. Возьмем в качестве второго браузера Firefox, так как он является вторым по популярности браузером, и его можно запустить на любой платформе. Запускать тесты мы хотим, указывая при запуске параметр browser_name, такой командой:</p>

<pre><code>pytest -s -v --browser_name=firefox test_cmd.py</code></pre>

<p>Сейчас нам придется вспомнить муки установки chromedriver из урока <a href="https://stepik.org/lesson/25969/" rel="noopener noreferrer nofollow">https://stepik.org/lesson/25969/</a> и повторить похожий сценарий установки браузера Firefox и Selenium-драйвера для него.</p>

<p>Для установки Firefox скачайте его с официального сайта и установите в вашей ОС: <a href="https://www.mozilla.org/firefox/new/" rel="noopener noreferrer nofollow">https://www.mozilla.org/firefox/new/</a>.</p>

<p>Selenium-драйвер для Firefox носит название geckodriver. Скачайте последнюю версию geckodriver с сайта <a href="https://github.com/mozilla/geckodriver/releases" rel="noopener noreferrer nofollow">https://github.com/mozilla/geckodriver/releases</a> и распакуйте его в папку C:\geckodriver на Windows, /usr/local/bin на Ubuntu и macOS. Для более подробной инструкции по установке geckodriver смотрите <a href="https://selenium-python.com/install-geckodriver" rel="noopener noreferrer nofollow">https://selenium-python.com/install-geckodriver</a>. Для Windows не забудьте добавить в системную переменную PATH папку C:\geckodriver и перезапустить командную строку, чтобы путь стал доступен.</p>

<p>Чтобы проверить правильность установки geckodriver, выполните в интерпретаторе Python команды:</p>

<pre><code class="language-python">from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")

</code></pre>

<p>Если вы увидели, как запустилось новое окно браузера Firefox и открылась указанная ссылка, то можете переходить к следующему шагу.</p>

<p>Если при попытке выполнения кода вы увидели подобное сообщение:</p>

<pre><code class="language-python">selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH. </code></pre>

<p>значит, geckodriver не установлен или к нему не прописан путь в системе. Повторите заново действия по установке. Если Firefox всё равно не запускается, то напишите в комментариях последовательность ваших действий и подробный лог ошибки, чтобы мы могли вам помочь.</p>