#Python 3.7 version - HackerRank solution for "Find the Runner-Up Score!"

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    nmax = max(arr)
    numbers = []


    for i in range(0, n):
        if arr[i] < nmax:
            numbers.append(arr[i])
    nrel = max(numbers)

    print(nrel)
