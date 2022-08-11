class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d={i:[] for i in range(numCourses)}
        res=[]
        for c,p in prerequisites:
            d[c].append(p)
        visitSet=set()
        def dfs(course):
            if course in visitSet:
                return False
            if d[course]==[]:
                if course not in res:
                    res.append(course)
                return True
            visitSet.add(course)
            for c in d[course]:
                if not dfs(c): 
                    return False
            res.append(course)
            visitSet.remove(course)
            d[course]=[]
            # res.append(course)
            return True
        for c in range(numCourses):
            if not dfs(c):return []
        return res