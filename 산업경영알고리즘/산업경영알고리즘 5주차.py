number1 = int(input("숫자를 입력하시오:"))
number2 = int(input("숫자를 입력하시오:"))
                    
def recursion(number1):
    if number1 == number2:
        return number1
    return number1+recursion(number1-1)

result = recursion(number1)
print(result)
