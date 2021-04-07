#입력받
import re
def solution(new_id : str) -> str :
    answer = ''

#1단계
    new_id = new_id.lower()

#2단계
    new_id= re.sub('[=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', new_id)

#3단계 점 합치
    for i in range(len(new_id)) :
        if ".." in new_id :
            new_id = new_id.replace("..", ".")     


#4단계 앞뒤에 점 지우기
    if new_id[0] == "." and new_id[-1] == "." :
        new_id = new_id[1:]
        new_id = new_id[:-1]
    elif new_id[0] == "." :
        new_id = new_id[1:]    
    elif new_id[-1] == "." :
        new_id = new_id[:-1]
    else :
        pass


#5단계
    if new_id == "" :
        new_id = "a"

#6단계
    if len(new_id) >= 16 :
        new_id = new_id[0:15]
        if new_id[-1] == "." :
            new_id = new_id[:-1]

#7단계
    while len(new_id) <=2 :
        new_id = new_id + new_id[-1]
    answer = new_id
    return answer
        
        


