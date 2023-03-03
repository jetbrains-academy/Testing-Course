<h2>Задание: оформляем тесты в стиле unittest </h2>

<p>Попробуйте оформить тесты из первого модуля в стиле unittest.</p>

Take [step](course://introduction/finding_elements_selenium/task10)  from the first 
section and re-write your tests in unittest style.



<ul>
	<li>Создайте в test.py класс с тестами, который должен наследоваться от <strong>unittest.TestCase</strong> по аналогии с предыдущим шагом</li>
	<li>Перепишите в стиле unittest тест для страницы <a href="http://suninjuly.github.io/registration1.html" rel="noopener noreferrer nofollow" target="_blank" title="Link: http://suninjuly.github.io/registration1.html">http://suninjuly.github.io/registration1.html</a></li>
	<li>Перепишите в стиле unittest второй тест для страницы <a href="http://suninjuly.github.io/registration2.html" rel="noopener noreferrer nofollow" target="_blank" title="Link: http://suninjuly.github.io/registration1.html">http://suninjuly.github.io/registration2.html</a></li>
	<li>Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод <a href="https://docs.python.org/3/library/unittest.html#assert-methods" rel="noopener noreferrer nofollow">assertEqual</a></li>
	<li>Запустите получившиеся тесты  </li> 
	<li>Просмотрите отчёт о запуске и найдите последнюю строчку  </li> 
</ul>

Вставьте строчку в [answer.txt](file://test_frameworks/test_frameworks/task_unittest/answer.txt) 

<p>Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!</p>

<p>Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения. </p>

<p>Не удаляйте код после прохождения этого задания, он пригодится в следующем уроке. </p>
