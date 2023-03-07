#문제1
#사용자로부터 사과의 개수와 가격,
#그리고 부가세율을 입력받아,
#총 가격을 계산하는 프로그램을 작성하세오
#개수 * 가격 + 개수 *가격 *부가세율 / 100 =총 가격!!


price = int(input("가격: "))
count = int(input("개수: "))
tax = float(input("부가세율: "))



totalPrice = price * count + price * count * tax / 100


print(f"가격:{price}개, 개수:{count}개, 부가세율:{tax:.2f}%, 총 가격:{totalPrice:.0f}")


