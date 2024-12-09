def SetIthBit(n,i):
    bitMask=n<<i
    print(n|bitMask)



def clearIthBit(n,i):
    bitMask=~(1<<i)
    print(n&bitMask)




def updateIthBit(n,i,newBit):
    if(newBit==0):
        print(clearIthBit(n,i))
    else:
        print(SetIthBit(n,i))

updateIthBit(10,2,1)
