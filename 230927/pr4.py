# 카카오 공채 5번

def solution(n,t,m,timetable):
  timetable = sorted([int(i[:2]) * 60 + int(i[3:]) for i in timetable]) # 시간을 기준으로 정렬, 시간을 분 단위로 변환하여 정렬합니다.

  콘의출근시간 = 540 # 9시 = 60 * 9 = 540분
  출근한사람들 = []
  셔틀버스시간 = 540 # 첫 출발 시간 09:00

  for i in range(n): # n 번의 셔틀 운행 시뮬레이션
    for j in range(m): #  m 명의 승객을 태우려고 시도
      if timetable and timetable[0] <= 셔틀버스시간: # 셔틀 버스가 도착한 시간보다 이른 시간대에 대기 중인 승객을 태우려고 시도
        콘의출근시간 = timetable.pop(0) - 1 # timetable list에서 승객을 하나씩 꺼내 콘의 출근 시간을 업데이트
      else:
        콘의출근시간 = 셔틀버스시간
    셔틀버스시간 += t # 셔틀버스의 출발 시간을 업데이트. 각 셔틀 버스 간격은 't'분

  return f'{str(콘의출근시간//60).zfill(2)}:{str(콘의출근시간%60).zfill(2)}' # 마지막 셔틀 운행이 끝난 후 콘의 출근 시간과 분을 변환하여 반환


testcase = [
    (1,1,5,['08:00', '08:01', '08:02', '08:03']), # 셔틀운행 횟수(n)은 1, 운행간격(t)은 1 최대 승객수(m)은 5
     (2,10,2,['09:10','09:09','08:00', '09:10']),
      (1,2,1,['09:00','09:00','09:00','09:00'])
      ]

for n, t, m, timetable in testcase:
    print(solution(n,t,m,timetable))