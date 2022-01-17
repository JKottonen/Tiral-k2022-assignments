import re
def find(s):
    match = ""
    is_complete = False
    i = 0
    while not is_complete and i < len(s):
        match += s[i]
        i += 1
        factor = int( len(s) // i )
        if factor * match == s:
            is_complete = True

    return i
            

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7