#사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를 +로 연결한 문자열을 생성하라.
#예를 들어 2, 5, 11, 33, 55를 입력하면 '2+5+11+33+55'를 생성하라.



#num1 = int(input())
#num2 = int(input())
#num3 = int(input())
#num4 = int(input())
#num5 = int(input())


num_list = input("5개의 숫자를 입력하세요 (구분자:띄어쓰기): ").split()
result = "+".join(num_list)
print(result)