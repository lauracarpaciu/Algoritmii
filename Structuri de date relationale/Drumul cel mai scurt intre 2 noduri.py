import sys
from typing import List, Any


def getShortestPath(source, dest, graph):
    numberOfNodes= len(graph)-1
    distances=[]
    isVisited=[]

    for nodeIndex in range(0,numberOfNodes):
        distances.append(sys.maxsize)
        isVisited.append(False)

    distances[source]=0
    iterationCounter = 0
    while iterationCounter<=numberOfNodes:
        minDistance=sys.maxsize
        closestNode=-1
        for nodeIndex in range(1,numberOfNodes):
            if not isVisited[nodeIndex] and distances[nodeIndex]<minDistance:
               closestNode=nodeIndex
               minDistance=distances[nodeIndex]

        isVisited[closestNode]=True

        for nodeIndex in range(1,numberOfNodes):
            if graph[closestNode][nodeIndex]>0 and not isVisited[nodeIndex]:
                edgeCost=graph[closestNode][nodeIndex]
                distanceToNeighbor=distances[closestNode]+edgeCost
                if distanceToNeighbor<distances[nodeIndex ]:
                    distances[nodeIndex]=distanceToNeighbor
        iterationCounter += 1

    return distances[dest]







cities: list[Any]=[]

cities=[
        [0,0,0,0,0],
        [0, 0, 5, 3, 10],
        [0, 5, 0, 0, 4],
        [0, 3, 0, 0, 2],
        [0, 10, 4, 2, 0]
             ]
a=getShortestPath(1,2,cities)
print(a)