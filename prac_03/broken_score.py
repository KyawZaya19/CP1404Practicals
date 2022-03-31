import random


def main():
    score = float(input("Enter your score: "))
    grade = determine_grade(score)
    print(grade)
    """ Random score and grade """
    random_score = random.randint(1, 101)
    print(random_score)
    random_grade = determine_grade(random_score)
    print(random_grade)


def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
