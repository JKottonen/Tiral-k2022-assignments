def count(s):
    sum = 0
    index = 0
    distinct = {}
    for i in s:
        index += 1
        if i not in distinct.keys():
            distinct[i] = 1
            sum += 1
        else:
            distinct[i] += 1
            sum += distinct[i]

    return sum

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abcd")) # 4
    print(count("ababca")) # 10