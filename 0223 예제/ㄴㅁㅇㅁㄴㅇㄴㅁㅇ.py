# 성적 계산기"를 작성하세요

# 사용자로부터 국어, 영어, 수학 세 과목의 성적을 입력받아, 각 과목의 평균 점수와 총 평균 점수를 계산한 후, 학점을 출력하는 프로그램을 작성하세요.
# 평균 점수는 소수점 둘째자리까지 출력합니다.
# 총 평균 점수는 국어: 40%, 영어: 40%, 수학: 20%로 가중치를 부여하여 계산합니다.
# 총 평균 점수가 90점 이상인 경우 "A", 80점 이상인 경우 "B", 70점 이상인 경우 "C", 60점 이상인 경우 "D", 60점 미만인 경우 "F"를 출력합니다.


k_score = int(input("국어점수를 입력하세요: "))
E_score= int(input("영어점수를 입력하세요: "))
M_score = int(input("수학점수를 입력하세요: "))

avg_k
avg_E
avg_M

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

Total_score = k_score * 0.4 + E_score * 0.4 + M_score * 0.2


print(f"{국어:k_score}, {영어:k_score},{수학:k_score}")
print(f"각 과목의 평균 점수:{Total_score}"}
print(f"총 평균 점수:{grade}"}