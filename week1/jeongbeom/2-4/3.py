#문제8
words = input().upper()
word_list = list(set(words))
cnt_list = []

for i in word_list :
    cnt = words.count(i)
    cnt_list.append(cnt)

max_cnt = cnt_list.count(max(cnt_list))
if max_cnt >= 2 :
    print("?")
    
else :
    print(word_list[cnt_list.index(max(cnt_list))])
