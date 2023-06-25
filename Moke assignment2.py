def firstUniqChar(s):
    count = {}

    # Count frequency
    for c in s:
        count[c] = count.get(c, 0) + 1

    # Find non-repeating character
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i

    return -1

s = "leetcode"
result = firstUniqChar(s)
print(result)
