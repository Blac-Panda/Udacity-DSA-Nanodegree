def rotated_array_search(input_list, number):
    if len(input_list) == 0:
        print("List is empty")
        return
    index = 0
    while input_list[index] < input_list[index + 1]:
        index += 1
        if index + 1 == len(input_list):
            index = len(input_list) // 2
            break
    index += 1
    
    if number in input_list[:index]:
        middle = len(input_list[:index]) // 2
    else:
        middle = index + (len(input_list[index:]) // 2)
        
    while input_list[middle] != number:
        if middle == index:
            return -1
        if input_list[middle] < number:
            middle += 1
        else:
            middle -= 1
        if middle < 0 or middle >= len(input_list):
            return -1
    return middle

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


#Test case
def run_testcases():
    print("Position")
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6 ))
    print(rotated_array_search([6, 7,8, 9, 10, 1, 2, 3, 4], 1))
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1))
    print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))

    print("\nPass/fail")
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[], 10])
    test_function([[6, 7, 8, 1, 2, 3, 4], -1])

run_testcases()
