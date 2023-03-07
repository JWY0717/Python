# 사용자로부터 현재 시간을 나타내는 1~12의 숫자를 입력 받는다.
# 또 "am" 혹은 "pm"을 입력 받고 경과 시간을 나타내는 값을 입력 받는다.
# 이로부터 최종 시간이 몇 시인지 출력하는 프로그램을 작성하라.



#C_time = int(input("현재 시간을 입력하시오: "))

#am_pm = int(input("오전이면 1, 오후이면 2를 입력하시오: "))


#F_timr = int(input("경과된 시간을 입력하시오: "))

#newhour = C_time+(F_timr%24)


#if am_pm == 1:
#    if newhour <= 12:
#        print("최종시간 : ", newhour, "am")
#    else:
#        print("최종시간 : ", newhour-12, "pm")
#else:
#    if newhour <= 12:
#        print("최종시간 : ", newhour, "pm")
#else:
#        print("최종시간 : ", newhour-12, "am") 





Now_time =int(input("현재 시간을 입력하시오(1~12): "))

am_pm = int(input("am이면 1, pm이면 2를 입력하시오: "))

Next_time = int(input("경과된 시간을 입력하시오: "))

New_hour =Now_time +  Next_time
New_hour2=Now_time+Next_time - 12

if (am_pm == 1):
    if ( Now_time+Next_time > 12):
        print(f"현재 시간:{New_hour2}pm")
    else:
        print(f"현재 시간:{New_hour}am")
else:
    if ( Now_time+Next_time >= 12):
        print(f"현재 시간:{New_hour2}am")
    else:
        print(f"현재 시간:{New_hour}pm")
    
    



