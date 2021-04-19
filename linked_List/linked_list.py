#from node import node

#node CLASS
class Node:
    #function to initialze the node object
    def __init__(self, dataVal):
        self.dataVal = dataVal #Assinging DATA
        self.nextVal = None #Initialize 'NEXT' as NULL

#linked List class contain node object
class sLinkedList:
    def __init__(self):
        self.headVal = None

if __name__ == 'main':

    lkdList = sLinkedList()

    lkdList = Node(1)
    sec = Node(2)
    third = Node(3)


    #LINKING NODE
    lkdList.headVal = Node(1) #head value here
    lkdList.headVal.nextVal = sec



"""

    #adding LIST TRAVERSAL : here
    def listprint(self):
        printval = self.headVal
        while printval is not None:
            print(printval.dataVal)
            printval = printval.nextVal

# LINKED LIST -  DAYS OF WEEK Expiramentation.
listOne = sLinkedList()
listOne.self = Node("Mon")
add2 = Node("Tue")
add3 = Node("Wed")
add4 = Node("Thur")

#link first Node to second Node
listOne.headVal.nextVal = add2

#link third NODE to ssecond
add2.nextVal.nextVal = add3

#list.listprint()
#list.p(sLinkedList)

"""


