#문자열의 처음과 끝이 무엇인지 검사
#srartswith(), endswith()
email="python@py.com"
print(email.startswith ("python"))
print(email.endswith(".com"))

name="홍길동"
# 성씨가 홍인지 검사 -> true/false
# 2가지 방법 / a==b:a가 b와 같나요?
print(name.startswith("홍"))
print(name[0]=="홍")


production="**[SALE] Apple iphone 17 pro** "
# apple iphone 17 pro
#strip(), replace(), lower()
production_strip = production.strip("*")

#문자열기능들은 원본을 바꾸지 X
print("원본:",production)
print("가공:",production_strip)

# **앞뒤 제거
production=production.strip("*")
# [SALE] 제거
producton=production.strip("[SALE]")
#소문자처리
producton = producton.lower()

print(producton)
#기능들?-> 함수:특정기능들을 실행하는 단위
# 함수의 결과가 값이같아지면 사용이 가능하다.
production="**[SALE] Apple iphone 17 pro** "
productoin=production.strip("*").replace("[SALE]","").lower()

