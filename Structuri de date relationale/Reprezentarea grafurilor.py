class GraphNode:
   name=''
   links={'key':'GraphNode'}

class MyGraph:

    def __init__(self,nodes={'key':'GraphNode'}):
        self.__nodes=nodes

    def addNode(self, nodeName, links):
        currentNode=self.__nodes.get(nodeName)
        if not currentNode:
            currentNode={"name",'links'}
        self.__nodes[nodeName]=currentNode

        for linkToAdd in links:
            oldLink=currentNode.add(linkToAdd)
            if not oldLink :
                linkNode=self.__nodes.get(linkToAdd)

            if not linkNode :
                 linkNode={"name",'links'}
            self.__nodes[linkToAdd]   =linkNode


    def printLinks(self,nodeName):
        try:
            node=self.__nodes[nodeName]
            print(node)
        except KeyError:
           print("Nu exista acest nod")
        # if(not node):
        #     print("Node does not exist")
        #     return

friendsGraph=MyGraph()
friendsGraph.addNode("A",["B","D"])
friendsGraph.addNode("B",["A","D"])
friendsGraph.addNode("C",["D"])
friendsGraph.addNode("D",["A","B","C"])
friendsGraph.printLinks("A")
friendsGraph.printLinks("B")
friendsGraph.printLinks("C")
friendsGraph.printLinks("D")
friendsGraph.printLinks("E")

