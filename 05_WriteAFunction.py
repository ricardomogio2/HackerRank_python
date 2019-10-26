#Python 3.7 version - HackerRank solution for "Write a Function"

def is_leap(year):  #Writing the function
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False


year = int(input())
print(is_leap(year)) #Calling the function plus a print
