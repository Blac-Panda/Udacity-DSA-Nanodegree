import sys
import heapq

class Node:
    def __init__(self,value, weight):
        """Create node for given symbol and weight."""
        self.left = None
        self.right = None
        self.value = value
        self.weight = weight        
        
    #compare weight of two Nodes
    def __lt__(self, other):
        return self.weight < other.weight
    
    #return a string version of Huff_Node, used for testing
    def __str__(self):
        return str(self.value)+" "+str(self.weight)
    
"""
Return ascending list of Huff Nodes
"""
def get_frequecies(data):
  freq = {}
  #dictionary of frequencies
  for item in data:
    if item not in freq:
      freq[item] = 1
    else:
      freq[item] +=1

  freq_sorted = sorted(zip(freq.values(), freq.keys()))

  for i in range(len(freq_sorted)): 
     freq = freq_sorted[i][0]  
     value = freq_sorted[i][1]
     
     freq_sorted[i] = Node(value, freq)
      
  return freq_sorted  


def huffman_tree(data):
    heap = get_frequecies(data)
    heapq.heapify(heap)
    while len(heap) != 1:
        newNode = Node(None,None)
        left = heapq.heappop(heap)
        newNode.left  = left
        right = heapq.heappop(heap)
        newNode.right  = right
        newNode.weight = left.weight + right.weight
        heapq.heappush(heap, newNode)
    return heap

"""
building huffman code table
"""
def code_table(root):
    code = {}
    #Traverse tree to build code table, where left edge is a 0 bit and right edge is a 1 bit
    def getCode(Node, currentCode=""):
        if (Node == None): 
            return
        if (Node.left == None and Node.right == None):
            code[Node.value] = currentCode
        getCode(Node.left, currentCode + "0")
        getCode(Node.right, currentCode + "1")
    getCode(root[0])
    return code

"""
Fucntion to return endoded string of 0s and 1s
"""
def huff_encode(data):
   
    if(len(get_frequecies(data))) == 1:
      return "0"*len(data)
    huff_code = "" 
    root = huffman_tree(data)
    table = code_table(root)#Huffman code dictionary
    for item in data:
       huff_code += table[item]
    return huff_code

#returns encoded data and root of the huffman tree
def huffman_encoding(data):
  
  return huff_encode(data), huffman_tree(data)


"""
Fucntion to return a Huffman decoded 
"""
def huffman_decode(bit_string,root):
    
    if(len(get_frequecies(bit_string))) == 1:
      return len(bit_string)*str(root.value)
    decode = ""
    n = len(bit_string)
    count = 0
    while count < n:
        current = root[0]
        while current.left != None and current.right != None:
            if bit_string[count] == "0":
                current = current.left
            else:
                current = current.right
            count+=1
        decode+=current.value
    return decode
  
#returns decoded Huffman code
def huffman_decoding(data,tree):
 
  return huffman_decode(data,tree)

"""
Run multiple testcases
"""
def test_Huffman(data):
  if data == None:
    print("----------")
    print(None)
  elif data == "":
    print("--------------------")
    print("Empty String")
  #single frequency data
  
  elif len(get_frequecies(data)) == 1:
    print("------------------------------------------------------------")
    code = "0"*len(data)
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(code, base=2))))
    print ("The content of the encoded data is: {}\n".format(code))
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(data)))
  else:
    print("------------------------------------------------------------")
    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))
    encoded_data, tree = huffman_encoding(data)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


def run_testcases():
    test_Huffman(None)          #Expected to return None
    test_Huffman("")            #Expected to return Empty string
    test_Huffman("Udacity")     #Single frequency data test
    #test with large data
    test_Huffman("Udacity Data Structures and Algorithms Nanodegree Program 2020. Project 2, Huffman Encoding")

run_testcases()
