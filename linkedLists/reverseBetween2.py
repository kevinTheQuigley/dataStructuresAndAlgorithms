class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0
    
    def reverse_between(self,start,end):
        diff = end-start
        currentIndex = 0
        currentNode = self.head
        nextNode = self.head.next
        nextNextNode = 0

        startingNode = self.head
        preStartingNode = None
  
        postFinalNode= None
        finalNode = None
        if diff <1:
            return None

        while currentIndex < start:
            preStartingNode = currentNode
            currentIndex+=1
            #print(f"Current Nodes pre {currentNode.value}->{currentNode.next.value} ")
            currentNode = currentNode.next
        nextNode = currentNode.next

        startingNode = currentNode
        if preStartingNode is not None:
            print(f"The pre-starting node has value {preStartingNode.value}")
        print(f"The startingNode has value {startingNode.value} and it is located at position {start} ")
        
        while currentIndex < end-1 :
            print(f"current index is {currentIndex}, and the value is {currentNode.value}")
            currentIndex+=1

            print(f"Current Node values {currentNode.value}->{currentNode.next.value} ")

            if nextNode.next is not None:
                print(f"Next Nodes pre reverse {nextNode.value}->{nextNode.next.value} ")
                nextNextNode = nextNode.next
                nextNode.next = currentNode
                currentNode = nextNode
                nextNode = nextNextNode
                print(f"next nodes After reversing: {nextNode.value}  ")
        print("Before last reversal:-----------")
        print(f"Current index is {currentIndex}, and the value is {currentNode.value}")
        print(f"next value is {nextNode.value} and the following value is {nextNode.next}")

        if nextNode.next is None:
            nextNode.next = currentNode
            finalNode = nextNode
            print(f"Final reverse: as nextNode is None {finalNode.value}->{finalNode.next.value} ")
            print(f"After reversing: {finalNode.value}->{finalNode.next.value} ->{finalNode.next.next.value}->{finalNode.next.next.value}")
            print(f"After reversing: {self.head.value}->{self.head.next.value} ->{self.head.next.next.value}->{self.head.next.next.value}")
        else:
            postFinalNode = nextNode.next
            finalNode = nextNode
            print(f"Final reverse : {finalNode.value}->{finalNode.next.value} ")
        """
        if nextNode.next is None:
            startingNode.next = nextNode
            preStartingNode.next = currentNode
            finalNode = nextNode
            print(f"Final reverse: as nextNode is None {startingNode.value}->{finalNode.next} ")
        """

        if preStartingNode is not None:
            preStartingNode.next = finalNode
            print(f"switching prestartingNode {preStartingNode.value} to align with {finalNode.value}")

        if startingNode is not None :
            startingNode.next = postFinalNode
            #print(f"After reversing: {startingNode.value}->{startingNode.next.value} ")
            #print(f"After reversing: {startingNode.value}->{startingNode.next.value} ->{startingNode.next.next.value}->{startingNode.next.next.value}")




                

        if startingNode ==self.head:
            self.head = finalNode
        

    # WRITE REVERSE_BETWEEN METHOD HERE #
    #                                   #
    #                                   #
    #                                   #
    #                                   #
    #####################################
    


linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("\nReversed sublist (2, 4): ")
linked_list.print_list()
print ("Should appear like 1,2,5,4,3")


print("\nStarting on the next reversal \n")
linked_list.reverse_between(1, 3)
print("\nReversed sublist (1, 3): ")
linked_list.print_list()
print ("Should appear like 1,4,5,2,3")

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
