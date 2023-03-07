#문제2
#초를 입력하면 분과 초로 표시하는 프로그램. 예를 들어, 200초를 입력하면 3분 20초로 표현하라

sec = int(input("초를 입력:"))


min = sec // 60
sec = sec % 60


print(f"{min}분, {sec}초")