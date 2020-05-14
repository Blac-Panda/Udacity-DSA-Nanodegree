class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
  def __repr__(self):
    return f"Node(data: {self.data})"


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  def append(self, data):
    
    node = Node(data)
    if(self.head == None):
      self.head = node
      self.tail = self.head
    else:
      self.tail.next = node
      self.tail = node

    self.size +=1

  def getSize(self):
    return self.size

  """
  Create an object generator to return a node when a loop is used
  The loop starts at head of the linkedlist
  """
  def __iter__(self):
    if self.size == 0:
      return

    node = self.head

    while node:
      yield node
      node = node.next

  """
  print the entire list
  """
  def getList(self):
    elem = []
    for n in self:
      elem.append(n.data)
    return elem

  def __repr__(self):
      output = ''
      for n in self:
          output += str(n) + "\n"
      return output

  def __str__(self):
      output = ''
      for n in self:
          output += str(n) + "\n"
      return output

def intersection(list1,list2):
  mapData = {}
  LLIntersect = LinkedList()

  """
  Check whether list1 or list 2 are empty
  """
  if list1 and list2 :

    first, second = (list1, list2) if list1.getSize() < list2.getSize() else (list2, list1)

    """
    map all the data in first list to map, returns false if the data hasn't been found
    """
    for node in first:
      mapData[node.data] = False

    for node in second:
      data = node.data
      isDuplicate = mapData.get(node.data)
      if isDuplicate != None and not isDuplicate:

        """
        Traverse the second list, check if data is in the map
        If data exists in the map, mark it as a duplicate, by changing its value to True, so that it is not added to the list again
        """

        LLIntersect.append(data)
        mapData[data] = True

    return LLIntersect

"""
A function to add data to the new LinkedList while keeping track of duplicates
"""
def appendListStripDuplicates(LinkedList,mapData,LinkListUnion):
  if LinkedList : 
    for node in LinkedList:
      data = node.data
      duplicate = mapData.get(node.data, False)
      if not duplicate:
        LinkListUnion.append(data)
        mapData[data] = True
  return (mapData,LinkListUnion)

def union(list1,list2):
  mapData = {}
  LinkListUnion = LinkedList()
  
  mapData,LinkListUnion = appendListStripDuplicates(list1,mapData,LinkListUnion)    #trasvere list1, add all the data to the new linkedList
  mapData,LinkListUnion = appendListStripDuplicates(list2,mapData,LinkListUnion)    #traverse list2, add all the data to the new linkedList
  return LinkListUnion

if __name__ == "__main__":

    """
        verify testcases
    """
    def run_testcases():

      # Test case 1
      linked_list_1 = LinkedList()
      linked_list_2 = LinkedList()

      element_1 = [3,2,4,35,6,65,6,4,3,21]
      element_2 = [6,32,4,9,6,1,11,21,1]

      for i in element_1:
          linked_list_1.append(i)

      for i in element_2:
          linked_list_2.append(i)

      print("Union of LinkedList1 and LinkedList2")
      print(union(linked_list_1,linked_list_2))

      print("Intersection of LinkedList1 and LinkedList2")
      print(intersection(linked_list_1,linked_list_2))

      # Test case 2
      linked_list_3 = LinkedList()
      linked_list_4 = LinkedList()
      element_1 = [3,2,4,35,6,65,6,4,3,23]
      element_2 = [1,7,8,9,11,21,1]

      for i in element_1:
          linked_list_3.append(i)

      for i in element_2:
          linked_list_4.append(i)

      print("Union of LinkedList3 and LinkedList4")
      print(union(linked_list_3,linked_list_4)) 

      print("Intersection of LinkedList3 and LinkedList4")
      print(intersection(linked_list_3,linked_list_4))

      # Test case 3
      linked_list_5 = LinkedList()
      linked_list_6 = LinkedList()
      element_1 = []
      element_2 = [1,7,8,9,11,21,1]

      for i in element_1:
          linked_list_5.append(i)

      for i in element_2:
          linked_list_6.append(i)

      print("Union of LinkedList5 and LinkedList6")
      print(union(linked_list_5,linked_list_6)) 

      print("Intersection of LinkedList5 and LinkedList6")
      print(intersection(linked_list_5,linked_list_6))

    run_testcases()
