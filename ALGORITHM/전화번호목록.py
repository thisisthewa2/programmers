def solution(phone_book):
    phone_book = set(phone_book)
    for number in phone_book:
        for i in range(1,len(number)):
            if number[:i] in phone_book:
                return False  
    return True
