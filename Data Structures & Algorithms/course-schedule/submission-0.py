class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        courses_taken = 0

        while queue:
            u = queue.pop()
            courses_taken += 1
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                
        return courses_taken == numCourses