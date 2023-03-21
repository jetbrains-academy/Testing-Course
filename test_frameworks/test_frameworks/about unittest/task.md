<h2>unittest</h2>

<p>Тест-раннеры сами находят тестовые методы в указанных при запуске файлах, но для этого нужно следовать общепринятым правилам. Общее правило для всех фреймворков: название тестового метода должно начинаться со слова "test_".  Дальше может идти любой текст, который является уникальным названием для теста:</p>

<pre><code class="language-python">def test_name_for_your_test():</code></pre>

<p>Для unittest существуют собственные дополнительные правила:</p>

<ul>
	<li>Тесты обязательно должны находиться в специальном тестовом классе.</li>
	<li>Вместо assert должны использоваться специальные assertion методы.</li>
</ul>

<p>Давайте теперь изменим наши предыдущие тесты, чтобы их можно было запустить с помощью unittest. Для этого нам понадобится выполнить следующие шаги:</p>

<ol>
	<li>Импортировать unittest в файл: <strong>import unittest</strong></li>
	<li>Создать класс, который должен наследоваться от класса TestCase: <strong>class TestAbs(unittest.TestCase):</strong></li>
	<li>Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: <strong>def test_abs1(self):</strong></li>
	<li>Изменить assert на <strong>self.assertEqual()</strong></li>
	<li>Заменить строку запуска программы на <strong>unittest.main()</strong></li>
</ol>

<pre><code class="language-python">import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
        
if __name__ == "__main__":
    unittest.main()
</code></pre>

<p>После изменений запустим наш файл с тестами всё так же с помощью Python:</p>

<pre><code class="language-bash">python test_abs_project.py

.F

======================================================================

FAIL: test_abs2 (__main__.TestAbs)

----------------------------------------------------------------------

Traceback (most recent call last):

  File "test_abs_project.py", line 9, in test_abs2

    self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

AssertionError: Should be absolute value of a number

----------------------------------------------------------------------

Ran 2 tests in 0.000s

FAILED (failures=1)</code></pre>

<p>Теперь мы видим более подробную информацию о результатах запуска: было запущено два теста, один тест выполнился с ошибкой. Место ошибки и пояснение к ней отображаются в логе.</p>

<p>В следующем уроке мы рассмотрим преимущества и особенности использования тестового фреймворка <strong>PyTest</strong>. Если вы хотите использовать <strong>unittest</strong> ﻿в своих проектах, вы можете изучить <a href="https://docs.python.org/3/library/unittest.html" rel="nofollow noopener noreferrer">документацию</a> самостоятельно.</p>