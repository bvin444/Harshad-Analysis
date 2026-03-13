# Harshad Analysis
import matplotlib.pyplot as plt
import math
def get_sum_of_Digits(test): # Function that takes an int and determines sum of digits
    hold = []
    sum = 0
    new = int(test)
    while new != 0:
        x = new % 10
        hold.append(x)
        new = new // 10 
    length = len(hold)
    for i in hold:
        sum = sum + i
    return sum, length
def is_Harshad(sum, int): # Function that determines if a Number is a Harshad
    if int % sum == 0:
        Divisibility_Count = int / sum
        return int, Divisibility_Count
    else:
        return -1, 0
def create_Harshad(INT, DC, l): # Function that creates a Harshad's corresponding Cyclicle Harshad
    SH__ = 0
    for i in range(0, DC):
        SH__ = SH__ + (INT*(10 ** (i * (l))))
    return SH__
Array = [] # array for (DC), SH)
Array_Single = [] # array for log(sH)
new_Array = [] # array for log (DC)
Array_sh = []
Array_DC = []
numbers = list(range(1, 10000))
for i in numbers:
    if i % 10 == 0:
        continue
    else:
        integer = i
        sum_of_Digit, length = get_sum_of_Digits(integer)
        test, Div_Cou = is_Harshad(sum_of_Digit, integer)
        if test != integer:
            continue
        else:
            Super_Harshad = create_Harshad(int(test), int(Div_Cou), length)
            Array.append((int(Div_Cou), math.log(int(Super_Harshad))))
            Array_Single.append(math.log(int(Super_Harshad)))
            new_Array.append(int(Div_Cou))
            continue
# print(new_Array) # Divisibility Count
# print(Array) # Cyclical Harshad
plt.hist(new_Array, bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Divisibility Count from Harshads 1 - 10000")
plt.show()
plt.hist(Array_Single, bins=10, color='skyblue', edgecolor='black')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of log(Super Harshads) from Harshads 1 - 10000")
plt.show()
# plt.plot(Array, color='skyblue')
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.title("Divisibility Count vs. Super Harshad")
# plt.show()
# plt.plot(new_Array)
# plt.show()
# cmd + / for Block - Commenting (Multiple Lines)
# Yay_array = []
# count = 0
# for i in range(1900, 2027):
#     for j in range(1, 13):
#         for k in range(1, 32):
#             if k < 10:
#                 x = int((str(f"{j}0{k}{i}")))
#             else:
#                 x = int((str(f"{j}{k}{i}")))
#             sum = function_Call(x) 
#             if x % sum == 0:
#                 Yay_array.append(x)
#                 count = count + 1
# # print(Yay_array)
# # print(count)