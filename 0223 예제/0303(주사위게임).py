    
import random

while True:


    dice_game1 = random.randint(1, 6)
    print(f"첫번째 주사위를 던졌을 때 나오는 수:{dice_game1}")

    dice_game2 = random.randint(1, 6)
    print(f"두번째 주사위를 던졌을 때 나오는 수:{dice_game2}")


    total_dice_sum = dice_game1+ dice_game2
    
    if total_dice_sum == 7:
        print("승리")
        break
    else:
        print("패배")
