def main():
    score = float(input("Enter your score: "))
    grade = verify_grade(score)
    print(grade)


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
