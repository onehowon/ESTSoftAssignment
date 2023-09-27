from collections import deque

def solution(cacheSize, cities):
    # 캐시 사이즈가 0일 경우 예외처리
    if cacheSize == 0:
        return len(cities)*5
    
    t,cache = 0,deque()
    for i in cities:
        # 대소문자를 구별하지 않는다는 조건
        i = i.lower()
        
        if i in cache:
            t += 1
            cache.remove(i)
            cache.append(i)
        else:
            t += 5
            cache.append(i)
            # 캐시사이즈보다 캐시가 많다면 맨 앞에것 제거
            if cacheSize < len(cache):
                cache.popleft()
                
    return t