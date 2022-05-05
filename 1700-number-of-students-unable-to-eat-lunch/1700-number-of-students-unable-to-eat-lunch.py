class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        s1=students
        while True:
            if len(sandwiches)==0:
                if len(students)==0:
                    return 0
                else:
                    return len(students)
            if sandwiches[0] not in students:
                return len(students)
            if students[0]==sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                # print('poping',i,students,sandwiches)
            else:
                students.append(students[0])
                students.pop(0)
                # print('NOt Poping',i,students,sandwiches)