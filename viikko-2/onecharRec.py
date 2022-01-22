def recSum(n):
    if n == 0:
        return 0
    else:
        return recSum(n-1) + n

def count(s):
    sum = 0
    prev = s[0]
    prevcount = 0
    index = 0
    for i in s:
        index += 1
        if( prev == i ):
            prevcount += 1
        else:
            sum += recSum(prevcount)
            prev = i
            prevcount = 1
    sum += recSum(prevcount)
    return sum

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5