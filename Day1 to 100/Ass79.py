'''You are given a binary string S of length N. You can perform the following operation on S:
    1)Pick any set of indices such that no two picked indices are adjacent.
    2)Flip the values at the picked indices (i.e. change 0 to 1 and 1 to 0).'''

test_case=int(input("Enter the test Cases:"))
for i in range(test_case):
    n = int(input("Enter the number of 0 and 1: "))
    b = input("Binary:")
    if b.count('1') == 0:
        print(0)
    elif b.count('11') >= 1:
        print(2)
    else:
        print(1)