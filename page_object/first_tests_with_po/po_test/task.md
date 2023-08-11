<h2>Первый тест на основе&nbsp;Page Object</h2>

<p>Ура, первый прототип страницы мы уже реализовали! Давайте теперь перепишем тест с помощью Page Object:&nbsp;</p>

<p>1. Откройте файл с вашим тестом&nbsp;<em>test_main_page.py</em></p>

<p>2. В самом верху файла нужно импортировать класс, описывающий главную страницу:&nbsp;</p>

<p>3. Теперь преобразуем сам тест в <em>test_main_page.py</em>:&nbsp;</p>

<pre>
<code class="language-python">from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # initializing page object 
    page.open()                      # opening page
    page.go_to_login_page()          # using page method to open login page 
</code></pre>

<p>4. Убедитесь, что тест проходит, запустив его все той же командой:&nbsp;</p>

<pre>
<code>pytest -v --tb=line --language=en test_main_page.py
</code></pre>

<p>Теперь наш тест <strong>почти </strong>полностью написан в модном стиле Page Object! Почему <strong>почти&nbsp;</strong>&mdash; узнаете в следующих шагах.</p>
