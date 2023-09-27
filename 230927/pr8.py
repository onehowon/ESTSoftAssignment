from collections import Counter

def solution(스테이지수, 스테이지):
  전체인원 = len(스테이지)
  스테이지에_머물고_있는_사람 = Counter(스테이지) # Counter 사용하여 각 스테이지 플레이어 리스트 수 카운트한 딕셔너리 '스테이지 머물고 있는 사람' 생성

  answer = {} # 딕셔너리 초기화
  for i in range(1, 스테이지수+1): # 스테이지 번호를 키로 사용하고, 실패율을 값으로 저장
    answer[i] = 0 # 초기화할 때 모든 스테이지의 실패율을 0으로 설정

  for i in answer: # 스테이지 수를 1부터 반복하면서 각 스테이지 실패율 계산, 실패율은 해당 스테이지에 머물러 있는 플레이어 수를 전체 인원으로 나눈 값
    answer[i] = 스테이지에_머물고_있는_사람[i]/전체인원 # 실패율 계산 이후 해당 스테이지에 머물러 있는 플레이어 수를 전체인원에서 빼줌
    전체인원 -= 스테이지에_머물고_있는_사람[i]

  return sorted(answer, key=lambda x: answer[x], reverse=True) # answer를 실패율 기준으로 내림차순 정렬

n,stages = (5,[2,1,2,6,2,4,3,3])
print(solution(n,stages))