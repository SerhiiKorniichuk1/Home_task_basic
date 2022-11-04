'''
Task №1
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.

Examples:

nextBigger(num: 12)    // returns 21
nextBigger(num : 513)  //  returns 531 
nextBigger(num : 2017  //  returns 2071

If the digits can't be rearranged to form a bigger number, return -1

 9  =>  -1
111 =>  -1
531 =>  -1
'''
b = 531

def nextBigger(b):
    if b < 10 or b%10 < (b%100-b%10) // 10:
        print("-1")
    else: 
        k = b - b % 100 + (b % 10 * 10) + (b%100-b%10) // 10
        print(k)

nextBigger(b)