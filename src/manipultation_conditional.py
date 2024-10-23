##Question 1: List Manipulation and Conditionals
##You are given a list of integers. Write a function separate_and_sum(nums) that:

##Separates the list into two lists: one containing all the even numbers and the other containing all the odd numbers.
#Sums the values in both lists.
#Returns the larger sum along with the list (even or odd) that had the larger sum.
#If both sums are equal, return the even list and the sum.

def separate_and_sums(lista):
    even_list = [num for num in lista if num % 2 == 0]
    odd_list = [num for num in lista if num % 2 != 0]

    even_sum = sum(even_list)
    odd_sum = sum(odd_list)

    if even_sum >= odd_sum:
        return even_list, even_sum
    else:
        return odd_list, odd_sum

lista = [1,2,3,4,5,6,7,8]
print(f"The Result of the Separate and Sums for a given list is {separate_and_sums(lista)}")