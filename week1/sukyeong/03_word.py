word = input()


def most_used_word():
    word_list = list(word.upper())
    word_ranking = []  # 순위를 매길 문자를 저장하는 리스트
    num_list = []  # 문자의 개수만 모아놓은 리스트

    # 중복되는 숫자가 없도록 순위 매길 문자 리스트 만드는 반복문
    for i in range(len(word_list)):
        if word_list[i] not in word_ranking:
            word_ranking.append(word_list[i])

    # 각 문자들의 개수를 세서 리스트에 저장하는 반복문
    # count 함수 써서 바꿔보기
    for i in range(len(word_ranking)):
        count = 0
        for j in range(len(word_list)):
            if word_ranking[i] in word_list[j]:
                count += 1
        word_ranking[i] = [word_ranking[i], count]
        num_list.append(count)

    highest_number = max(num_list)
    answer = word_ranking[num_list.index(highest_number)][0]
    num_list.remove(highest_number)

    if highest_number in num_list:
        print('?')
    else:
        print(answer)

most_used_word()