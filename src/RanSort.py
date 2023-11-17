import random

print("RanSort v1.0 By WYC\n")

with open('data/list.txt', encoding='utf8') as f:
    list = f.read().splitlines()

if len(list) == 0:
    print("错误: data\list.txt 不得为空")
    input()

else:
    while 1:
        random.shuffle(list)
        i=0
        while i < len(list) - 1:
            print(list[i], end=", ")
            i=i+1
        print(list[i], end="\n")

        print("按 Enter 键重新排序")
        input()