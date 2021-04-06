phone_book = ["123", "456", "789"]
phone_length = []
new_phone_book = []

def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        phone_length.append(len(phone_book[i]))

    for j in range(len(phone_book)):
        new_phone_book.append(phone_book[j][:min(phone_length)])
    print(new_phone_book)

    if len(new_phone_book) != len(set(new_phone_book)):
        answer = False

    return answer

print(solution(phone_book))
