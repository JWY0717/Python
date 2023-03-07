# 변수 사용 예제
x = 10  # 변수 x에 정수 10을 저장
y = 20  # 변수 y에 정수 20을 저장
z = x + y  # 변수 z에 x와 y의 합을 저장
print(z)  # 변수 z의 값을 출력


# 10진수
x = 42
print(x)    # 출력: 42

# 2진수
y = 0b101010
print(y)    # 출력: 42

# 8진수
z = 0o52
print(z)    # 출력: 42

# 16진수
w = 0x2a
print(w)    # 출력: 42

a = 3.5e2   # 3.5 x 10의 2승
print(a)



# 복소수 생성
z1 = 2 + 3j
z2 = complex(4, -2)

# 복소수 연산
z3 = z1 + z2
z4 = z1 * z2
z5 = z1 / z2
z6 = z1 ** 2

# 결과 출력
print(z3)   # (6+1j)
print(z4)   # (14+8j)
print(z5)   # (-0.4+0.7j)
print(z6)   # (-5+12j)

# 복소수형 데이터를 다룰 때,
# 실수부와 허수부를 각각 얻는 방법은 아래와 같습니다.

z = 3 + 4j
print(z.real)  # 출력: 3.0
print(z.imag)  # 출력: 4.0

string = "Hello, World!"
print(string[0]) # "H" 출력
print(string[7]) # "W" 출력

# 문자열 메소드를 통해 문자열의 형식을 검색
position = string.find("World")
print(position)

# 다음과 같이 정수형과 문자열을 더하려고 할 때 타입 에러가 발생합니다
# num = 10
# text = "apple"
# print(num + text)

#변수 num은 정수형(int)이고, 변수 text는 문자열(str)이므로 덧셈 연산을 할 수 없습니다.
#따라서 num을 문자열로 변환해야 합니다.
num = 10
text = "apple"
print(str(num) + text)


#리스트(List)
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits[1])
fruits[1] = "orange"
fruits[2] = "안녕"
print(fruits)

#튜플 !!!!요소의 추가, 수정, 삭제 등이 불가능합니다!!!!
fruits = ("apple", "banana", "cherry")
print(fruits)
print(fruits[1])

# 딕셔너리(Dictionary) 중괄호({})를 사용하여 만들며
# key와 value로 이루어진 쌍(pair)들을 저장합니다.
fruits = {"apple": 3, "banana": 2, "cherry": 5}
print(fruits)
print(fruits["banana"])
fruits["orange"] = 4
print(fruits)




