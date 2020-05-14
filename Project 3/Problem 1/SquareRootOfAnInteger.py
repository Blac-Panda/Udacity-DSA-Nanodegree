def sqrt(number):
    """
    Calculate the floored square root of a number
    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        return None
    if (number == 0) or (number == 1):
        return number

    start = 0
    end = number//2

    while start <= end:
        middle = (start + end)//2
        middle_pow = middle * middle

        if middle_pow == number:
            return middle
        elif middle_pow < number:
            start = middle + 1
            result = middle
        else:
            end = middle - 1

    return result

def run_testcases():
    # Normal cases
    print("Pass" if (3 == sqrt(9)) else "Fail")        #Expected to pass, because square root of 9 is 3
    print("Pass" if (4 == sqrt(16)) else "Fail")       #Expected to pass, because square root of 16 is 4
    print("Pass" if (5 == sqrt(27)) else "Fail")       #Expected to pass, because square root of 27 is 5.196, so it should return 5

    # Edge cases
    print("\nPass" if (None == sqrt(-1)) else "Fail")  #Expected to pass, because if number is less than 1, it should return None
    print("Pass" if (10 == sqrt(250)) else "Fail")     #Expected to fail, because 250 should be 50, not 10
    print("Pass" if (0 == sqrt(0)) else "Fail")        #Expected to pass, because if number is 0 or 1, it should return the number
    print("Pass" if (1 == sqrt(1)) else "Fail")        #Expected to pass, because if number is 0 or 1, it should return the number

run_testcases()
