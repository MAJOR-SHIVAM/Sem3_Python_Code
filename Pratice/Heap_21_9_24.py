# # importing "heapq" to implement heap queue
# import heapq
# h = []
# heapq.heappush(h, 5)
# print(h)
# heapq.heappush(h, 7)
# print(h)
# heapq.heappush(h, 1)
# print(h)
# heapq.heappush(h, 3)
# print(h)
# heapq.heappush(h, 4)
# print(h)
# heapq.heappush(h, 0)
# print(h)

# heapq.heappop(h)
# heapq.heappop(h)
# print(h)






# # importing "heapq" to implement heap queue
# import heapq
# # initializing list
# li = [5, 7, 9, 1, 3]
# # using heapify to convert list into heap
# heapq.heapify(li)
# # printing created heap
# print ("The created heap is : ",(list(li)))





# # importing "heapq" to implement heap queue
# import heapq
# # initializing list 1
# li1 = [5, 1, 9, 4, 3]
# # initializing list 2
# li2 = [5, 7, 9, 4, 3]
# # using heapify() to convert list into heap
# heapq.heapify(li1)
# heapq.heapify(li2)
# # using heappushpop() to push and pop items simultaneously
# # pops 1
# print("The popped item using heappushpop() is : ", end="")
# print(heapq.heappushpop(li1, 2))
# print(li1)
# # using heapreplace() to pop and push items simultaneously
# # pops 3
# print("The popped item using heapreplace() is : ", end="")
# print(heapq.heapreplace(li2, 2))






# # Python code to demonstrate working of
# # nlargest() and nsmallest()
# # importing "heapq" to implement heap queue
# import heapq
# # initializing list
# li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
# # using heapify() to convert list into heap
# heapq.heapify(li1)
# # using nlargest to print 3 largest numbers
# # prints 10, 9 and 8
# print("The 3 largest numbers in list are : ", end="")
# print(heapq.nlargest(3, li1))
# # using nsmallest to print 3 smallest numbers
# # prints 1, 3 and 4
# print("The 3 smallest numbers in list are : ", end="")
# print(heapq.nsmallest(3, li1))







# def nextSquare():
# # """
# # An infinite generator function that prints
# # next square number. It starts with 1.
# # """
# i = 1
# # An Infinite loop to generate squares
# while True:
#     yield i*i
#     i += 1 # Next execution resumes from this point
# # Driver code to test above generator function
# for num in nextSquare():
#     if num > 100:
#         break
#     print(num)