import csv


def read_graph(file):
    with open(file, 'r') as graph:
        print('Reading Graph...')
        reader = csv.reader(graph, delimiter='\t')
        length = 200 # TODO Put the number of vertices here
        verticesList = []
        adjacencyList = []
        for i in range(0, length + 1):
            adjacencyList.append([])

        for line in reader:
            vertex = int(line[0])
            verticesList.append(vertex)
            for item in line[1:]:
                adjVerDist = item.split(',')
                adjVerDist = [int(x) for x in adjVerDist if x != '']
                adjacencyList[vertex].append(adjVerDist)

            if [] in adjacencyList[vertex]:
                adjacencyList[vertex].remove([])
            # print(adjacencyList[vertex])
        print("Graph Creation completed successfully")
        # print(verticesList)
    return verticesList, adjacencyList


def dijkstra(source, adjacencyList, verticesList):
    ShortLenghts = [1000000 if vertex != source else int(0) for vertex in verticesList]
    print("dijkstra started...")
    captured = [source]
    edgeList = []
    for vertex in verticesList:
        for item in adjacencyList[vertex]:
            newEdge = [vertex, item[0], item[1]]
            if newEdge not in edgeList:
                edgeList.append(newEdge)
    # print(edgeList)
    while len(captured) != len(verticesList):
        minlen = 1000000
        edgeReturned = [0, 0, 0]
        for edge in edgeList:
            # print(edge)
            if edge[0] in captured and edge[1] not in captured:
                # print(True)
                newlen = edge[2] + ShortLenghts[edge[0]-1]
                # print(newlen)
                if newlen < minlen:
                    edgeReturned = edge
                    # print('hello')
                    minlen = edge[2] + ShortLenghts[edge[0]-1]

        captured.append(edgeReturned[1])
        # print(captured)
        ShortLenghts[edgeReturned[1]-1] = minlen
    print("dijkstra ends")
    return ShortLenghts


if __name__ == '__main__':
    verticesList, adjacencyList = read_graph('dijkstra.txt')
    # num = int(input("Enter the Source vertex: "))

    # endnum = int(input("Enter the terminal vertex: "))
    Shortestpath = dijkstra(1 , adjacencyList, verticesList)
    numnew = [7,37,59,82,99,115,133,165,188,197]
    diction = []
    for num in numnew:
        print("Shortest path from {} to {} is {}".format(1, num, Shortestpath[num - 1]))
        diction.append(Shortestpath[num-1])
    print(diction)