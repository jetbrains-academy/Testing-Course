<h2>Запуск автотестов для разных языков интерфейса</h2>

<p>Цель: научиться запускать автотесты для разных локалей, т.е. для разных языков интерфейсов.</p>

<p>Мы уже запускали автотесты для разных языков в одном из предыдущих <a href="/lesson/237240/step/2" rel="noopener noreferrer nofollow">шагов</a>, используя параметризацию с помощью разных ссылок, но такой подход сложно масштабировать на большое количество тестов. Давайте сделаем так, чтобы сервер сам решал, какой язык интерфейса нужно отобразить, основываясь на данных браузера. Браузер передает данные о языке пользователя через запросы к серверу, указывая в Headers (заголовке запроса) параметр <strong>accept-language</strong>. Если сервер получит запрос с заголовком {accept-language: ru, en}, то он отобразит пользователю русскоязычный интерфейс сайта. Если русский язык не поддерживается, то будет показан следующий язык из списка, в данном случае пользователь увидит англоязычный интерфейс. Это, кстати, примерно то же самое, что и выставить предпочтительный язык в настройках своего браузера: </p>

<p><img alt="" height="254" src="https://ucarecdn.com/03bd7599-7838-4f35-8e4f-19656a4ea049/" width="612"></p>

<p>Чтобы указать язык браузера с помощью WebDriver, используйте класс Options и метод <strong>add_experimental_option</strong>, как указано в примере ниже:</p>

<pre><code class="language-language-python language-python">from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
browser = webdriver.Chrome(options=options)
</code></pre>

<p>Для Firefox объявление нужного языка будет выглядеть немного иначе:</p>

<pre><code class="language-language-python language-python">fp = webdriver.FirefoxProfile()
fp.set_preference("intl.accept_languages", user_language)
browser = webdriver.Firefox(firefox_profile=fp)
</code></pre>

<p><em>В конструктор webdriver.Chrome или webdriver.Firefox вы можете добавлять разные аргументы, расширяя возможности тестирования ваших веб-приложений: можно указывать прокси-сервер для контроля сетевого трафика или запускать разные версии браузера, указывая локальный путь к файлу браузера. Предполагаем, что эти возможности вам понадобятся позже и вы сами сможете найти настройки для этих задач.</em></p>