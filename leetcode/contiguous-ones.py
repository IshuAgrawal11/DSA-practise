s = "11001"
count = 0
num = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1] == "1":
        count += 1

for i in range(len(s)):
    if s[i] == "1":
        num += 1
print(True if num == count == 1 else False)

       