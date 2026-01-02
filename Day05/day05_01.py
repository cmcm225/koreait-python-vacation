#반복문-for
"""
for 변수 in  전체:
    반복실행될 코드
전체-> 컬렉션 자료형, 문자열, range() 등...
반복마다 하나씩 가져올수있는 구조면 가능 (__inter__)

변수 -> 순서재로 대입받는 변수(for문 내에서 사용)
"""
print("Hello")
print("") #enter키가 자동 포함
print("world")
print("hello,",end=" ") # 출력끝에 enter대신 ""가 포함

print()
nums=[0,1,2,3,4]
for num in nums:
    print(num, end=" ")

print()

# range(a,b)-> a이상 b미만 [
# ex) range(1,5) -> [1,2,3,4]
# range(n) == range(0,n)->0 이상 n 미만
nums= list(range(5)) #리스트로 쓰려면 형변환
print(nums)

#range(10)->[0,1,2,...,9]
for num in range(10):
    print(num, end=" ")

for _ in range(5): #요소가 필요없으면 "_" 로 표현(관행)
    print("hello world")

# 1~50까지 홀수는 홀수끼리 짝수는 짝수끼리 나누어 담기
odds, evens=[], [] # 튜플 언패킹
for num in range(1,51):
    if num%2==0:
        evens.append(num) # evens 에 num 추가
    else:
        odds.append(num)
print(odds)
print(evens)

#1~50 홀수는 홀수끼리, 짝수는 짝수끼리 더하여서 각각 출력
#total_sum=0 # 누적변수에 초기값 대입
#for num in range(1,51):
 #   total_sum= total_sum+num

#print(total_sum) #1~50 누적합

even_sum, odd_sum=0,0 #누적변수 초기화
for num in range(1,51):
    if num%2==0:
        even_sum = even_sum + num
    else:
        odd_sum = odd_sum + num

print (f"짝수합:{even_sum},홀수합:{odd_sum}")

names= ["김지수","김길동","박철호","박화목","최영희"]
#박 성씨인 이름들만 모으기
parks=[]
count=0
for name in names:
    #내부적으로 name=names[0]
    #name= name[1],....
    if name.startswith("박"): #if name[0] =="박": 과 같음
        parks.append(name)
        count = count + 1
print(parks)
#박 성씨인 이름이 몇개인지 출력
print(count)

files=["report.pdf","ad.exe","setup.bat","memo.txt"]
#for문으로 파일명을 확인하면서 .exe파일로 끝나면, "위험한 파일입니다!" 출력
#endswith() 사용
for file in files:
    if file.endswith(".exe"):
        print("위험한 파일입니다!")
#banned_files에 기록되어있는 확정자로 끝나면 "위험한 파일입니다!" 출력
banned_files= [".exe",".bat"]

for file in files:
    # "."의  index를 찾는다
    dot_idx= file.index(".")
    #.부터 끝까지 슬라이싱
    ext=file[dot_idx:]
    #in 연산자로  banned_files에 있는지 확인
    if ext in banned_files:
        print("위험한 파일입니다!")
    #있으면 출력

# 2중 for문
# 바깥 반복 한번당 안쪽 반복 전체가 도는 구조

#일주일
for day in range(1,8):
    print(f"{day}일 살았습니다!", end=" ")
# 한달
for week in range(1,5):
    print(f"{week}주 시작")
    #일주일 코드 #4번 반복
    for day in range(1, 8):
        print(f"{day}일 살았습니다!", end=" ") # 4x7=28번 반복
    print() #엔터
    print(f"{week}주 끝") # 4번 반복

#구구단(2단~9단)
"""
2단시작!
2x1=2
2x2=2
...
2x9=18
2단끝!
3단 시작!
3x1=3
3x2=3
...
3x9=27
3단 끝!
...9단 끝!
"""
#2단
#for num in range(1,10):
#   print(f"2x{num}={2*num}"
#3단
#for num in range(1,10):
#   print(f"3x{num}={3*num}"
#4단
#for num in range(1,10):
#   print(f"4x{num}={4*num}"


for dan in range(2,10):
    print(f"{dan}단 시작!")
    for num in range(1,10):
        print(f"{dan}x{num}={dan*num}")
    print(f"{dan}단 끝!")

