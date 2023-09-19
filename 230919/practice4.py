class Grade:
  def __init__(self, name, student_number, major):
    self.name = name
    self.student_number = student_number
    self.major = major
    self.score = {}

  def inputScore(self,subject,score):
    self.scores[subject] = score

  def calculateAverage(self):
    if not self.score:
      return 0.0
    total_score = sum(self.score.values())
    return total_score / len(self.score)

  def calculateGrade(self):
    average = self.calculateAverage()
    if 4.0 < score <= 4.5:
      return 'A+'
    elif 3.5 < score <= 4.0:
      return 'B+'
    elif 3.0 < score <= 3.5:
      return 'C+'

  def displayScore(self):
    print(f"학생: {self.name, self.student_number}")
    for subject, score in self.score.items():
      print(f"{subject}: {score}")
    average = self.calculateAverage()
    grade = self.calculateGrade()
    print(f"평균 점수: {average:.2f}")
    print(f"학점: {grade}")

  def main():
    student_name = input("학생의 이름을 입력하세요: ")
    student = Student(student_name)

    while True:
        print("\n1. 성적 입력")
        print("2. 성적 출력")
        print("3. 종료")
        choice = input("메뉴를 선택하세요 (1/2/3): ")

        if choice == '1':
            subject = input("과목 이름을 입력하세요: ")
            score = float(input("성적을 입력하세요: "))
            student.add_score(subject, score)
        elif choice == '2':
            student.display_scores()
        elif choice == '3':
            break
        else:
            print("올바른 메뉴를 선택하세요.")


if __name__ == "__main__":
    main()