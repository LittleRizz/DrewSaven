# Pascal's triangle
# accepts n, the outpul level, as an integer
# output prints

# Create a function that expands on itself, from 1 to n
def pascalT(n):

  # Create a helper function
  def helper(array, n): 
  iAr = [1]
  
    # Create a base case to break the recursion - n will have to be the limit
    # Will a
  if len(iAR) == n:
    return
  for i in range(len(array)):
    iAr.append(array[i]+array[i+1:i+2])

  	
  # Create a step that uses the prior array to
  # generate the next array and prints it.
  
  #with each loop of the recursion, we're going to want to do two things:
  #create a new array that is one longer, and use the values of the previous array to populate the new array
  
  
  
  # May need to always append 1 first, this would
  # also solve the initial level problem
  
  # Then, increment based on the length of the
  # parameter array.
  
  
  # Need to use ar[i:i+1] notation to handle the 
  # end of the parameter array neatly

  # Need a way to start with printing 1


