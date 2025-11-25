arr = [0, 10, 20]
if arr[0] == 0:
	print(-1)
idx = 0
count = []
n = len(arr)
try:
    for i in range(n):
        idx += arr[idx]
        count.append(idx)
        if idx == n-1:
            break

except IndexError:
    pass

print(len(count))









    


   