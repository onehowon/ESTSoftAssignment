like = ['볶음밥', '라면', '국수', '파스타', '치킨', '짜장면', '국밥']
dislike = ['국밥', '짬뽕', '찜닭', '파스타', '국수', '카레', '덮밥']

combined = list(set(like+dislike))

print(combined)

final_menu = []

for menu in like:
    if menu not in dislike:
        final_menu.append(menu)

print(final_menu)