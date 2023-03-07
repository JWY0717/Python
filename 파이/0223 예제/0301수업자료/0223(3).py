# 산술연산자 사용 예제
a = 10
b = 3
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
print(c)  # 13 출력
print(d)  # 7 출력
print(e)  # 30 출력
print(f)  # 3.3333333333333335 출력
print(g)  # 1 출력
print("_"*40) #꿀팁!!!!

# 멤버쉽 연산자 사용 예제 !!포함되어 있는지 여부를 확인!!
a = [1, 2, 3, 4, 5]
b = "Hello, World!"
print(3 in a)  # True 출력
print(6 in a)  # False 출력
print(4 in a)
print("a" in b)
print("a" not in b)
print("o" in b)  # True 출력
print("k" not in b)  # True 출력

print("_"*40) #꿀팁!!!!


# 산술식 및 비교식 응용 예제
x = 10
y = 5
a = x + y
b = x - y
c = x * y
d = x / y


#산술식과 비교식을 이용한 활용법
if a > c and b < d:  # a가 c보다 크고, b가 d보다 작은 경우
    print("a > c and b < d")  # 출력 안 됨
elif a < c or b > d:  # a가 c보다 작거나, b가 d보다 큰 경우
    print("a < c or b > d")  # "a < c or b > d" 출력
else:
    print("neither")  # 출력 안 됨
    
print("_"*40) #꿀팁!!!!

# 문자열 출력 예제
print("Hello, world!")  # "Hello, world!" 출력
print("My name is John.")  # "My name is John." 출력
print('The "quick brown" fox jumps over the lazy dog.')  # 'The "quick brown" fox jumps over the lazy dog.' 출력
print("I'm a boy.")  # "I'm a boy." 출력
print("He said, \"Hello!\"")  # "He said, "Hello!"" 출력
print("10"+"20") #문자열 잇기  1020
print("abc " * 3) #문자열 3번 출력  abc abc abc

# 변수 출력 예제
x = 10
y = 5
z = x + y
print(x, y, z)  # 10 5 15 출력

print(10+20)  # 30




