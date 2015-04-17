def BitchAssTriangle (rowNum):
   #first we write a breakout sequence.  Like a fuckin boss.
   if rowNum == 1:
      return [1]
      #see, this will break us out, and at the same time put a pretty 
      #top on our triangle.  Cause that's how we roll.
   else:
      #since every line starts (and ends) with 1, we can make that a default value.
      currentLine = [1]
      #now we need a function that will compare the previous line.
      #we're gonna go inception, and use rowNum-1, since the line above is shorter
      previousLine = BitchAssTriangle(rowNum-1)
      #we want to iterate through the previous line, 
      #but leave the last number, since it's always 1.
      for i in range(len(previousLine)-1):
         #now since previousLine is technically an array, we can call the values
         #that we need to perform artihmatic on.  We will append those values
         #to our currentLine.
         currentLine.append(int(previousLine[i] + previousLine[i+1]))
      #then we tack on a nice happy 1 onto the end of this bisnizzy.
      currentLine += [1]
   print previousLine
   return currentLine

print(BitchAssTriangle(4))
