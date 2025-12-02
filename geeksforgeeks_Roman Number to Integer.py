s = "MCMIV" # Output: 1904
Roman_map = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}
total = 0
n = len(s)
i = 1
for i in range(n):
    if i < n-1 and Roman_map[s[i]] < Roman_map[s[i+1]]:
        total -= Roman_map[s[i]]  
    else:
        total += Roman_map[s[i]]


print(total)


