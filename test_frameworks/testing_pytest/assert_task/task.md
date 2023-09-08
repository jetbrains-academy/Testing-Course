<h2>Task: PyTest — checking the expected result (assert)</h2>

Using pytest, implement two test cases. 

The first test case `test_valid_input` takes a valid number from 1 to 1000 as input and realizes the following scenario: 

1. Open the link page.
2. Insert a valid number (it will be passed to the function as a parameter).
3. Click the checkbox "I'm a robot".
4. Click the Submit button.

The expected result: 

The correct result of the mathematical function in the pop-up window.

For this check, use pytest assert. 

The second test case `test_invalid_input` takes a number beyond the 1–1000 range as input and realizes the following scenarioп:

1. Open the link page. 
2. Insert a valid number (it will be passed to the function as a parameter).
3. Click the checkbox "I'm a robot".
4. Click the Submit button.

The expected result: 

No pop-up window.

For this check, use the `pytest.raises` construct.
