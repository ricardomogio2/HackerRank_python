#Python 3.7 version - HackerRank solution for "Print Function"

if __name__ == '__main__':
    n = int(input())

    for i in range(1,n+1):
        print(i, end='') #end parameter put a empty character at the end of the print. If dont use this, the nest iteration of print will be on the next line
