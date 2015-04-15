def say_hello(name):
	"""Greet with parameter name"""
	return 'Hello there, {:s}'.format(name)

# The count-up branch will implements a function that will count up to a particular value
def countup(numb):
	count = 1
	while count <= numb:
		print(count)
		count +=1
		
# The branch pick-random branch will implement a function that will return a random element from a list
def pickrandom(lst):
  # Importing the random library
  import random
  
  # Calculating the len(lst)
  ll = len(lst)

<<<<<<< HEAD
  # Returning a random element of the lst
  return lst[random.randrange(0,ll)]
  
# The branch reverse-name will implement a function that returns the reverse order of the name parameter
=======
# The branch reverse-name will implement a function that returns the reverse order of the name parameter
  def reversename(name):
  // Create an empty string
  rname = ""

  # Calculate the length of the name
  nl = len(name)

  # Iterate through the name adding each letter to the front of the empty string
  for i in name:
    rname = i +rname
  return rname
>>>>>>> Added reverse_name fxn
