<h2>PyTest — как пишут тесты</h2>

<p>PyTest не требует написания дополнительных специфических конструкций в тестах, как того требует unittest.</p>

<p>Мы уже увидели, что PyTest может запускать тесты, написанные в unittest-стиле. Перепишем наши тесты из <strong>test_abs_project.py</strong> в более простом формате, который также понимает PyTest. Назовём новый файл test_abs.py:</p>

<pre><code class="language-python">def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

</code></pre>

<p>Запустим тесты в этом файле:</p>

<pre><code class="language-python">pytest test_abs.py</code></pre>

<p>Код тестов стал короче и читабельнее.</p>