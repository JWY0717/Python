# 사용자로부터 이수한 학점을 입력 받는다. 
# 학점이 40학점 미만이면 "1학년입니다"를 출력하고, 
# 40이상 80미만이면 "2학년입니다"를 출력하고. 
# 학점이 80이상이면 "졸업반입니다"를 출력하는 프로그램을 작성하라.

user_score = int(input("학점을 입려하시오: "))

if user_score >= 80:
    result = "졸업반입니다"
elif 40 <= user_score < 80:
    result = "2학년입니다"
else :
    result = "1학년입니다"
    
print(f"{result}")