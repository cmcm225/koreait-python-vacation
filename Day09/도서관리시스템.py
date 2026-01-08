books=[]
#{"book_id": "1", "book_name":"파이썬책"
#[ {},{},{}]
while True:
    print("== 독서관리시스템 ==")
    print("1.도서 등록")
    print("2. 전체 도서 조회")
    print("3. 도서 삭제")
    print("q. 종료")

    selected_menu=input("메뉴를 선택>>")
    if selected_menu=="1":
        print("도서 등록메뉴입니다")
        book_id=input("도서번호를 입력하세요>>")
        book_name=input("도서명을 입력하세요>>")

        is_duplicated=False
        for book_dict in books:
            book_id= book_dict["book_id"]
            if book_id==book_id:
                print("이미 등록된 도서번호입니다")
                break
        if is_duplicated:
            continue

        new_book={
            "book_id":book_id,
            "book_name":book_name,
        }

        pass

        books.append(new_book)
        print(f"{book_name}이 등록되었습니다.")

    elif selected_menu=="2":

        if len(books)==0:
            print("등록된 도서가 없습니다.")
            continue

        for book in books:
            book_id= book["book_id"]
            book_name= book["book_name"]
            print(f"도서번호:{book_id}, 도서명:{book_name}")

    elif selected_menu=="3":
        if len(books)==0:
            print("삭제할 도서가 없습니다")
            continue

        targeted_book=input("삭제할 도서번호를 입력하세요")
        found= False
        for book in books:
            if book["book_id"]==targeted_book:
                found=True
                books.remove(book)
                print(f"{book["book_id"]}번호 삭제 완료")
        if not found:
            print("해당 도서번호는 존재하지 않습니다.")

    elif selected_menu=="q":
        break
    else:
        print("잘못된 입력입니다. 다시입력하세요.")
        continue