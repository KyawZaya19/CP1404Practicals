import random


def main():
    score = float(input("Enter your score: "))
    grade = verify_grade(score)
    print(grade)
    random_score = random.randint(1, 101)
    print(random_score)
    random_grade = verify_grade(random_score)
    print(random_grade)


def verify_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
