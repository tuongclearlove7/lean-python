nNum = int(input("Enter a number: "))

num2words_less_10 = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}
two_digits = {10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nighteen"}
tens_multiple = {20 : "twenty", 30 : "thirty", 40 : "fourty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety"}
tens_power = ["hundred", "thousand"]

if nNum < 10:
    print(num2words_less_10[nNum])
elif 10 <= nNum < 20:
    print(two_digits[nNum])
elif 20<= nNum < 100:
    if nNum % 10 == 0:
        print(tens_multiple[nNum])
    else:
        print(tens_multiple[nNum // 10 * 10], num2words_less_10[nNum %10])
elif 100 <= nNum < 1000:
    nValue = int(nNum / 100)
    if nValue == 1:
        str100 = "hundred"
    else:
        str100 = "hundreds"
    if nNum % 100 == 0:
        print(num2words_less_10[nNum / 100], str100)
    else:
        nNum_two_digits = nNum - (int(str(nNum[0])) * 100)
        print(nNum_two_digits)