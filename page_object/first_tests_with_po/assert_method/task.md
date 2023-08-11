<h2>Проверка элемента на странице</h2>

<p>Чтобы выводить адекватное сообщение об ошибке, мы будем все проверки осуществлять с помощью assert и перехватывать исключения.</p>

<p>Для этого напишем вспомогательный метод поиска элемента в нашей базовой странице BasePage, который будет возвращать нам <code>True</code> или <code>False</code>. Можно сделать это по-разному (с настройкой явных или неявных ожиданий). Сейчас воспользуемся неявным ожиданием.</p>

<p>1. В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10:</p>

<pre><code class="language-python">def __init__(self, browser, url, timeout=10):
    self.browser = browser
    self.url = url
    self.browser.implicitly_wait(timeout)</code></pre>

<p>2. Теперь в этом же классе реализуем метод <code>is_element_present</code>, в котором будем перехватывать исключение. В него будем передавать два аргумента: <em>как </em>искать (css, id, xpath и тд) и собственно <em>что </em>искать (строку-селектор). </p>

<p>Чтобы перехватывать исключение, нужна конструкция <code>try/except</code>: </p>

<pre><code class="language-python">def is_element_present(self, how, what):
    try:
        self.browser.find_element(how, what)
    except (имя исключения):
        return False
    return True</code></pre>

<p>Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать: </p>

<pre><code>from selenium.common.exceptions import имя_исключения</code></pre>

<p>Отлично! Теперь для всех проверок, что элемент действительно присутствует на странице, мы можем использовать этот метод. </p>

<p>3. Теперь модифицируем метод проверки ссылки на логин так, чтобы он выдавал адекватное сообщение об ошибке: </p>

<pre><code>def should_be_login_link(self):
    assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"</code></pre>

<p>Запустите тесты и посмотрите, что вывод об ошибке стал более понятным: </p>

<pre><code>pytest -v --tb=line --language=en test_main_page.py</code></pre>
