
def hasCycle(graph):
    visited=set()
    stack=set()
    def dfs(node):
        visited.add(node)
        stack.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfs(neighbour):
                    return True
            elif neighbour in stack:
                    return True
            else:
                stack.remove(node)
                return False
        for node in graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False
graph={1:[2],2:[3,4],3:[7,8],4:[5],5:[6],6:[4],8:[7]}
print(hasCycle(graph))
