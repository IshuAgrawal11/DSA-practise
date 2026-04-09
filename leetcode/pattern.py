s1 = "adcdba"
s2 = "cabdab"

s1_even = s1[0::2]
s1_odd  = s1[1::2]

s2_even = s2[0::2]
s2_odd  = s2[1::2]

result = sorted(s1_even) == sorted(s2_even) and sorted(s1_odd) == sorted(s2_odd)
print(result)