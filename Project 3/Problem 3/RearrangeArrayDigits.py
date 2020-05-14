def rearrange_digits(input_list):

    if input_list is None:
        return None

    if len(input_list) <= 1:
        return input_list
    
    nums = reverse_nums(input_list)
    list1 = list()
    list2 = list()
    
    for num in nums:
        if len(list1)> len(list2):
            list2.append(str(num))
        else:
            list1.append(str(num))
    return [int("".join(list1)), int("".join(list2))]

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
        
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index +=1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged

def reverse_nums(nums):
    if len(nums) <= 1:
        return nums

    index = len(nums) // 2
    left = nums[:index]
    right = nums[index:]

    left = reverse_nums(left)
    right = reverse_nums(right)

    return merge(left, right)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

def run_testcases():
    #Test case
    print(rearrange_digits([10, 3]))          
    print(rearrange_digits([]))              
    print(rearrange_digits(None))            
    print(rearrange_digits([1, 2, 3, 4, 5])) 

run_testcases()
