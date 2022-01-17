import re
def find(s):
    regex = ""
    for i in range(0, len(s)):
        regex += s[i]
        print(regex)
        if re.match(f"({regex})", s):
            return i + 1

    return len(s)
            

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("ybabtuaybabtu")) # 7
    print(find("abcabca")) # 7