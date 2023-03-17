def add_node(v):
    if v in graph:
        print(v, "is already present in graph")
    else:
        graph[v] = []
def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "not present")
    elif v2 not in graph:
        print(v2, "not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def delete_node(v):
    if v not in graph:
        print(v, " not present in graph")
    else:
        graph.pop(v)
        for i in graph:
            list1 = graph[i]
            if v in list1:
                list1.remove(v)
def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, " is not present in graph")
    elif v2 not in graph:
        print(v2, " is noe present in graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)
def DFS(node, graph):
    visited = set()
    if node not in graph:
        print("The node not in graph")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current, "-->", end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)
def BFS(node, graph):
    visited = set()
    if node not in graph:
        print("The node not in graph")
        return
    queue = []
    queue.append(node)
    while queue:
        current = queue.pop(0)
        if current not in visited:
            print(current, "-->", end=" ")
            visited.add(current)
            for i in graph[current]:
                queue.append(i)
graph = {}
add_node("100")
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge("A", "B")
add_edge("B", "E")
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "D")
add_edge("C", "D")
add_edge("E", "D")
# print(graph)
# delete_node("C")
# print("After node deletion")
# print(graph)
# print("After edge deletion")
# delete_edge("B", "D")
# print(graph)
# print("DFS")
DFS("A", graph)
# print("\nBFS")
# BFS("A", graph)
