list_a, list_b, list_c = [], [], []
list = [list_a, list_b, list_c]
column = "|"  #기둥


while True:     
    try:    #오류가 없을 경우
        n = int(input("원판의 개수는?   "))     #원판의 개수를 받는다
        break

    except:    #오류가 났을 경우 실행
        print("숫자만")     

for i in range(1, n + 1):   
    list_a.insert(0, i)     #list_a에 원판 넣기

while True:
    print()

    #공백 생성
    for i in list:
        for j in range(n - len(i)):
            i.append(column)

    #출력
    for i in range(n - 1, -1, -1):
        for j in range(len(list)):
            print(str(list[j][i]).center(4, " "), end=" ")
        print()

    #공백 제거
    for i in range(len(list)):
        for j in range(len(list[i])):
            if column in list[i]:
                list[i].pop()

    #승리 조건
    if len(list[len(list) - 1]) == n:
            print()
            print("승리")
            exit()
    print()

    #어디에서
    while True:
        try:
            x = int(input()) - 1
            if x > 3:
                print("1~3")
                continue
            break
        
        except:
            print("1~3")

    #서렌
    if x == 76:
        print("GG")
        exit()

    #어디로
    while True:
        try:
            y = int(input()) - 1
            if y > 3:
                print("1~3")
                continue
            break

        except:
            print("1~3")

    #이동 불가능한 조건
    if x > len(list) - 1 or y > len(list) - 1 or x < 0 or y < 0 or len(list[x]) == 0:
        print("b")
        continue

    #이동 가능한 조건
    if len(list[y]) == 0 or list[x][len(list[x]) - 1] < list[y][len(list[y]) - 1]:
        list[y].append(list[x].pop())

    else:
        print("다시 입력해주세요")

    print("---------------------------------------------")