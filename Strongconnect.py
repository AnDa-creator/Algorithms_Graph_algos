import csv
from operator import itemgetter


# import sys
# import threading
# # Will segfault without this line.
# sys.setrecursionlimit(2097152)    # adjust numbers
# threading.stack_size(134217728)   # for your needs


def create_graph(file):
    with open(file, 'r') as file:
        print("creating graph")
        global new_order
        global scc
        reader = csv.reader(file, delimiter=' ')
        length = 875714  # TODO put number of vertices here
        verticeslist = []
        adjacencyList = []
        revAdjList = []
        new_order = {}
        scc = []
        for i in range(0, length + 1):
            adjacencyList.append([])
            revAdjList.append([])
            scc.append([])
        index1, index2 = 0, 0
        for line in reader:
            temp = index1
            temp2 = index2
            index1 = int(line[0])
            index2 = int(line[1])
            adjacencyList[index1].append(index2)
            revAdjList[index2].append(index1)
            if temp % (5 * 10 ** 4) == 0 and temp >= (5 * 10 ** 4) and temp != index1:
                print("currently processed adjacency list for {} vertices".format(temp))
                print("currently processed revadjacency list for vertex {} ".format(temp2))

            if index1 not in verticeslist:
                verticeslist.append(index1)
            if index2 not in verticeslist:
                verticeslist.append(index2)
        print("Created graph succesfully")
    return verticeslist, adjacencyList, revAdjList


def dfs_scc(graph, vertex, explored):
    global scc
    explored.append(vertex)
    scc[vertex] = numSCC
    for endpoint in graph[1][vertex]:
        if endpoint not in explored:
            dfs_scc(graph, endpoint, explored)


def dfs_scc_iter(graph, vertex, explored):
    print("Starting dfs on new index")
    a_stack = []
    global scc
    a_stack.append(vertex)
    while len(a_stack) != 0:
        point = a_stack.pop()
        if point not in explored:
            explored.append(point)
            scc[point] = numSCC
            for another_point in graph[1][point]:
                a_stack.append(another_point)
    print("dfs on new indices done successfully")


def topo_sort(graph, index):
    print("Starting Topographical Sort")
    explored = []
    global curlabel
    curlabel = len(graph[0])
    for point in graph[0]:
        if point not in explored:
            dfs_topo_iter(graph, point, explored, index)

    print("Topographical sorting done")
    return explored, new_order


def dfs_topo(graph, vertex, explored, index):
    global curlabel
    explored.append(vertex)
    for point in graph[index][vertex]:
        if point not in explored:
            dfs_topo_iter(graph, point, explored, index)
    new_order.update({vertex: curlabel})
    curlabel -= 1


def dfs_topo_iter(graph, vertex, explored, index):
    global curlabel
    a_stack = [vertex]
    while len(a_stack) != 0:
        point = a_stack.pop()
        if point not in explored:
            explored.append(point)
            for another_point in graph[index][point]:
                a_stack.append(another_point)
            new_order.update({point: curlabel})
            curlabel -= 1


def kosaraju(graph):
    print("Starting Kosaraju")
    explored_rev, new_order = topo_sort(graph, 2)
    global numSCC
    global curlabel
    global scc
    numSCC = 0
    explored = []
    new_list = []
    new_order = sorted(new_order.items(), key=itemgetter(1))
    for index in new_order:
        new_list.append(index[0])
    for point in new_list:
        if point not in explored:
            numSCC += 1
            dfs_scc_iter(graph, point, explored)

    print("Kosaraju completed Successfully")
    return numSCC, scc


if __name__ == '__main__':
    global new_order
    global numSCC
    global scc
    graph = create_graph("SCC.txt")
    num, array = kosaraju(graph)
    array.remove([])
    print("The number of SCC is {}".format(num))
    numcomp = sorted(array)
    i = 1
    countmax = []
    for j in range(1, num + 1):
        countmax.append(0)
    for item in numcomp:
        while True:
            if item != i:
                i += 1
            elif item == i:
                countmax[item - 1] += 1
                break

    print("The SCC array in sorted order is {}".format(sorted(countmax, reverse=True)))
