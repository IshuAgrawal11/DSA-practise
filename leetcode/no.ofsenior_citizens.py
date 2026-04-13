details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
count = 0
for detail in details:
    if detail[11:13] > "60":
        count += 1
    else:
        continue
print(count)

def countSeniors(details: list[str]) -> int:
    return(sum(detail[11:13] > "60" for detail in details))

details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(countSeniors(details))