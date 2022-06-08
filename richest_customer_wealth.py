customerAccounts = [[4,3,2], [3,2,10], [3,4,3]]

# First Iteration #
wealth_list = []
for i in customerAccounts:
    wealth_list.append(sum(i))
print(max(wealth_list))

# Second Iteration #
print(max(map(sum, customerAccounts)))


# Leetcode 1
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         wealth_list = []
#         for i in accounts:
#             wealth_list.append(sum(i))
#         return(max(wealth_list))

# Leetcode 2 
# class Solution:
#   def maximumWealth(self, accounts: List[List[int]]) -> int:
#       return(max(map(sum, accounts)

# I learned that Python's map function can apply a function to a given array. This map function sums all the lists in the account array.

# Space complexity: O(1)
# Time complexity: O(M * N) ... m customers iterating over n accounts
