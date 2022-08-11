class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        d={i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            d[course].append(pre)
        visitSet=set()
        def dfs(course):
            if course in visitSet:
                return False
            if d[course]==[]:
                return True
            visitSet.add(course)
            for p in d[course]:
                if not dfs(p):
                    return False
            visitSet.remove(course)
            d[course]=[]
            return True
        for c in range(numCourses):
            if not dfs(c): return False
        return True
                