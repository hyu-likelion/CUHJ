#문제5
def solution(participant : list, completion : list) -> str :
    for runner in completion :
        if runner in participant :
            participant.remove(runner)
        else :
            continue
    return participant[0]
