def minOperations(s: str) -> int:
    count = 0
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != '0':
                count += 1
        else:
            if s[i] != '1':
                count += 1
    return min(count, len(s) - count)


def lessOperations(s: str) -> int:
    s_list = list(s)
    count = 0
    for i in range(len(s_list) - 1):
        if s_list[i] == s_list[i + 1]:
            s_list[i + 1] = "0" if s_list[i] == "1" else "1"
            count += 1
    return min(count, len(s) - count)

s = "10011001"
print(minOperations(s))
print(lessOperations(s))
        


