arr=[
    [1 ,2 ,3 ,4 ,5,],
    [6 ,7 ,8 ,9 ,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    ]

sum=0

# O(n^2)
# for i in range(0,len(arr)): 
#     for j in range(0,len(arr[0])):
#         if(i==j):
#             sum+=arr[i][j]
#         elif(i+j==len(arr)-1):
#             sum+=arr[i][j]
    

# O(n)
for i in range(0,len(arr)):
        # primary diagonal
        sum+=arr[i][i]

        # secondr diagona
        # i+j == len(arr)-1 therfore to finde j value j=len(arr)-1-i 
        if(i != len(arr)-i-1):
            sum+=arr[i][len(arr)-i-1]



print(sum)