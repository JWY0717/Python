
# for 루프를 이용하여 다음과 같은 리스트를 생성하라.

# 0~49까지의 수로 구성되는 리스트
list1 = [i for i in range(0,50)]
print(list1)

# list1 = []
#for i in range(0,50):
#        list1.append(i)
#print(list1)    


print("=====================================================")

# 1~50까지 수의 제곱으로 구성되는 리스트

list2 = []
for i in range(1, 50):
    
    #append를 사용해서 끝에 계속해서 받기
    list2.append(i*i)
print(list2)


#list2 = [i for i in range(1,51)]
#list3 = [x for i ** i  in range(1,51)]
#print(list2)
#print(list3)

