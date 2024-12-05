
arr=[
    [1 ,2 ,3 ,4 ,5,],
    [6 ,7 ,8 ,9 ,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25],
    ]

startRow=0
endRow=len(arr)-1
startCol=0
endCol=len(arr)-1


while (startRow<=endRow and startCol<=endCol):
    # printing top line in 2d array
    for j in range(startCol,endCol+1):
        print(arr[startRow][j],end=" ")

    # printing right line in 2d array
    for i in range(startRow+1,endRow+1):
        print(arr[i][endCol],end=" ")

    # printing bottom line in 2d array
    for j in range(endRow-1,startCol-1,-1):
        if(startRow==endRow):break
        print(arr[endRow][j],end=" ")

    # printing left line in 2d array
    for i in range(endRow-1,startRow,-1):
        if(startCol==endCol):break
        print(arr[i][startCol],end=" ")
    
    startRow+=1
    endRow-=1
    startCol+=1
    endCol-=1