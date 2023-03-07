
#크기가 같은 두 개의 리스트 L, M을 생성하고

#두 리스트의 각 요소 합으로 구성되는 새로운 리스트를 생성하라.

# L=[1,2,3]이고 M=[4,5,6]이면 [5,7,9]인 리스트 생성


list1 = [1,2,3]
list2 = [4,5,6]

#list3 = []
#for i in range(0,len(L)):
#   N.append(list1[i] +list2[i])
    
list3 = [list1[i] + list2[i] for i in range(len(list1))]
print(f"{list3}")






