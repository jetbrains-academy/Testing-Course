<h2>Финализаторы — закрываем браузер</h2>

<p>Вероятно, вы заметили, что мы не использовали в этом примере команду <strong>browser.quit()</strong>. Это привело к тому, что несколько окон браузера оставались открыты после окончания тестов, а закрылись только после завершения всех тестов. Закрытие браузеров произошло благодаря встроенной фикстуре — сборщику мусора. Но если бы количество тестов насчитывало больше нескольких десятков, то открытые окна браузеров могли привести к тому, что оперативная память закончилась бы очень быстро. Поэтому надо явно закрывать браузеры после каждого теста. Для этого мы можем воспользоваться <strong>финализаторами</strong>. Один из вариантов финализатора — использование ключевого слова Python: <strong>yield</strong>. После завершения теста, который вызывал фикстуру, выполнение фикстуры продолжится со строки, следующей за строкой со словом <strong>yield</strong>:</p>

<p>test_fixture3.py</p>

<pre><code class="language-python">import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group &gt; a")
</code></pre>

<p>Есть альтернативный способ вызова teardown кода с помощью встроенной фикстуры <strong>request</strong> и ее метода <strong>addfinalizer</strong>. Можете изучить его сами по документации <a href="https://docs.pytest.org/en/latest/how-to/fixtures.html#adding-finalizers-directly" rel="nofollow noopener noreferrer">PyTest</a>. </p>

<p>Рекомендуем также выносить очистку данных и памяти в фикстуру, вместо того чтобы писать это в шагах теста: финализатор выполнится даже в ситуации, когда тест упал с ошибкой. </p>