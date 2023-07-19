from _pytest.fixtures import fixture
import os

# penguins bake cookies, penguins eagerly feasting together

filename = "answer.txt"

@fixture(scope="session", autouse=True)
def file():
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, "x")
    yield f
    f.close()

@fixture(scope="class")
def cookies_together(file):
    file.write("cookies, ")
    yield
    file.write("together ")


@fixture(scope="module")
def bake(file):
    file.write("bake ")


@fixture(scope="function")
def eagerly_feasting(file):
    file.write("eagerly ")
    yield
    file.write("feasting ")


@fixture(scope="function", autouse=True)
def penguins(file):
    file.write("penguins ")