

# 사용자로부터 국어, 영어, 수학 세 과목의 성적을 입력받아,
# 각 과목의 평균 점수와 총 평균 점수를 계산한 후, 
# 학점을 출력하는 프로그램을 작성하세요.

# 평균 점수는 소수점 둘째자리까지 출력합니다.
# 총 평균 점수는 국어: 40%, 영어: 40%, 수학: 20%로 가중치를 부여하여 계산합니다.
# 총 평균 점수가 90점 이상인 경우 "A", 80점 이상인 경우 "B", 70점 이상인 경우 "C",
# 60점 이상인 경우 "D", 60점 미만인 경우 "F"를 출력합니다.



K_score = int(input("국어 성적을 입력하시오: "))
E_score = int(input("영어 성적을 입력하시오: "))
M_score = int(input("수학 성적을 입력하시오: "))


Avg_score = (K_score+ E_score+ M_score)  / 3

if Avg_score >=90:
    result='A'
elif Avg_score >=80:
    result='B'
    
elif Avg_score >=70:
    result='C'
elif Avg_score >=60:
    result='D'
else:
    result='f'  
    

print(f"국어:{K_score:.2f},영어:{E_score:.2f},수학:{M_score:.2f}")

print(f"각 과목의 평균 점수는 {K_score:.2f}점,{E_score:.2f}점,{M_score:.2f}점")

print(f"총 평균점수 {Avg_score:.2f}점")

print(f"학점: {result}")