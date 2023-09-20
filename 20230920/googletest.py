def maximize(pots):
    if not pots: return 0

    # A가 먼저 좌측을 선택할 경우
    choose_leftmost = pots[0]

    # B는 최적의 선택을 하므로 그 다음 A가 B이후에 가질 수 있는 값은
    # -> B가 좌측을 선택하고 남은 항아리들의 maximize값
    # -> B가 우측을 선택하고 남은 항아리들의 maximize값
    # 위 둘 중 작은 값을 가져야만 한다.
    # 왜냐하면 B가 최선의 선택을 하기 때문에 A는 둘 중에 작은 값을 가질 수 밖에 없다.
    next_choose_left = maximize(pots[2:])       # a가 좌측, b가 좌측선택
    next_choose_right = maximize(pots[1:-1])    # a가 좌측, b가 우측선택
    next_value = min(next_choose_left, next_choose_right)

    # 두 값을 더한다.
    left_case = choose_leftmost + next_value

    # 이번에는 A가 우측을 선택할 경우
    choose_rightmost = pots[-1]

    # 위와 마찬가지 경우이므로 설명 생략
    next_choose_left = maximize(pots[1:-1])     # a가 우측, b가 좌측
    next_choose_right = maximize(pots[0:-2])    # a가 우측, b가 우측
    next_value = min(next_choose_left, next_choose_right)

    # 두 값을 더한다.
    right_case = choose_rightmost + next_value

    # 최종적으로 둘중에 큰값을 리턴한다.
    return max(left_case, right_case)


print(maximize([9,8,7,5,4,6,3,1,2]))
print(maximize([1,3,4,5,1]))