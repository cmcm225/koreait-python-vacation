# 클래스
# 클래스의 쉬운 설명: 내가 새로운 자료형을 정의하는 것

a= 10
b="abc"
#자료형은 사실 클래스였다
print(type(a))
print(type(b))
print(b.upper()) #str 클래스에는 여러 함수 존재

# 클래스란 특정 데이터와 동작(함수)을 묶은 것

#클래스는 첫글자 대문자(관례)
class Puppy:
    #__init__(self, 내가 이 클래스에 넣고 싶은 데이터들)
    #-> 생성자
    #name, age와 같은 객체의 공간
    #-> 필드, 멤버 변수, 속성
    def __init__(self,name,age):
        #self는 자기자신을 의미
        #self는 생성될때 할당받은 메모리 공간
        self.name=name
        self.age=age
        print(f"{self.name}가 생성되었어요!")

    def bark(self):
        #self를 통해 각 개체가 가지고있는 데이터에 따라 서로 다르게 동작할 수있다.
        print(f"{self.name}가 짖습니다.멍멍")

#생성자를 통해 내가 정의한 클래스의 객체(인스턴스)를 생성할 수 있다.
Puppy1=Puppy("초코",5)
Puppy2=Puppy("뽀삐",5)
#class 비유
#class는 설계도(틀)이다. -붕어빵 틀이다.
#그 클래스로 생성된것은 객체(인스턴스)이다. -붕어빵이다.

#객체(인스턴스).bark()
Puppy1.bark()
Puppy2.bark()

# 직접 car클래스를 정의해주세요
# 저장하는 데이터는 model,price
# 내부에 drive라는 함수를 정의해주세요
# {모델명}이 주행을 시작합니다! 출력

class Car:
    #생성자 정의-Car()호출시 호출됨
    def __init__(self,model,price):
        self.model=model
        self.price=price

    def drive(self):
        print(f"{self.model}가 주행을 시작합니다!")

car1=Car("소나타",2400)
car2=Car("산타페",4000)
car1.drive()
car2.drive()