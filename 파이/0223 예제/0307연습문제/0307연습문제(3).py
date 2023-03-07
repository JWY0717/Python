#문제 1번 :3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램하시오

string_list = ["장우영","장유정","장동익","하계연"]

#1.insert()로 맨 앞에 새로운 친구 추가

string_list.insert(0,"홍길동")
print(string_list) 


#2.insert()로 3번째 위치에 새로운 친구 추가

string_list.insert(3,"아무개")
print(string_list)

#3.append()로 마지막에 친구 추가

string_list.append("철수")
print(string_list)


#문제 2번:리스트 [1, 2, 3]에 대해 다음과 같은 처리를 하라.


#my_list = [1,2,3]

#두 번째 요소를 17로 수정
my_list = [1, 2, 3]
my_list[1] = 17
print(my_list) 


#리스트에 4, 5, 6을 추가
my_list = [1, 2, 3]
my_list.append(4)
my_list.append(5)
my_list.append(6)
print(my_list) 


#첫 번째 요소 제거

my_list = [1, 2, 3, 4, 5, 6]
del my_list[0]
print(my_list) # 출력 결과: [1, 2, 4]

#리스트를 요소 순서대로 배열하기

my_list = [1, 6, 3, 5, 4, 2]
sorted_my_list = sorted(my_list)
print(sorted_my_list)

#인덱스 3에 25넣기

my_list = [1, 2, 3, 4, 5, 6]
my_list.insert(3, 25)
print(my_list)
