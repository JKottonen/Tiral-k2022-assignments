def count(s):
    sum = 0
    length = len(s)
    strings = []

    substring = s[0]                    # First character of s
    for i in range(1, length):          # Iterate rest of s
        if s[i] != s[i-1]:              # If current char is not same as the previous one:
            strings.append(substring)   # Add current substring to a list
            substring = s[i]            # Substring is initalized for the new char
        
        else:                           # If current char is same as the previous one:
            strings.append(substring)   # Add current substring to the list
            substring += s[i]           # Current character is added to current substring

    strings.append(substring)           # After iterating, add the last substring to the list

    for substring in strings:           # sum the lengths of all the possible substrings
        sum += len(substring)

    return sum

if __name__ == "__main__":
    print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    print(count("abcde")) # 5