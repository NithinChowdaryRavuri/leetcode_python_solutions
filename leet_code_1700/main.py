class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        counter1 = Counter(students)
        counter2 = Counter(sandwiches)
        if counter1 == counter2:
            return 0
        j = 0
        students = deque(students)
        while True:
            if students[0] == sandwiches[j]:
                counter1[students[0]] -= 1
                students.popleft()
                j += 1
            else:
                if counter1[sandwiches[j]] == 0:
                    return len(sandwiches) - j
                students.append(students.popleft())