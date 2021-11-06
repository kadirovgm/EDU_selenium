# # Example assert messages for test runs
# def test_input_text(expected_result, actual_result):
#     # ваша реализация, напишите assert и сообщение об ошибке
#     assert expected_result == actual_result, \
#         f"expected {expected_result}, got {actual_result}"

# # using "in" or "find"
# s = 'My Name is Julia'
#
# if 'Name' in s:
#     print('Substring found')
#
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')

# # example
# def test_substring(full_string, substring):
#     # ваша реализация, напишите assert и сообщение об ошибке
#     assert substring in full_string, \
#         f"expected '{substring}' to be substring of '{full_string}'"

# # Best practise:
# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# def test_abs2():
#     assert abs(-42) == -42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     test_abs2()
#     print("Everything passed")

