if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student_avg = {}
    for name,marks in student_marks.items():
        student_avg[name] = f'{sum(marks)/len(marks):.2f}'
        
    print(student_avg[query_name])
