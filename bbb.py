from random import randint

print('请输入最小值')
A = int(input())
print('请输入最大值')
B = int(input())

def play():

    random_int = randint(A, B)

    while True:
        print('猜测数字是多少？('+str(A)+'-'+str(B)+')')
        guess = int(input())

        if guess == random_int:
            print('你猜对了，数字是' + str(random_int) + '恭喜你。')
            break

        if guess < random_int:
            print('你猜小了。')
            continue

        if guess > random_int:
            print('你猜大了。')
            continue

if __name__=='__main__':
    play()