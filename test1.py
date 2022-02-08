arr=[3,4,4,4,5,6,6,7]
new_arr=[]
n=len(arr)
for i in range(0,n-1):
	for j in range(i+1,n):
		if arr[i]==arr[j]:
			if arr[i] not in new_arr:
				new_arr.append(arr[j])
				
print(new_arr)

