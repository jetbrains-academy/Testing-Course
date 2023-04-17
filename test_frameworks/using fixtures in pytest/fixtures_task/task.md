<h2>Task: fixture scope</h2>

<p>We have a set of tests that uses several fixtures. Calculate how many smileys will be printed after executing this test class. </p>

<pre><code>import pytest


@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # some assertions

    def test_second_smiling_faces(self, prepare_faces):
        # some assertions
</code></pre>