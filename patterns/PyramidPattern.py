# Take input from the user for the number of rows (this will be a square pattern)
n = int(input("Enter row size: "))


for i in range(1, n + 1):
    # Print spaces to center the stars
    for j in range(0, n - i):
        print(" ", end="")
    # Print stars for the current row
    for j in range(0, 2 * i - 1):
        print("*", end="")
    # Move to the next line after each row
    print()



    """
     output

Enter row size: 22

                     *
                    ***
                   *****
                  *******
                 *********
                ***********
               *************
              ***************
             *****************
            *******************
           *********************
          ***********************
         *************************
        ***************************
       *****************************
      *******************************
     *********************************
    ***********************************
   *************************************
  ***************************************
 *****************************************
*******************************************

    """