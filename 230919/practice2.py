import datetime
dt = datetime.datetime.now()   #함수는 () 사용해야함
print(dt)

age = input("생년월일(19951031) 형태로 본인의 생년월일을 입력하시오")
year = age[:4]
month = age[4:6]
day = age[6:]

year_diff = dt.year - year
month_diff = dt.month - month
day_diff = dt.day - day

if day_diff < 0 :  # 일 내림 처리
    month_diff -= 1
if month_diff < 0 : # 월 내림 처리
    year_diff -= 1
print("당신의 나이는", year_diff + 1)

if year_diff < 18 :
    print("당신은 미성년자입니다.")
else :
    print("당신은 미성년자가 아닙니다.")