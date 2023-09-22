# 실제로 실무에서 match 사용되는 패턴 (공식문서)
valid = re.compile(r"^[a2-9tjqk]{5}$")

def displaymatch(match):
    if match is None:
        return None
    return '' % (match.group(), match.groups())

displaymatch(valid.match("akt5q"))
     