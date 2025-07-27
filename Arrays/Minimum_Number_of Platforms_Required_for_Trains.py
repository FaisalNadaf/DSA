# Input: arr[] = [900, 940, 950, 1100, 1500, 1800], dep[] = [910, 1200, 1120, 1130, 1900, 2000]
# Output: 3 
# Explanation: There are three trains during the time 9:40 to 12:00. So we need a minimum of 3 platforms.

# Input: arr[] = [1,  5], dep[] = [3, 7] 
# Output: 1 
# Explanation:  All train times are mutually exclusive. So we need only one platform

# 1≤ number of trains ≤ 50000
# 0000 ≤ arr[i] ≤ dep[i] ≤ 2359


# Output: 3 
# arr = [900, 900, 900]
# dep = [1000, 1000, 1000]


# Output: 1
# arr = [1,  5]
# dep =  [3, 7]


# Output: 1
# arr = [100, 200, 300]
# dep = [150, 250, 350]


# Output: 4
# arr = [900, 940, 950, 1100, 1500, 1800, 1900]
# dep = [910, 1200, 1120, 1130, 1900, 2000, 2000]


# Output: 3 
arr = [900, 940, 950, 1100, 1500, 1800]
dep =[910, 1200, 1120, 1130, 1900, 2000]

arr.append(0)

a=0

for i in range(0,(len(dep))):
    if(dep[i]<arr[i+1] and a!=0):
        a-=1
    elif(dep[i]>arr[i+1]):
        a+=1



print(a)