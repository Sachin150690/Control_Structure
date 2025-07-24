n1=int(input("Enter the lower limit"))
n2=int(input("Enter the upper limit"))
summation=0
for i in range(n1,n2):
    summation=summation+i
print(f"The sum of number from {n1} to {n2-1} is:",summation)
