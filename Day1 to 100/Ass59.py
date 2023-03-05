"""Body mass Index"""

n=int(input("Enter the test case:"))
for i in range(n):
    M,H = map(int,input("Enter the values of M and H:").split(" "))
    BMI = M//pow(H,2)
    if BMI <=18:
        print("1")
    elif 19<=BMI<=24:
        print("2")
    elif 25<=BMI<=29:
        print("3")
    elif BMI >=30:
        print("4")
    