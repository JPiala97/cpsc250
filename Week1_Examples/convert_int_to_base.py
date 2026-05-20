num = 4095
base = 2

num_original = num
res = ""

while num > 0:
    digit = num % base
    if digit > 9:
        digit = chr(digit-10+ord('A'))
    #print(num, digit)
    res = str(digit)+res
    num = int(num/base)

print(num_original, " in base 10 = ", res, " in base ",base)
