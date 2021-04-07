import re

def solution(new_id):
    new_id = new_id.lower()  # 1단계
    new_id = re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', new_id)

    new_id = new_id.split(".")
    new_id = list(filter(None,new_id))
    new_id = ".".join(new_id)

    if new_id == '' :
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == "." :
            new_id = new_id[:14]

    if len(new_id) <= 2:
        new_id = list(new_id)
        word = new_id[-1]
        while len(new_id) != 3:
            new_id.append(word)
        new_id = "".join(new_id)



    return new_id

print(solution("abcdefghijklmn.p"))
