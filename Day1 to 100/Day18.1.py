
import math
f1_nume,f1_deno = map(int,list(input("Enter the numerator for 1st fraction : ").split(" ")))
f2_nume,f2_deno= map(int,list(input("Enter the numerator for 2nd fraction : ").split(" ")))
#check if denominators are same
if(f1_deno == f2_deno):
#add numerator
    Fraction1 = f1_nume + f2_nume
    print("Addition of two fractions are :",Fraction1 ,"/",(f1_deno))
#if denominators are not same
else:
    Fraction2 = (f1_nume * f2_deno) + (f2_nume * f1_deno)
    Fraction3=(f1_deno * f2_deno)
    print("Addition of fractions are :",(Fraction2),"/", Fraction3)
    print(math.gcd(Fraction2,Fraction3))