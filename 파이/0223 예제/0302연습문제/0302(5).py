# 3의 배수와 5의 배수의 합 구하기
# 사용자로부터 양의 정수 n을 입력받아,
# 1부터 n까지의 자연수 중에서 3의 배수와 5의 배수의 합을 구하고,
# 이를 출력하는 프로그램을 작성하세요.
# 사용자로부터 입력받는 정수 n은 1 이상의 양의 정수입니다.
# 결과값은 정수형으로 출력합니다

n = int(input("양의 정수 n을  입력하시오 : "))


sum =0

for i in range (1, n+1):
    if i % 3 == 0 or i % 5 == 0:
        sum = sum + i


#a = (n/ 3) =0 #3의 배수
#b = (n/ 5 ) =0 #5의 배수

# result = a + b
        
        
print(f"1부터 {n}까지의 자연수 중에서 3의 배수와 5의 배수의 합: {sum}")