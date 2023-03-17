class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
        def __init__(self):
          self.headval = None
          self.tailval = None
        def insert_at_beginning(self,data):
           nb = Node(data)
           nb.nextval = self.headval
           self.headval=nb

        def listprint(self):
          printval = self.headval
          while printval is not None:
             print (printval.dataval)
             printval = printval.nextval
        def insert_at_end(self,data):
           ne= Node(data)
           temp = self.headval
           while temp.nextval:
               temp= temp.nextval
           temp.nextval = ne






        def insert_position(self,pos,data):
           np = Node(data)
           temp = self.headval
           for i in range(0,pos-1):
               temp = temp.nextval
           np.data= data
           np.nextval = temp.nextval
           temp.nextval = np

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
list.insert_at_beginning(10)
list.insert_at_end(20)
list.insert_position(5,15)
list.insert_at_end(40)
list.listprint()