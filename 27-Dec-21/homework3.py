"""
Zhang San deposited the principal of 4,000 yuan in the bank, 
assuming that the annual interest rate was four thousandths. 
Every year, the principal and interest are added together as a new principal. 
Calculate the principal amount obtained after 10 years.
"""

principal = 4000

print(f"Principal: {principal}")
print("Interest: 0.4%")

for i in range(10):
    principal += principal * 0.004
    print(f"Year {i+1}: {principal} yuan")

print(f"The principal amount obtained after 10 years is {principal} yuan")