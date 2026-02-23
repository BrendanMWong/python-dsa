# Using a queue and stack is a trap

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_circular_count = 0
        student_square_count = 0
        for element in students:
            if element == 0:
                student_circular_count += 1
            else:
                student_square_count += 1
        
        for index in range(len(sandwiches)):
            if sandwiches[index] == 0:
                if student_circular_count == 0:
                    return student_circular_count + student_square_count
                student_circular_count -= 1
            else:
                if student_square_count == 0:
                    return student_circular_count + student_square_count
                student_square_count -= 1
        return 0