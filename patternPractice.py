
num = int(input("give me a input"))
for i in range(num):               # * * * * *
    print("* ",end=" ")
print("")

num = int(input("give me a input"))  # * * * * *
for i in range(num):                 # * * * * *
    print("* " * num)                # * * * * *
print("")                            # * * * * *

num = int(input("give me a number"))  # 5 5 5 5 5
for i in range(num):                  # 5 5 5 5 5
    print((str(num)+" ")* num)        # 5 5 5 5 5
print("")                             # 5 5 5 5 5

num = int(input("give me a number"))  # 1 1 1 1 1
for i in range(num):                  # 2 2 2 2 2
    print((str(i+1)+" ") * num)       # 3 3 3 3 3
print("")                             # 4 4 4 4 4

num = int(input("give me a number"))  # A
for i in range(num):                  # B  B
    print((chr(65+i)+" ") *(i+1))     # C  C  C
print("")                             # D  D  D  D
                                      # E  E  E  E  E

num = int(input("give me a number"))  #  *
for i in range(num):                  #  *  *
    print("* " * (i+1))               #  *  *  *
print("")                             #  *  *  *  *
                                      #  *  *  *  *  *

num = int(input("give me a number"))  #  *  *  *  *  *
for i in range(num):                  #  *  *  *  *
    print("* " * (num-i))             #  *  *  *
print("")                             #  *  *
                                      #  *
num = int(input("give me a number"))  #  *  *  *  *  *
for i in range(num):                  #     *  *  *  *
    print("  " * (i) + "* "*(num-i))  #        *  *  *
print("")                             #           *  *
                                      #              *
num = int(input("give me a number"))  #              *
for i in range(num):                  #           *  *
    print("  "*(num-i-1)+ "* "*(i+1)) #        *  *  *
print("")                             #     *  *  *  *
                                      #  *  *  *  *  *
num= int(input("give me a number"))   #        *
for i in range(num):                  #       *  *
    print(" "*(num-i-1)+"* "*(i+1))   #      *  *  *
print("")                             #     *  *  *  *
                                      #    *  *  *  *  *
                                      #   *  *  *  *  *  *

num = int(input("give me a input"))   #   * * * * * * * * * *
for i in range(num):                  #     * * * * * * * *
    print(" " * (i)+ "* "* (num-i))   #       * * * * * *
print("")                             #         * * * *
                                      #           * *
                                      #            *
num = int(input("give me a input"))   #            *
for i in range(num):                  #           * *
    print(" "*(num-i-1)+"* "*(i+1))   #          * * *
for i in range(num):                  #         * * * *
    print(" "*(i+1)+ "* "* (num-i-1)) #          * * *
                                      #           * *
                                      #            *
num = int(input("give me a input"))   #
for i in range(num):
    print("* " *(i+1)+ " "*(num-i+1))
for i in range(num):
    print("* "*(num-i-1)+" "*(i-1))

num = int(input("give me a number"))  #
for i in range(num):                  #
    print("  "*(num-i-1)+ "* "*(i+1)) #
for i in range(num):
    print("  "*(i+1)+"* " * (num-i-1))

num = int(input("give me a number"))
for i in range(num):
    print((" "*i +"* " )+(" "*((2*num)-(2*i)-3)+"* "))


