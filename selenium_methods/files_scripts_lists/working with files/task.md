<h2>Загрузка файлов</h2>

<p>﻿Если нам понадобится загрузить файл на веб-странице, мы можем использовать уже знакомый нам метод send_keys. Только теперь нам нужно в качестве аргумента передать путь к нужному файлу на диске вместо простого текста.</p>

<p>Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с операционной системой — <strong>os</strong>. В этом случае ваш код не будет зависеть от операционной системы, которую вы используете. Добавление файла будет работать и на Windows, и на Linux, и даже на MaсOS.</p>

<p>Пример кода, который позволяет указать путь к файлу<strong> 'file.txt</strong>', находящемуся в той же папке, что и скрипт, который вы запускаете:</p>

<pre><code class="language-python">import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
element.send_keys(file_path)</code></pre>

<p>Попробуйте добавить в файл отдельно команды <code><samp><strong>print(os.path.abspath(__file__))</strong> </samp></code>и <code><samp><strong>print(os.path.abspath(os.path.dirname(__file__)))</strong></samp></code> и посмотрите на разницу. Подробнее о методах модуля <strong>os</strong> можете почитать самостоятельно в документации: <a href="https://docs.python.org/3/library/os.path.html" rel="noopener noreferrer nofollow">https://docs.python.org/3/library/os.path.html</a>. Обратите внимание, что это будет работать только при запуске кода из файла, в интерпретаторе не сработает.</p>

<p>Если совсем непонятно что происходит, пример: </p>

<p>Допустим, мы написали код скрипта и сохранили код в <em>lesson2_step7.py</em> в своей локальной папке <em>D:\stepik_homework. </em>Активируем виртуальное окружение и запускаем его <strong>python lesson2_step7.py. </strong>В таком случае конструкция <strong>os.path.abspath(os.path.dirname(__file__)) </strong>вернет нам путь до директории файла с кодом, то есть <em>D:\stepik_homework</em><strong>. </strong>В эту же папку кладем файл, который хотим прикрепить, то есть <em>file.txt</em>. Тогда, после выполнения команды:</p>

<p><code>file_path = os.path.join(current_dir, 'file.txt')</code></p>

<p>В переменной <em>file_path</em> будет полный путь к файлу '<strong>D:\stepik_homework\file.txt'</strong>. Фишка в том, что если мы файлы <em>lesson2_step7.py </em>вместе с<em> file.txt </em>перенесем в другую папку, или на компьютер с другой ОС, то такой код без правок заработает и там. </p>

<p> </p>

<p>Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут<strong> type="file"</strong>. Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему метод <strong>send_keys(file_path)</strong>.</p>
