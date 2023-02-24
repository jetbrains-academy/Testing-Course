<h2>Выбор test runner</h2>

<p>В предыдущих шагах мы научились писать простые тесты и запускать их с помощью Python. Приведём здесь код тестов и результаты запуска из предыдущего шага еще раз.</p>

<p><strong>test_abs_project.py:</strong></p>

<pre><code class="language-python">def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")

</code></pre>

<p>Консоль:</p>

<pre><code>
$ python test_abs_project.py

Traceback (most recent call last):

  File "test_project.py", line 9, in &lt;module&gt;

    test_abs2()

  File "test_project.py", line 5, in test_abs2

    assert abs(-42) == -42, "Should be absolute value of a number"

AssertionError: Should be absolute value of a number
</code></pre>

<p>Рассмотрим минусы такого подхода к запуску автотестов:</p>

<ul>
	<li>Когда тестов становится много, сложно становится запускать только тесты из нужных тест-сьютов.</li>
	<li>Для каждого теста нужно создавать тестовые данные и окружение отдельно. Например, если мы захотим для каждого теста запускать браузер, а после завершения теста браузер закрывать, то логику работы с браузером придется дублировать в коде каждого теста.</li>
	<li>Если один из тестов завершится с ошибкой, например, тест упадёт с ошибкой AssertionError, то последующие тесты не запустятся. Мы не узнаем, были ли проблемы в этих тестах, пока не починим упавший тест или пока не запустим эти тесты по отдельности.</li>
</ul>

<p>Для решения этих проблем и упрощения написания и запуска тестов существуют специальные фреймворки, которые называются test runners (тест-раннеры). Можно выделить три основных тестовых фреймворка для Python: <strong>unittest</strong>, <strong>PyTest</strong> и <strong>nose</strong>. Модуль <strong>unittest</strong> является встроенным инструментом Python — и это его большой плюс. <strong>PyTest</strong> и <strong>nose</strong> устанавливаются дополнительно, они позволяют получить расширенные возможности по сравнению с <strong>unittest</strong>. Мы кратко рассмотрим, как используется <strong>unittest</strong>, а затем изучим возможности <strong>PyTest</strong>, который позволяет писать более простой код тестов по сравнению с <strong>unittest</strong> и гибко настраивать запуск тестов. Еще один плюс использования <strong>PyTest</strong> в том, что для него существует большое количество плагинов, которые позволяют решить практически любую проблему, связанную с запуском автотестов.</p>