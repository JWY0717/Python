#판매자가 딸기와 포도를 판매하고 있다.
#포도 한 알의 무게는 75g이고 딸기 한 알의 무게는 113.5g이다.
#사용자로부터 포도 알의 개수와 딸기의 개수를 입력 받아 총 무게를 계산하여 출력하는 프로그램을 작성하고 실행하라


grape_w =75
strawberry_W =113.5

grape_n = int(input("포도 의 총 개수 : "))
strawberry_n = int(input("딸기 의 총 개수 : "))

total_w = (grape_w * grape_n) + (strawberry_W * strawberry_n)

print(f"총 무게: {total_w:.2f} g")