b = 0
c = 0
grades1 = []
print("How many grades will you enter? ")
numGrades = int(input())
print("Enter grades: ")
for x in range(numGrades):
    grades = int(input())
    grades1.append(grades)
print("No   Grades   Letter Grades")
letters = []
for c in grades1:
    b += 1
    if (c <= 100 and c >= 90):
        letters.append("A")
        print(b, ' \t\t', "{}".format(c), '\t\t', "A")
    elif c >= 80:
        letters.append("B")
        print(b, ' \t\t', f"{c}", '\t\t', "B")
    elif c >= 70:
        letters.append("C")
        print(b, ' \t\t', f"{c}", '\t\t', "C")
    elif c >= 60:
        letters.append("D")
        print(b, ' \t\t', f"{c}", '\t\t', "D")
    elif c >= 0:
        letters.append("F")
        print(b, ' \t\t', f"{c}", '\t\t', "F")
print("Histogram")
print("---------")
print(f"A = {letters.count('A')}")
print(f"B = {letters.count('B')}")
print(f"C = {letters.count('C')}")
print(f"D = {letters.count('D')}")
print(f"F = {letters.count('F')}")