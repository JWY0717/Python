# 사용자로부터 cm 단위의 길이를 입력 받는다. 
# 입력 값이 음수이면 "잘못 입력하였습니다"라는 메시지를 출력하고 
# 양수이면 길이를 인치로 변환하여 출력하는 프로그램을 작성하라. 
# 1인치 = 2.54cm


cm_length = float(input("길이를 입력하시오(cm): "))


inch = cm_length / (254/100)


if cm_length < 0:
    print("잘못 입력하였습니다")
else :
    print(f"{inch}")