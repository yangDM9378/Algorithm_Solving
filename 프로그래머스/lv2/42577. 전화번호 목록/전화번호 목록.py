def solution(phone_book):
    phone_book = sorted(phone_book) 
    for j in range(len(phone_book)-1):
        if phone_book[j] == phone_book[j+1][0:len(phone_book[j])]:
            return False
    return True