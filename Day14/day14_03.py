colors=["빨강","파랑","노랑","블랙","화이트"]

#아래의 코드에서 예외가 발생 경우의 수를 고려하여
#예외처리를 작성해주세요
#정상적이면 result 출력
#마지막엔 항상 "안녕히 가세요" 출력
# try:
#     my_idx= input ("번호입력>>")
#     my_idx = int(my_idx) # ValueError
#     result = colors[my_idx] # IndexError
# except (ValueError,IndexError) as e:
#     print("정상적인 값을 입력하십시오!")
#     print(f"에러내용:{e}")
# else:
#     print(f"선택한 색상:{result}")
# finally:
#     print("안녕히 가세요!")

# raise:예외를 의도적으로 생성하는 문법
try:
    # 생성할때 넣어주는 문자열
    raise ValueError("저는 님이 만든 에러입니다.")
except ValueError as e:
    # e 메세지
    print(e)

# 커스텀(비지니스) 에러
#Exception을 상속받으면 된다
#Exception -> 모든 에러의 부모클래스
class NegativeScoreError(Exception):
    def __init__(self,message):
        super().__init__(message)
        self.message=message

    def __str__(self):
        return self.message

try:
    score=input("점수를 입력하세요>>")
    score=int(score)
    if score<0:
        raise NegativeScoreError("점수는 음수일수 없습니다")
except NegativeScoreError as e:
    print(e)

#커스텀 에러를 정의하고
#사용자에게 이메일주소를 입력받고,
# "@", ".com"가 없으면 InvalidEmailError 예외를 발생
#올바르지 않으면 -> "올바르지않은 이메일 형식입니다" 출력
#올바르다면 -> "올바른 이메일입니다" 출력
class InvalidEmailError(Exception):
    def __init__(self):
        self.message= "유효하지않은 이메일 형식"
        super().__init__(self.message)
try:
    email=input("이메일주소를 입력하세요>>")
    if "@" not in email or not email.endswith(".com") :
        raise InvalidEmailError()
except InvalidEmailError as e:
    print(e)
else:
    print("올바른 이메일입니다")

"""
시스템이 복잡해지면 f(f(f(f(f())))) 복잡도 상승
return으로는 한계존재한다.
즉시 멈추고 바로 탈출할 수 있는 문법 필요하다! -> 커스텀예외 던지기
"""