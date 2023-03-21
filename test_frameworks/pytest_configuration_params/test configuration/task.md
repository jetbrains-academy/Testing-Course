<h2>Conftest.py&nbsp;&mdash; конфигурация тестов</h2>

<p>Ранее мы добавили&nbsp;фикстуру browser, которая создает нам экземпляр браузера для тестов в данном файле. Когда файлов с тестами становится больше одного, приходится в каждом файле с тестами описывать данную фикстуру. Это очень неудобно. Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать файл<strong> conftest.py,</strong> который должен лежать в директории верхнего уровня в вашем проекте с тестами. Можно создавать дополнительные файлы conftest.py в других директориях, но тогда настройки в этих файлах будут применяться только к тестам в под-директориях.</p>

<p>Создадим файл <strong>conftest.py</strong> в корневом каталоге нашего тестового проекта&nbsp;и перенесем туда фикстуру <strong>browser</strong>. Заметьте, насколько лаконичнее стал выглядеть файл с тестами.</p>

<p><strong>conftest.py:</strong></p>

<pre>
<code class="language-python">import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()</code></pre>

<p>Теперь, сколько бы файлов с тестами мы ни&nbsp;создали, у тестов будет доступ к фикстуре browser. Фикстура передается в тестовый метод в качестве аргумента. Таким образом&nbsp;можно удобно переиспользовать одни и те же вспомогательные функции в разных частях проекта.</p>

<p><br />
<strong>test_conftest.py:</strong></p>

<pre>
<code class="language-python">from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")</code></pre>

<h3><span style="color:#ff4363"><strong>ОЧЕНЬ&nbsp;ВАЖНО!&nbsp;</strong></span></h3>

<p>Есть одна важная особенность поведения конфигурационных файлов, о которой вы обязательно должны знать. PyTest автоматически находит и подгружает файлы conftest.py, которые находятся в директории с тестами. Если вы храните все свои скрипты для курса в одной директории, будьте аккуратны и следите,&nbsp;чтобы не возникало ситуации, когда вы запускаете тесты из папки tests:</p>

<pre>
<code class="language-no-highlight">tests/
├── conftest.py
├── subfolder
│   └── conftest.py
│   └── test_abs.py

следует избегать!</code></pre>

<p>В таком случае применяются ОБА файла&nbsp;conftest.py, что может вести к непредсказуемым ошибкам и конфликтам.&nbsp;&nbsp;</p>

<p>Таким образом можно переопределять разные фикстуры, но мы в рамках курса рекомендуем придерживаться одного файла на проект/задачу&nbsp;и держать их горизонтально, как-нибудь так:&nbsp;</p>

<pre>
<code class="language-no-highlight">selenium_course_solutions/
├── section3
│   └── conftest.py
│   └── test_languages.py
├── section4 
│   └── conftest.py
│   └── test_main_page.py

правильно!</code></pre>

<p>Будьте внимательны и следите, чтобы не было разных conftest во вложенных друг в друга директориях, особенно, когда будете скачивать&nbsp;и проверять задания сокурсников.</p>

<p><a href="https://docs.pytest.org/en/7.1.x/how-to/fixtures.html?highlight=fixture%20folder#override-a-fixture-on-a-folder-conftest-level" rel="noopener noreferrer nofollow">Override a fixture on a folder (conftest) level</a></p>
