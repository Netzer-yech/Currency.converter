from coins import USD
# import relevant class

def test_block_1():
    # test_1 enter value to convert
    value_to_convert = float('30.05')
    usd = USD()
    result = usd.calculate(value_to_convert)
    currency_list = [str(result)]

    # test_2 asserting result is valid
    assert result is not None
    assert isinstance(result, float)
    # checking result is float

    # test_3 checking the content of the result file
    with open('C:\\automation course\\results_test.txt', 'w') as f:
        f.write(str(result))
    with open('C:\\automation course\\results_test.txt', 'r') as f:
        content = f.readlines()
        # reading the file content as a list using readlines function
        assert content == currency_list


test_block_1()
# execute the test block


