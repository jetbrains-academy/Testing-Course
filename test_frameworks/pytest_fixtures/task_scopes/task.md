

The fixture function `answer_file()` should open a file by `'filename'` and return a file object. 
The fixture must close the file after the test passes.

We have the following set of tests:
<pre><code>
class TestCookies:
    def test1(self):
        pass
    def test2(self, cookies_together, bake, eagerly_feasting):
        pass
</code> </pre>

Mark the existing fixtures in task.py with proper scopes and the autouse instruction
so that the resulting output in the file makes the sentence `penguins bake cookies, penguins eagerly feasting together`.
