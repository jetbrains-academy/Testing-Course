<h2><strong>PyTest: правила запуска тестов </strong></h2>

<p>В этом шаге мы коротко обсудим важные особенности запуска тестов с помощью PyTest. Когда мы выполняем команду <strong>pytest</strong>, тест-раннер собирает все тесты для запуска по определенным правилам:</p>

<ul>
	<li>
	<p>если мы не передали никакого аргумента в команду, а написали просто pytest, тест-раннер начнёт поиск в текущей директории</p>
	</li>
	<li>
	<p>как аргумент можно передать файл, путь к директории или любую комбинацию директорий и файлов, например: </p>
	</li>
</ul>

<pre><code class="language-python">pytest scripts/selenium_scripts
# найти все тесты в директории scripts/selenium_scripts

pytest test_user_interface.py
# найти и выполнить все тесты в файле 

pytest scripts/drafts.py::test_register_new_user_parametrized
# найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить 
</code></pre>

<ul>
	<li>
	<p>дальше происходит рекурсивный поиск: то есть PyTest обойдет все вложенные директории</p>
	</li>
	<li>
	<p>во всех директориях PyTest ищет файлы, которые удовлетворяют правилу  <strong>test_*.py</strong> или <strong>*_test.py</strong> (то есть начинаются на test_ или заканчиваются _test и имеют расширение .py)</p>
	</li>
	<li>
	<p>внутри всех этих файлов находит тестовые функции по следующему правилу:</p>

	<ul>
		<li>
		<p>все тесты, название которых начинается с <strong>test</strong>, которые находятся вне классов</p>
		</li>
		<li>
		<p>все тесты, название которых начинается с <strong>test</strong> внутри классов, имя которых начинается с <strong>Test</strong> (и без метода __init__ внутри класса)</p>
		</li>
	</ul>
	</li>
</ul>

<p>Подробности: <a href="https://docs.pytest.org/en/stable/goodpractices.html#conventions-for-python-test-discovery" rel="noopener noreferrer nofollow">Conventions for Python test discovery</a></p>