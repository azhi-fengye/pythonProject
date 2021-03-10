import random

cpu_number = random.randint(0, 50)
for i in range(5, -1, -1):
    if i > 0:
        print('您还有{}次机会哦'.format(i))
        player_input = int(input('猜一猜我心里想的数是啥？\n'))
        if (player_input > cpu_number):
            print('你猜的数字太大了')
        elif player_input < cpu_number:
            print('你猜的数字太小了')
        else:
            print('哎呀，被你猜中了')
            break
    else:
        print('哎呀，没有机会你输了')
