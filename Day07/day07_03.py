import random

# 미니 로또
#6개 중복없는 숫자
#6개:1등,5개:2등,4개:3등,꽝


#1. 당첨번호 뽑기
winning_nums=[]
while True:
    random_num= random.randint(1,45)
    if random_num in winning_nums:
        continue #중복때문에 for 대신 while 사용

    winning_nums.append(random_num)
    #6개 뽑으면 탈출
    if len(winning_nums) ==6:
        break
print(f"이번회차 당첨번호:{winning_nums}")

#2. 번호6개 찍기-중복x
my_nums=[]
while True:
   print(f"현재내가 뽑은 번호{my_nums}")
   my_num=input("1~45 사이 번호 입력>>")
   if not my_num.isdecimal():
       print("숫자를 입력하세요!")
       continue
   my_num=int(my_num)
   if not (1<=my_num<=45):
       print("1~45사이값을 입력하세요!")
       continue

   #중복확인,중복아니면 추가
   if my_num not in my_nums:
       my_nums.append(my_num)

   #6개 찍으면 탈출
   if len(my_nums) ==6:
       print(f"현재내가 뽑은 번호{my_nums}")
       break
#6개:1등,5개:2등,4개:3등,꽝
#3. 두개 비교하기
#맞춘횟수 변수를 만들어서 두 리스트를 비교해서
#같은값이 있으면 +1

winning_count=0

#for my_num in my_nums:
#    if my_num in winning_nums:
#        for winning_num in winning_nums:
#            if my_num==winning_num:
#               winning_count+=1

for my_num in my_nums:
    if my_num in winning_nums:
        winning_count+=1

if winning_count==6:
    print("1등")
if winning_count==5:
    print("2등")
if winning_count==4:
    print("3등")
else:
    print("꽝")



