

Fixture function `answer_file()` should open file by `'filename'` and return file object. 
Fixture must close the file after test passes.

We have this set of tests:
<pre><code>
class TestCookies:
    def test1(self):
        pass
    def test2(self, cookies_together, bake, eagerly_feasting):
        pass
</code> </pre>

Mark existing fixtures in task.py with according scopes and autouse instruction,
so that resulting output in file make sentence `penguins bake cookies, penguins eagerly feasting together`