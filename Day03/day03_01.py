"""
멀티라인-함수설명(docString)용
변수에 할당하지 않으면, 주석처럼 사용가능
"""
name="홍길동"
test=f"""Hello World 
my name is {name} """
print(test)
"""
조건문
if bool 데이터:
    bool데이터가 True일때 실행되는 코드
"""
#코드블럭- 코드의 영역
# 들여쓴 부분을 하나의 코드블럭으로 간주한다.
if False:
    print('if문 안쪽입니다')
print("if문 밖입니다.")

# 10만원 이상이면 10%할인가격
# 아니면 할인없는 가격
# input() 으로 받아온 데이터는 모구 str이다
#price=input("상품가격을 입력하세요>>")
#price=int(price)

#if price>100000:
    #price=price*0.9
   # print(price)
#else: #위의 모든 조건이 False일때
    #print(price)
#if~elif~else: 하나의 블럭 코드만 실행
#순차적으로 검사 (위->아래)

age=15

#조건은 내림차순,오름차순으로 작성되어야함
if age>=20:
    print("성인")
elif age >=17: #이전조전이 False 였다
    print("고등학생")
elif age >=14:
    print("중학생")
elif age >=8:
    print("초등학생")
else:
    print("미취학아동")

isLogin=False
isBanned=True

if not isLogin:
    #로그아웃 상태리면
    print("로그인을 하셔야합니다")
elif isBanned:
    print("정지된 계정입니다")
"""
bmi 계산기
bmi= 체중(kg)/키(m)*키(m)
bmi가
30이상 비만/25이상 30미만 과체중
18.5이상 25 미만 정상/18.5 미만 저체중
철수(174cm,70kg)의 비만도를 출력
"""
weight=70
height=174/100
bmi= weight/height**2
if bmi>=30:
    print("비만")
elif bmi>=25: # 위의 조건들이 False -> and bmi<30
    print("과체중")
elif bmi>=18.5: # bmi<25
    print("정상")
else:
    print("저체중")

# 홀짝 판별
#num이하는 변수에 숫자 입력 받고
#짝수면 짝수입나다. 홀수면 홀수입니다. 출력
num=input("숫자를 입력하세요>>")
num=int(num) #str->int 형변환
isEven=num%2==0
if isEven:
    print("짝수입니다")
else:
    print("홀수입니다")
