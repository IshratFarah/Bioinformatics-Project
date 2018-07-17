from pylogeny.tree import tree     # import tree class definition


t = tree("(1,((3,2),(4,(11,(10,((7,8),(9,(5,6))))))));") # instantiate with this Newick string
#print t
topo = t.toTopology()       # converts a tree to a rich object of branches and nodes

rearrList = topo.allSPR()   # a list of rearrangement objects
for rearr in rearrList:
  move = rearr.doMove()     # perform the rearrangement and get a topology object
  print move                # prints the Newick string for this topology
  
  #foo(move)                # do something with this topology