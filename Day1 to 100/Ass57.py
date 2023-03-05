'''Pass or Fail'''
def pass_fail(n, x, p):
    score = x*3 + (n-x)*(-1)
    if score >= p:
        return "PASS"
    else:
        return "FAIL"

T = int(input("Num of test case:"))
for i in range(T):
    n,x,p = map(int,input("Container (num of question,correct_ques,pass_mark): ").split())
    print("The result is:",pass_fail(n,x,p))
