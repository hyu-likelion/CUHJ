participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]


def solution(participant, completion):
    answer = ''
    for i in range(len(completion)):
        participant.remove(completion[i])
    answer = participant[0]
    return answer


print(solution(participant, completion))
