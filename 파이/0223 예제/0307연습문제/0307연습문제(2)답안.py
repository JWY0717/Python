word = input("Your word:")

#문자 'a'가 처음 나오는 위치를 찾음

index_a = word.find('a')

if index_a != -1:
    # 문자 'a'가 존재하면,문자열을 분리하여 출력
    print(word[:index_a+1])
    print(word[index_a+1:])
else:
    # 문자 'a'가 존재하지 않으면,문자열을 그대로 출력
    print(word)
    
print("=====================================================")   



#a가 여러게 나올때

s = "daasdsgscwa"

print(s.replace('a','a\n'))