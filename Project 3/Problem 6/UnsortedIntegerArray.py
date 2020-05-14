def get_min_max(ints):
    min = ints[0]
    max = ints[0]
    for num in ints:
        if num > max:
            max = num
        if num < min:
            min = num
    return (min, max)

import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

def run_testcases():
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
    print ("Pass" if ((0, 5) == get_min_max(l)) else "Fail")       #Expected to fail because 5 isn't the max number expected
    print ("Pass" if ((None, None) == get_min_max(l)) else "Fail") #Expected to fail because min,max is set to none
    print ("Pass" if ((0, -10) == get_min_max(l)) else "Fail")

run_testcases()
