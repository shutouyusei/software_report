# プログラムの説明:
# このプログラムは、複数の学生の成績を管理し、合計点と平均点を計算し、
# 最も成績の良い学生を見つけます。
def run(students):
    best_score = 0
    best_student = ""
    for s in students:
        avg, total = average(s, students)
        best_score, best_student = get_better(s, total, best_score, best_student)
        print(f"Student: {s}, Total: {total}, Average: {avg}")
    return best_student, best_score


def get_better(s, total, best_score, best_student):
    if total > best_score:
        best_score = total
        best_student= s
    return best_score, best_student


def average(s, students):
    total = 0
    count = 0
    for g in students[s]:
        total += g
        count += 1
    avg = total / count
    return avg, total


students = {
    "Alice": [85, 90, 78],
    "Bob": [92, 88, 84],
    "Charlie": [70, 75, 80],
    "David": [95, 85, 90]
}

top_student, top_score = run(students)
print(f"Best student: {top_student} with total score: {top_score}")