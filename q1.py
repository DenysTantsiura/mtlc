def q1(str1: str, str2: str) -> float:
    num1 = str1.split('.')  # ['1', '2']
    num2 = str2.split('.')  # ['102','5007']
    num1 = int(num1[0]) + int(num1[1])/(10**len(num1[1]))
    num2 = int(num2[0]) + int(num2[1])/(10**len(num2[1]))
    return num1 + num2


print(q1('0.0508', '0.0508'))  # 0.1016
print(q1('1.2', '102.5007'))  # 103.7007
