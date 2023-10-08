def main():
    # 학생 정보 입력 받기
    name = input("이름을 입력하세요: ")
    student_id = input("학번을 입력하세요: ")
    department = input("학과를 입력하세요: ")
    grade = input("학년을 입력하세요: ")

    # 학생 정보 출력
    print("\n입력한 학생 정보:")
    print("이름:", name)
    print("학번:", student_id)
    print("학과:", department)
    print("학년:", grade)

if __name__ == "__main__":
    main()
