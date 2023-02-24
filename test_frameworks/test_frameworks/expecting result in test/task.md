<h2>Проверка ожидаемого результата</h2>

<p>Как можно проверить ожидаемый результат? Для этого используется встроенная в Python инструкция <strong>assert</strong>, которая проверяет истинность утверждений. <strong>assert True</strong> не приводит к выводу дополнительных сообщений, а вот <strong>assert False</strong> вызовет исключение <strong>AssertionError</strong>.</p>

<p>Рассмотрим работу assert на примере встроенной функции <strong>abs</strong>(), которая возвращает абсолютное значение числа по модулю. Для этого активируйте созданное ранее виртуальное окружение и запустите интерпретатор Python. </p>


<p>Теперь будем вводить приведенные ниже команды и смотреть на результат их выполнения.</p>

<p>Если значение выражения истинно, то в консоли не должно появиться дополнительных сообщений. Выполним:</p>

<pre><code>&gt;&gt;&gt; assert abs(-42) == 42

</code></pre>

<p>Если условие не выполнено, то в консоли выводится лог ошибки с названием файла и номером строчки, в которой произошла ошибка, а также тип ошибки <strong>AssertionError</strong>:</p>

<pre><code>
&gt;&gt;&gt; assert abs(-42) == -42

Traceback (most recent call last):

  File "&lt;stdin&gt;", line 1, in &lt;module&gt;

AssertionError
</code></pre>

<p>Простое сообщение <strong>AssertionError</strong> не очень информативно. Когда тестов становится много, бывает сложно вспомнить, что именно мы проверяем в данном тесте. Для добавления дополнительного сообщения можно при вызове assert через запятую написать нужное сообщение, которое будет выведено в случае ошибки проверки результата:</p>

<pre><code>
&gt;&gt;&gt; assert abs(-42) == -42, "Should be absolute value of a number"

Traceback (most recent call last):

  File "&lt;stdin&gt;", line 1, in &lt;module&gt;

AssertionError: Should be absolute value of a number
</code></pre>

<h2 style="text-align: center;"> </h2>