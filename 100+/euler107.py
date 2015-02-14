def read_in_graph():
    f = open("p107_network.txt", "r")
    rows = f.read().split("\n")
    graph = []
    
    for row in rows:
        graph.append(row.split(","))

    return graph    

def min_graph_wgt(graph):
    min_graph = []
    for _ in range(len(graph)): min_graph.append(["-"]*len(graph[0]))
    nodes_in_graph = [0]

    # Prim's Algorithm
    while len(nodes_in_graph) < len(graph):
        mini = (1000000, 0, 0)
        for i in nodes_in_graph:
            for j in range(len(graph)):
                if j in nodes_in_graph or graph[i][j] == "-": continue
                if int(graph[i][j]) < mini[0]: mini = (int(graph[i][j]), i, j)

        min_graph[mini[1]][mini[2]] = graph[mini[1]][mini[2]]
        nodes_in_graph.append(mini[2])

    min_wgt = 0

    # calculate weight at start
    for i in range(len(min_graph)):
        for j in range(len(min_graph[i])):
            if min_graph[i][j] != "-": min_wgt += int(min_graph[i][j])
            
    return min_wgt

def euler107():
    graph = read_in_graph()[:-1]
    start_wgt = 0

    # calculate weight at start
    for i in range(len(graph)):
        for j in range(i+1, len(graph[i])):
            if graph[i][j] != "-": start_wgt += int(graph[i][j])

    min_wgt = (min_graph_wgt(graph))
    return start_wgt - min_wgt

if __name__ == "__main__":
    print euler107()
