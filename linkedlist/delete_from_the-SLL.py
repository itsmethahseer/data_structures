class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None
class SLinkedList:
   def __init__(self):
      self.headval = None



   def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
   def delete_from_biggining(self):
       temp = self.headval
       self.headval = temp.nextval
       temp.nextval = None
   def delete_from_end(self):
       prev = self.headval # First value is taken into 'prev'
       temp = self.headval.nextval   # second value is taken into temp
       while temp.nextval is not None:
           temp = temp.nextval
           prev = prev.nextval
       prev.nextval = None



   def delete_using_index(self,pos):
       prev = self.headval
       temp = self.headval.nextval
       for i in range(1,pos-1):
           temp =temp.nextval
           prev = prev.nextval
       prev.nextval = temp.nextval







list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
# list.delete_from_biggining()
# list.delete_from_end()
# list.delete_using_index(1)
list.listprint()


