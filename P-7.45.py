# Sparse Array object

class SparseArray(object):

        # define the number of items in the array

        def __init__(self,items=0):

            self.L = [0]*items

        # set item of the array object  with indexing

        # j=> index

        # e=> value

        def __setitem__(self, j, e):

            self.L[j] = e

        # get the item stored at particular index=>j

        def __getitem__(self, j):

            return self.L[j]

        # to string method to support

        # the print and display operations

        def __str__(self):

            return str(self.L)

# declare and intialize the SparseArray

sa=SparseArray(5)

# add tuple to the array signifying

# index and value in the sparse array

sa[0]=(12,"some")

sa[1]=(21,"more")

sa[2]=(51,"values")

sa[3]=(76,"are")

sa[4]=(108,"here")

# print the items in sparse array

print("Sparse Array Content: \n",sa)
