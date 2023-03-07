#분(min)을 입력 하면	 일, 시간, 분으로 출력하는 프로그램을 만들어라.
#(예 : 1550분은 1일 1시간 50분)

min = int(input("분을 입력 : "))


hour =  min // 60
min2 = min % 60
day1 = hour // 24
hour1 = hour % 24

print(f"{day1}일 {hour1}시간 {min2}분")
