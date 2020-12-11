import random
import time
import argparse
import sys

def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-inp', default="random")
    return parser

def get_desk_from_file(file):
    f = open(file, 'r')
    desk = []
    while True:
        s = f.readline()
        if not s:
            break
        else:
            desk.append([int(i) for i in s.split()])
    return desk
def get_desk_by_random(M, N):
    desk = []
    for i in range(N):
        desk.append([random.randint(0, 1) for i in range(M)])
    return desk
def generate_desk(desk):
    while True:
        for i in range(N):
            print(*desk[i])
        new_desk = []
        for i in range(N):
            new_desk.append([0]*M)
        for i in range(N):
            for j in range(M):
                alive_neighbors = 0
                #Сосед слева
                if i != 0 and (desk[i-1][j] == 1):
                    alive_neighbors += 1
                #Сосед справа
                if i != N-1 and desk[i+1][j] == 1:
                    alive_neighbors += 1
                #Сосед сверху
                if j != 0 and desk[i][j-1] == 1:
                    alive_neighbors += 1
                #Сосед снизу
                if j != M-1 and desk[i][j+1] == 1:
                    alive_neighbors += 1
                #Сосед слева сверху
                if i != 0 and j != 0 and desk[i-1][j-1] == 1:
                    alive_neighbors += 1
                #Сосед слева снизу
                if i != 0 and j != M-1 and desk[i-1][j+1] == 1:
                    alive_neighbors += 1
                #Сосед справа сверху
                if j != 0 and i != N-1 and desk[i+1][j-1] == 1:
                    alive_neighbors += 1
                #Сосед справа снизу
                if j != M-1 and i != N-1 and desk[i+1][j+1] == 1:
                    alive_neighbors += 1
                if desk[i][j] == 0:
                    if alive_neighbors == 3:
                        new_desk[i][j] = 1
                    else:
                        new_desk[i][j] = 0
                else:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_desk[i][j] = 0
                    else:
                        new_desk[i][j] = 1
        for i in range(N):
            for j in range(M):
                desk[i][j] = new_desk[i][j]
        print()
        print()
        time.sleep(3)

if __name__ == "__main__":
    parser = arguments()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.inp == "file":
        file = input("Enter file name: ")
        desk = get_desk_from_file(file)
        N = len(desk)
        print(N)
        M = len(desk[0])
        print()
        generate_desk(desk)
    elif namespace.inp == "random":
        M, N = map(int, input().split())
        print()
        desk = get_desk_by_random(M, N)
        generate_desk(desk)
    else:
        print("Error in argument inp")