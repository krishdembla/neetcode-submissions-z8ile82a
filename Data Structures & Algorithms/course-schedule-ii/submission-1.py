class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #if cycle is found return []
        # a startnode (first ele in return) cannot have prereq
        adj = defaultdict(list)

        for course,prereq in prerequisites:
            adj[prereq].append(course)
        
        in_deg = [0] * numCourses #count of incoming edges (prereq) for each vertex node

        for u in adj:
            for v in adj[u]:
                in_deg[v] += 1
        
        queue = deque(i for i in range(numCourses) if in_deg[i] == 0) #appending all nodes with no prereq
        topo_order = []

        while queue:
            u = queue.pop()
            topo_order.append(u)

            for v in adj[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    queue.append(v)
            
        return topo_order if len(topo_order) == numCourses else []

