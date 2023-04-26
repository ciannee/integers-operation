# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
#  Assignment 4: Programming Exercise 4 (Square and Cube of Integers)


# read integers text file
with open("integers.txt") as my_file:
    # for each line
    for i in my_file:
        # parse integers
        if i.strip:
            num = int(i)
            # extract even integers
            if (num % 2 == 0):
                # append double text file
                even = open("double.txt", "a")
                # square all even integers
                even.write(str(num**2))
                even.write("\n")
            # extract odd integers
            else:
                # append triple text file
                odd = open("triple.txt", "a")
                # cube all odd integers