import random

choices = ['Rock', 'Paper', 'Scissors', 'Q']  # choice() 方法返回一个列表，元组或字符串的随机项。Rock:石头;Paper:布;Scissors:剪刀
cpu_score = 0  # 电脑胜利的次数
player_score = 0  # 玩家胜利的次数
while True:
    computer = random.choice(choices)  # 使用random.choices()返回列表里面的随机项
    player = input(
        '请输入你想的选择：Rock(石头)、Scissors(剪刀)、Paper(布)、q(退出)：').capitalize()  # capitalize()将字符串的第一个字母变成大写,其他字母变小写。
    if player in choices:
        if player == computer:
            print('Tie!')  # 平局
        elif player == 'Rock':
            if computer == 'Scissors':
                print('you win!')  # 当玩家出石头而计算机出剪刀时，玩家赢了
                player_score += 1
            else:
                print('you lose!')  # 当玩家出石头而计算机出布时，玩家输了
                cpu_score += 1
        elif player == 'Paper':
            if computer == 'Rock':
                print('you win!')  # 当玩家出布而计算机出石头时，玩家赢了
                player_score += 1
            else:
                print('you lose!')  # 当玩家出布而计算机出剪刀时，玩家输了
                cpu_score += 1
        elif player == 'Scissors':
            if computer == 'Rock':
                print('you lose!')  # 当玩家出剪刀而计算机出石头时，玩家输了
                cpu_score += 1
            else:
                print('you win!')  # 当玩家出剪刀而计算机出布时，玩家赢了
                player_score += 1
        elif player == 'Q':
            print('game over')
            print('{}:cpu vs player:{}'.format(cpu_score, player_score))
            break
    else:
        print('您的输入有误，请重新输入')
