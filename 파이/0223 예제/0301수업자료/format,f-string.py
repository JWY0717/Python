endline=("="*50)

name = "Tom"
age = 20

#format() 메소드를 이용한 문자열 포매팅
print("My name is {} and I am {} years old.".format(name,age))

print(endline)

#f-string을 이용한 포매팅
print(f"My name is {name} and I am {age} years old.".format(name,age))

print(endline)
a=3
b=2
c=1

print(f"I have {a:d} apples, {b:d}oranges, and {c:d} banana.")

print(endline)

a=1.23
print(f"The result is {a:2f}.")
