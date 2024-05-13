import random,sys,os
game = [[0 for i in range(4)]for i in range(4)]
vgame = [[0 for i in range(4)]for i in range(4)]
o = [[0 for i in range(4)]for i in range(4)]

def random_number():
    random_running = True

    while random_running:
        global x, y

        x, y = [random.choice(range(4))for i in range(2)]

        if game[y][x] == 0:
            random_running = False

    game[y][x] = 2

def view():
    os.system('cls')
    for i in range(4):
        for j in range(4):
            if game[i][j] == 0:
                vgame[i][j] = ""
            else:
                vgame[i][j] = game[i][j]

    print("\n "+("-"*9+" ")*4)
    for i in range(4):
        for j in range(4):
            print("|"+'\033[32m' + f'{str(vgame[i][j]).center(9," ")}' + '\033[0m',end="")
        print("|\n " + ("-" * 9 + " ") * 4)

def direction_choice(way):
    for i in range(4):
        for j in range(4):
            o[i][j] = game[i][j]

    if way == "W":
        for i in range(4):
            for j in range(1, 4):
               
                if game[j][i] != 0:
                    y = j

                    while y > 0 and game[y - 1][i] == 0:
                        game[y - 1][i] = game[y][i]
                        game[y][i] = 0
                        y -= 1

                    if y > 0 and game[y - 1][i] == game[y][i]:
                        game[y - 1][i] += game[y][i]
                        game[y][i] = 0
        return False


    elif way == "A":
        for j in range(4):
            for i in range(1, 4):
                
                if game[j][i] != 0:
                    x = i
                    
                    while x > 0 and game[j][x - 1] == 0:
                        game[j][x - 1] = game[j][x]
                        game[j][x] = 0
                        x -= 1
                    
                    if x > 0 and game[j][x] == game[j][x - 1]:
                        game[j][x - 1] += game[j][x]
                        game[j][x] = 0
        return False
    
    elif way == "S":
        for i in range(4):
            for j in range(2, -1, -1):
                if game[j][i] != 0:
                    y = j

                    while y < 3 and game[y + 1][i] == 0:
                        game[y + 1][i] = game[y][i]
                        game[y][i] = 0
                        y += 1

                    if y < 3 and game[y + 1][i] == game[y][i]:
                        game[y + 1][i] += game[y][i]
                        game[y][i] = 0

        return False
    
    elif way == "D":
        for j in range(4):
            for i in range(2, -1, -1):
                if game[j][i] != 0:
                    x = i

                    while x < 3 and game[j][x + 1] == 0:
                        game[j][x + 1] = game[j][x]
                        game[j][x] = 0
                        x += 1

                    if x < 3 and game[j][x + 1] == game[j][x]:
                        game[j][x + 1] += game[j][x]
                        game[j][x] = 0
        return False
    
    elif way == "GG":
        print("포기")
        sys.exit()
        
    else:
        return True

def check():
    for i in game:
        if 2048 in i:
            print("승리")
            sys.exit()
    
    for i in game:
        for j in i:
            if 0 != j:
                for q in range(4):
                    for p in range(3):
                       if (game[q][p] == game[q][p + 1]):
                            return False
                       
                for q in range(4):
                    for p in range(3):
                        if (game[p][q] == game[p + 1][q]):
                            return False 
    return True          

random_number()
random_number()

while True:
    view()

    a = input("'W, A, S, D' 로 이동! (포기는 'GG')").upper().strip()    

    if direction_choice(a):
        continue

    if o != game:
        random_number()

    if check():
        print("패배")
        sys.exit()