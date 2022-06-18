def percentage_error(actual , expected) :
    actual_value = int(input())
    expected_value = int(input())
    first = (actual_value - expected_value) /expected_value
    value = first * 100
percentage_error ("actual" , "expected")