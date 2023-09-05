# for i in range(1,5):                            ****
#     for j in range(1,5):                        ****
#         print("*", end='')                      ****
#     print()                                     ****

#*************************************

# for i in range(1, 5):                           *
#     for j in range(1, 5):                       **
#         if(j<=i):                               ***
#             print("*", end='')                  ****
#         else:
#             print(" ", end='')
#     print()

#*************************************

# for i in range(1,5):                               *
#     for j in range(1,5):                          **
#         if(j>=5-i):                              ***
#             print("*", end='')                  ****
#         else:
#             print(" ", end='')
#     print()

#************************************

# for i in range(1,5):                            ****
#     for j in range(1,5):                        ***
#         if(j<=5-i):                             **
#             print("*", end='')                  *
#         else:
#             print(" ", end='')
#     print()

#************************************

# for i in range(1,5):                             ****
#     for j in range(1,5):                          ***
#         if(j>=i):                                  **
#             print("*", end='')                      *
#         else:
#             print(" ", end='')
#     print()

#************************************

# for i in range(1,5):                                *
#     for j in range(1, 8):                          ***
#         if(j>=(5-i) and j<=(i+3)):                *****
#             print("*", end='')                   *******
#         else:
#             print(" ", end='')
#     print()        

#*************************************

# for i in range(1, 5):                            *******
#     for j in range(1, 8):                         *****
#         if(j>=i and j<=(8-i)):                     ***
#             print("*", end='')                      *
#         else:
#             print(" ", end='')
#     print()

#*************************************

# for i in range(1, 5):                            *******
#     for j in range(1, 8):                        *** ***
#         if(j<=(5-i) or j >= (3+i)):              **   **
#             print("*", end='')                   *     *
#         else:
#             print(" ", end='')
#     print()

#*************************************

for i in range(1, 5):
    for j in range(1, 7):
        if((i==1) or (i==4) or (j==1) or (j==6)):
            print("*", end='')
        else:
            print(" ", end='')
    print()

# ******
# *    *
# *    *
# ******
