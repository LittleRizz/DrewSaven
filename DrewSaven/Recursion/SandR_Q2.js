//first we need to figure out how to input a tree

//We will need to scan through the different nodes of the tree to figure out
// which nodes have children.  

//Make sure that a node has no more than 2 kids
//report the degree of the tree. (we could do this a  number of ways--
//for instance, we could keep track of how many levels we go in a separate
//array, and ultimately report back the length of the array.

// Create a tree object for testing purposes
function BinTree(identity) {
  var tree = {},
      tree.identity = identity,
      tree.children = [];
      
      function tree.addChild( self , val ){
        if
        var holder = tree( val );
        tree.children.push(holder);
      }
      
      
}

class Tree(object):
    def __init__(self, value):
        self.children = []
        # More code here
        # Creates a value for holding the value
        self.value = value
    def prettyPrint(self):
		print "Node: {0}".format(self.value)
		if len(self.children):
		    for i in self.children:
		        i.prettyPrint()
		        # pass

    def add_child(self, value):
    	# Creates a new tree 
    	if (self.children.length <2 ) {
    	  
    	holder = Tree(value)
        self.children.append(holder)
        # pass

    def contains(self, target):
    	# Should check the entire tree
    	if self.value == target:
    		return True
        else:
        	for i in self.children:
	        	if i.contains(target):
	        		return True
		return False