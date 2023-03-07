# 사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다.
# 또 "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력 받는다.
# 이로부터 최종 시간이 몇 시인지 출력하는 프로그램을 작성하라.


time = int(input("시간을  입력하세요: "))
apm = int(input("오전 (1),오후 (2)를 입력하시오: "))

overtime = int(input("몇 시간이 경과되었나요?: "))

new_time = time + (overtime % 24) 


if new_time > 12:
    if apm == 1:
        apm = "pm"
    else:
        apm = "am"
    print("New hour: %d %s "%(new_time % 12, apm))
else:
    if apm == 1:
        apm = "am"
    else:
        apm = "pm"
    print("New hour: %d %s "%(new_time, apm))  








