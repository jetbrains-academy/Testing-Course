<h2>Составные сообщения об ошибках </h2>

<p>Отдельно хочется поговорить про качество сообщений об ошибках, которые показываются при падении теста. Почему это важно? Хорошо написанный текст помогает быстро локализовать найденный баг и разобраться в том, что произошло и из-за чего тест упал. Хороший assert сэкономит вам часы вашей работы, особенно когда количество тестов переходит за сотню.</p>

<p>В целом, тут как с любым фидбеком: важно давать его точно и актуально. Если вы проверяете наличие элемента, то обязательно пишите, что это за элемент по смыслу на странице: </p>

<pre><code class="language-python">assert self.is_element_present('create_class_button', timeout=30), "No create class button"</code></pre>

<p><em>Примечание: Функция is_element_present() вспомогательная. Как её реализовать и использовать, мы разберемся чуть позжe.</em></p>

<p>Если элемент встречается на нескольких страницах приложения, не лишним будет указать, где именно произошла ошибка: </p>

<pre><code class="language-python">assert self.is_element_present('new_announcement_button', timeout=30), "No new announcement button on profile page"</code></pre>

<p>Если вы работаете с каким-то текстом (например, проверяете информационное сообщение, текущий url, ссылку, placeholder в input-элементе или любой другой текст), в сообщении об ошибке всегда лучше выводить оба значения: то, которое ожидалось, и то, которое получили по факту. Всё как в хорошем багрепорте: ожидаемый и фактический результат.</p>

<h3>Форматирование строк с помощью конкатенации</h3>

<p>В питоне такое можно провернуть с помощью конкатенации строк, например:</p>

<pre><code class="language-python">actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")</code></pre>

<p>Но из-за обилия кавычек, знаков сложения и вот этого всего этот способ не самый удобный и читается тоже плохо.</p>

<h3>Форматирование строк с помощью str.format</h3>

<p>Гораздо лучше воспользоваться возможностью python для форматирования строк. Дополнительно можно почитать здесь: <a href="https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat" rel="noopener noreferrer nofollow">https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat</a></p>

<p>Если вкратце, то python умеет подставлять пользовательские значения в строки с помощью функции <strong>.format()</strong>. Синтаксис выглядит примерно так:</p>

<pre><code class="language-python">"Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")</code></pre>

<p>Попробуйте запустить её в интерпретаторе:</p>

<pre><code class="language-python">print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))</code></pre>

<p>Такая строка при исполнении кода превратится в: </p>

<pre><code class="language-no-highlight">Let's count together: one, then goes two, and then three</code></pre>

<p>Таким образом мы можем удобно компоновать ожидаемое и фактическое значение в одну строку.</p>

<h3>Форматирование строк с помощью f-strings</h3>

<p>И наконец наиболее современный способ форматирования строк, который появился в Python3.6, носит название f-strings. Он позволяет исполнять выражения на Python прямо внутри строк, обладает еще большей лаконичностью и удобством использования. Для использования возможностей f-strings нужно указывать символ f перед строкой в таком формате: f"ваша строка {my_var}". В фигурных скобках указывается имя переменной, значение которой надо подставить в строку, или выражение, результат исполнения которого также требуется подставить в вашу строку.</p>

<p>Подробнее про f-strings можно почитать здесь: <a href="https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36" rel="noopener noreferrer nofollow">https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36</a>. Так как мы предполагаем, что вы используете последнюю версию Python, то предлагаем вам применять именно этот подход в данном курсе.</p>

<p>Пример 1:</p>

<pre><code class="language-python">str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")</code></pre>

<p>Итог выполнения выражений в интерпретаторе:</p>

<pre><code class="language-no-highlight">Let's count together: one, then goes two, and then three</code></pre>

<p>Пример 2:</p>

<pre><code class="language-python">actual_result = "abrakadabra"
f"Wrong text, got {actual_result}, something wrong"
</code></pre>

<p>Итог выполнения выражений в интерпретаторе:</p>

<pre><code class="language-no-highlight">Wrong text, got abrakadabra, something wrong</code></pre>

<p>Пример 3:</p>

<pre><code class="language-no-highlight">&gt;&gt;&gt; f"{2+3}"
'5'</code></pre>

<p> </p>

<p>Еще один важный момент: когда вы работаете с текстом элементов на странице или любым другим контентом, который может измениться, всегда записывайте его в отдельную переменную для сравнения. </p>

<p><span style="color: #ff4363;"><strong>неправильно: </strong></span></p>

<pre><code class="language-python">assert self.catalog_link.text  == "Каталог", \
    f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'" </code></pre>

<p>Дважды считывать атрибут — это плохая практика, потому что при повторном считывании текст на странице может измениться, и вы получите неактуальный текст об ошибке. Результат выполнения такого теста сложно анализировать: </p>

<pre><code class="language-python">"Wrong language, got 'Каталог' instead of 'Каталог'"</code></pre>

<p><span style="color: #66cc66;"><strong>правильно: </strong></span></p>

<pre><code class="language-python">catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"  </code></pre>