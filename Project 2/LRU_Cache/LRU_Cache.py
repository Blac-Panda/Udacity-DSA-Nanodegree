class Node(object):
 
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node(key: {self.key}, value: {self.value})"
    
    def __str__(self):
        return f"Node(key: {self.key}, value: {self.value})"

#create a DoublyLinkedList

class DLL(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodeCount = 0

    def removeNode(self,node) :

        if (node.prev != None):
            node.prev.next = node.next
        else:
            self.head = node.next
   

        if (node.next != None) :
            node.next.prev = node.prev
        else:
            self.tail = node.prev
    

        self.nodeCount -= 1

    def prependNode(self,node):

        node.next = self.head
        node.prev = None

        if (self.head != None):
            self.head.prev = node

        self.head = node

        if (self.tail == None):
            self.tail = self.head

        self.nodeCount += 1
        return node;

    """
    adding a node with key and value to the top of the list
    """
    def prepend(self, key, value): 
        new_node = Node(key,value,None,None)
      
        return self.prependNode(new_node);

    """
    adding a node with key and value to the bottom of the list
    """
    def append(self, data):
        new_node = Node(key,value,None,None)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None

            print(self.tail)

            self.tail.next = new_node
            self.tail = new_node
        self.nodeCount += 1
        return node;

    """
    Displays data inside the linked list
    """
    def printList(self):
        print ("-"*10)
        print ("\n\nShow Doubly linked list data:")
        print ("-"*30)
        current_node = self.head
        counter = 0;
        while current_node is not None:
            counter +=1;
            print ("\n"),
            print (f"{counter}:"),
            print (f"prev:    {current_node.prev}") if hasattr(current_node.prev, "value") else None,
            print (f"current: {current_node}"),
            print (f"next:    {current_node.next}") if hasattr(current_node.next, "value") else None
 
            current_node = current_node.next
        print ("-"*30,"\n\n\n")

"""
Use a dictionary to store pointers to nodes in the cache.
"""
class LRU_Cache(DLL):

    def __init__(self, capacity = 0):
        # Initialize class variables
        self.capacity = capacity
        self.cStorage = {}

        # Called the DoublyLinkedList constructor
        super().__init__()


    def get(self,key):

        if key in self.cStorage:
            node = self.cStorage.get(key)
            self.removeNode(node)
            self.prependNode(node)
            return node.value
        
        return -1
    
    def set(self,key, value) :
        """
        The key already exist, update its value and move the node to the top/front of the list
        """
        if key in self.cStorage:
            node = self.cStorage.get(key)
            node.value = value
            self.removeNode(node)
            self.prependNode(node)
        else :
            """
                The cache's maximum capacity has been reached    
                remove the "least recently used" (oldest item) item from the cache by deleting it from linkedlist and from the hashmap
            """
            if (len(self.cStorage) == self.capacity):
              del self.cStorage[self.tail.key]
              self.removeNode(self.tail)
            
            """
                Add the new node to top/front of the list
            """    
            newnode = self.prepend(key,value)
        
            self.cStorage[key] = newnode

if __name__ == '__main__':
	
	"""
	    Add data to the cache in order to verify the values stored
	"""
	def run_test():
	    our_cache = LRU_Cache(5)

	    our_cache.set(1, 1);
	    our_cache.set(2, 2);
	    our_cache.set(3, 3);
	    our_cache.set(4, 4);

	    print(our_cache.get(1))      # returns 1
	    print(our_cache.get(2))      # returns 2
	    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
	    print(our_cache.get(''))     # returns -1 because input is null

	    # Move items in the cache, so that they are positioned closer to the top of the recently used list
	    our_cache.set(5, 5) 
	    our_cache.set(6, 6)

        # returns -1 because 3 was the least recently used entry when the cache reached it's capacity, therfore it got deleted
	    print(our_cache.get(3) ) 

	    print("Nodes in list: ",our_cache.nodeCount)
	    
	    print(list(our_cache.cStorage.keys()))
	    # Uncomment our_cache.printList function to view the Doubly LinkedList
	    #our_cache.printList()

	run_test()
