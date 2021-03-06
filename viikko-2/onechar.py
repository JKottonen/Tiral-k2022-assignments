def index_sum(row_length):
    sum = 0
    i = row_length
    while( i >= 0):
        sum += i
        i -= 1
    return sum

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
            sum += index_sum(prevcount)
            prev = i
            prevcount = 1
    sum += index_sum(prevcount)
    return sum

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5