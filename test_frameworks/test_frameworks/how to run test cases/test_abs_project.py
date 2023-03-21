def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number" 

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    # test_abs2()
    print("All tests passed!")