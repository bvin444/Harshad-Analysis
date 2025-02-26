## Harshad Analysis

HarshadTestValue = int(input("Please enter an integer: "))
X = HarshadTestValue
TestArray = []

while HarshadTestValue != 0:
    TestArray.append(HarshadTestValue % 10) 
    HarshadTestValue = HarshadTestValue // 10
print(TestArray)
Sum = 0
for i in TestArray:
    Sum = Sum + i
print(Sum)
if X % Sum == 0:
    print("Congrats you have found a Harshad")
    Continue = True
else:
    print("Sorry, that number is not a Harshad")
    Continue = False

if Continue == True: 
    N = X / Sum
    print(N)
    runningTotal = 0
    for j in range(0, int(N)):
        runningTotal = runningTotal + (10 ** (j*len(TestArray)))*(X)
    print(runningTotal)
else:
    print("Goodbye")




