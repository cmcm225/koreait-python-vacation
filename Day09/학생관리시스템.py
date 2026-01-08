#학생관리시스템

students=[]
#{ "name": "이름", "student_id": 1, "major": "컴공" }
#[{},{},{},...,{}]

#메인 루프
while (True):
    print("=== 학생 관리 시스템 ===")
    print("1. 학생 등록")
    print("2. 전체 학생 조회")
    print("3. 학생 삭제(이름)")
    print("q. 종료")

    selected_menu= input("메뉴 번호 입력>>")
    if selected_menu == "1":
        #학생등록
        print("학생 등록메뉴 입니다.")
        name= input("이름>>")
        stu_id= input("학번>>")
        major= input("전공>>")

        # 1. 이미 있는 학번인지 확인 하고, 중복학번이 입력되면
        #"이미 존재하는 학번입니다"
        # continue
        is_duplicated = False
        for stu_dict in students: #리스트에서 가져온건 dict
            #dict에서 필요한 value만 꺼냄
            std_id= stu_dict["stu_id"]
            if std_id == stu_id: #비교
                print("이미 존재하는 학번입니다.")
                break
        if is_duplicated:
            continue

        new_student={
            "name":name,
            "student_id":stu_id,
            "major":major
        }
        pass

        students.append(new_student)

        print(f"{name}학생이 등록되었습니다.")
    elif selected_menu == "2":
        # 2. 학생이 아무도 없으면, "등록된 학생이 없습니다" 출력
        #자동형변환&len()
        if not len(students)==0:
            print("등록된 학생이 없습니다.")
            continue

        #학생 전체 조회
        for student in students:
            stu_id= student["student_id"]
            name=student["name"]
            major= student["major"]
            print(f"{stu_id}: 이름-{name}, 전공-{major}")


    elif selected_menu == "3":
        #학생 삭제
        if len(students)==0:
            print("등록되어있는 학생이 없습니다.")
            continue

        target_std=input("삭제할 학생의 학번>>")
        found=False
        for stu_dict in students:
            found=True
            std_id= stu_dict["student_id"]
            if std_id == target_std:
                students.remove(stu_dict)
                print(f"{std_id}학번 학생 삭제 완료")
                break

        if not found:
            print("해당 id의 학생을 찾을 수 없습니다.")

    elif selected_menu == "q":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시입력하세요.")
        continue

