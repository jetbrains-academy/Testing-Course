<h2>Тестовые сценарии</h2>

<p>Созданные тесты нужно сохранить в файле, чтобы его было удобно
запускать и хранить в системе контроля версий.
Давайте создадим файл<strong> test_abs_project.py</strong> и напишем в нём следующий код:</p>

<pre><code class="language-python">def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number" 

if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")</code></pre>

<p>Мы поместили тестовый сценарий в функцию для разделения тест-кейсов и возможности их независимого запуска.</p>

<p>Не вдаваясь в подробности, скажем только, что конструкция <strong>if __name__ == "__main__"</strong> служит для подтверждения того, что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля. Весь код написанный в теле этого условия будет выполнен только если пользователь запустил файл самостоятельно. Подробнее можно ознакомиться в видео <a href="https://www.youtube.com/watch?v=cW_-zGG4ef4" rel="noopener noreferrer nofollow" target="_blank">Олега Молчанова</a>. </p>

<p>В этой конструкции мы вызвали функцию<strong> test_abs1()</strong>, которая выполняет тестовый сценарий.</p>

<p>С помощью <strong>print("All tests passed!")</strong> мы вывели сообщение, если все тесты прошли успешно.</p>

<p>Чтобы запустить тест, выполните в консоли команду:</p>

<pre><code class="language-bash">python test_abs_project.py</code></pre>

<p>Вы должны увидеть в консоли сообщение<strong> "All tests passed!"</strong>.</p>

<p> </p>

<p>Если нам нужно добавить еще один тест, мы можем написать его как функцию в этом же файле. В приведенном примере мы уже не увидим сообщение "Everything passed", так как падение любого теста вызывает выход из программы:</p>

<pre><code class="language-python">def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")
</code></pre>

<p>Запустите файл снова. Вы должны увидеть сообщение об упавшем втором тесте:</p>

<pre><code>
$ python test_abs_project.py

Traceback (most recent call last):

  File "test_abs_project.py", line 9, in &lt;module&gt;

    test_abs2()

  File "test_abs_project.py", line 5, in test_abs2

    assert abs(-42) == -42, "Should be absolute value of a number"

AssertionError: Should be absolute value of a number
</code></pre>