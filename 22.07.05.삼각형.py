num = int(input("라인 넘버를 입력하세요 :"))

for row in range(num):

    for col in range(num):
        if row >= col and col+row <= num - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()