<h2>Плагины и перезапуск тестов</h2>

<p>Для PyTest написано большое количество <a href="https://docs.pytest.org/en/latest/explanation/flaky.html?highlight=plugins#plugins" rel="nofollow noopener noreferrer" title="Link: https://docs.pytest.org/en/latest/plugins.html">плагинов</a>, то есть ﻿дополнительных модулей, которые расширяют возможности этого фреймворка. Полный список доступных плагинов доступен <a href="https://docs.pytest.org/en/latest/reference/plugin_list.html" rel="nofollow noopener noreferrer">здесь</a>.</p>

<p>Рассмотрим еще одну проблему, с которой вы обязательно столкнетесь, когда будете писать end-to-end тесты на Selenium. Flaky-тесты или "мигающие" авто-тесты, т.е. такие тесты, которые по независящим от нас внешним обстоятельствам или из-за трудновоспроизводимых багов, могут иногда падать, хотя всё остальное время они проходят успешно. Это может происходить в момент прохождения тестов из-за одновременного обновления сайта, из-за сетевых проблем или странных стечений обстоятельств. Конечно, надо стараться исключать такие проблемы и искать причины возникновения багов, но в реальном мире бывает, что это требует слишком много усилий. Поэтому мы будем перезапускать упавший тест, чтобы еще раз убедиться, что он действительно нашел баг, а не упал случайно.</p>

<p>Это сделать очень просто. Для этого мы будем использовать плагин <strong>pytest-rerunfailures</strong>.</p>

<p>Сначала установим плагин в нашем виртуальном окружении. После установки плагин будет автоматически найден PyTest, и можно будет пользоваться его функциональностью без дополнительных изменений кода:</p>

<pre><code class="language-bash">pip install pytest-rerunfailures</code></pre>

<p>Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:</p>

<p><strong>"--reruns n"</strong>, где n — это количество перезапусков. Если при повторных запусках тесты пройдут успешно, то и прогон тестов будет считаться успешным. Количество перезапусков отображается в отчёте, благодаря чему можно позже анализировать проблемные тесты.﻿﻿<br>
Дополнительно мы указали параметр <strong>"--tb=line"</strong>, чтобы сократить лог с результатами теста. Можете почитать подробнее про настройку вывода в <a href="https://docs.pytest.org/en/stable/usage.html#modifying-python-traceback-printing" rel="noopener noreferrer nofollow">документации PyTest</a>:</p>

<pre><code class="language-bash">pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py</code></pre>

<p>Давайте напишем два теста: один из них будет проходить, а другой — нет. Посмотрим, как выглядит перезапуск.</p>

<p><strong>test_rerun.py:</strong></p>

<pre><code class="language-python">link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")</code></pre>

<p>Мы увидим сообщение: "1 failed, 1 passed, 1 rerun in 9.20s﻿", то есть упавший тест был перезапущен, но при втором запуске тоже упал. Если бы во второй раз мигающий тест все-таки прошёл успешно, то мы бы увидели сообщение: ﻿﻿"2 passed, 1 rerun in 9.20s"﻿, и итоговый результат запуска всех тестов считался бы успешным.</p>