# We usually refer to the entries of a two-dimensional list by their row and column, like below on the left. Another
# way is shown below on the right. Write some code that translates from the left representation to the right one. The
# // and % operators will be useful. Be sure your code works for arrays of any size. Write some code that translates
# from the right representation to the left one.

L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

list_dim_1 = eval(input("enter the first dimension: "))
list_dim_2 = eval(input("enter the second dimension: "))
left_rep = input("enter left hand form: ")[1:][:-1].split(",")

print(f"right hand form is {int(left_rep[0]) * list_dim_1 + int(left_rep[1])}")
