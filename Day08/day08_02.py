dialog="솔직히 말해서 솔직히 저는 이게 맞는지 모르겠습니다. 솔직히 근데 그냥 솔직히 귀찮습니다."

word="솔직히"

#"솔직히"라는 단어는 몇 번 반복하는지?
count=0
len_of_word=len(word)
len_of_dialog=len(dialog)
for i in range(len_of_dialog):
    tmp = dialog[i:i+len_of_word]
    if tmp == word:
        count+=1

print(f"솔직히가 등장한 횟수:{count}")

#-> 문장과 단어를 매개변수로 받고
#단어가 문장안에서 몇 번 등장하는지 리턴하는 함수
count=0
def count_repeat(dialog,word):
    for i in range(len_of_word):
       tmp = dialog[i:i + len_of_word]
 #      if tmp == word:
  #          count+= 1

    return count_repeat
count = count_repeat ("아브라카다브라 다브라","다브라")

#할인 계산기
menu={
    1:("아메리카노",2500),
    2:("카푸치노",4000),
    3:("바닐라 라떼",3500),
}
menu_choice=input("메뉴를 선택하세요(1~3) >>")
menu_choice=int(menu_choice) # 숫자로 변환

menu_name, price=menu[menu_choice]
print(f"내가고른 메뉴:{menu_name}, 가격:{price}")

day= input("오늘은 무슨 요일인가요?(월~일)>>")
#day를 매개변수로 전달 받아서
#월:10%,화~금:5%, 토~일20%
#적용해서 최종가격을 리턴하는 함수
def calc_week_discount(day,price):
    day= day.strip() # 좌우공백 제거

    if day=="월":
        price*=0.9
    elif day in ["화","수","목","금"]:
        price*=0.95
    elif day in ["토","일"]:
        price*=0.8

    return price

total_price=calc_week_discount(day,price)
print(f"주문화신 음료:{menu_name}, 결제금액:{total_price}")

