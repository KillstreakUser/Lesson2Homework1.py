num = input("Enter Number ")

digits = len(num)
total = 0

for digit in num:
    total += int(digit) ** digits

if total == int(num):
    print(num, "Is an Armstrong Number!")
else:
    print(num, "Isn't an Armstrong Number :<")