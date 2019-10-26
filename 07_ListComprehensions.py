#Python 3.7 version - HackerRank solution for "List Comprehensions"

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    vector = []
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                if (i+j+k) != n:
                    vector.append([i,j,k])

    print(lista)
