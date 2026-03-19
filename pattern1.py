rows = 7 
 
for i in range(rows): 
     for j in range(rows): 
         if i == j or j == rows - i - 1:
            print("*", end=" ")
         else:
            print("", end=" ") 
     print()
      

# Output:   
# *           *
#   *       *           
#     *   *
#       *
#     *   *
#   *       *
# *           *
# Note: The spaces between the stars may vary based on the environment.
