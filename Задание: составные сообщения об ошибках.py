def test_input_text(expected_result, actual_result):
    assert actual_result == expected_result, f"expected {expected_result}, got {actual_result}"
    return f"expected {expected_result}, got {actual_result}"
test_input_text(8,9)