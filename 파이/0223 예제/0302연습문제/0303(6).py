



# 사용자로부터 5개의 정수형 숫자를 입력받아, 입력받은 숫자들 중에서 최댓값과 최솟값을 찾고, 이를 출력하는 프로그램을 작성하세요.
# 입력받은 숫자는 1 이상 100 이하의 자연수입니다.
# 입력받은 숫자 중 중복된 숫자가 있을 수 있습니다.



max=0
min=101


#User_num = int(input("첫 번째 정수:  (1이상 100이하)"))
#User_num = int(input("두 번째 정수:   (1이상 100이하)"))
#User_num = int(input("세 번째 정수:   (1이상 100이하)"))
#User_num = int(input("네 번째 정수:   (1이상 100이하)"))
#User_num = int(input("다섯 번째 정수:  (1이상 100이하)"))


for i in range (1,6):
    num = int(input(f"{i}번째 수를 입력하시요:"))
    if num > max:
        max = num

    if num < min:
        min = num
    
print(f"최댓값 : {max}, 최솟값 : {min}")   