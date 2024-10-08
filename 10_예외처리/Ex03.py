'''
Created on 2024. 8. 8.

@author: user
'''

def load_books():
    try:
        with open('file.txt', 'r', encoding='utf-8') as file:
            books = [line.strip() for line in file.readlines()]
        return books
    except FileNotFoundError:
        return []


def save_books(bookList):
    with open('file.txt', 'w', encoding='utf-8') as file:
        for book in bookList:
            file.write(book + '\n')

bookList = load_books()

while True:
    print('----Menu Select----')
    print('1. 전체 조회')
    print('2. 추가')
    print('3. 수정')
    print('4. 삭제')
    print('0. 종료')
    
    try: 
        menu = int(input('번호 선택: '))
        
        if menu == 1:
            print('1. 전체 조회')
            print('제목    가격')
            for book in bookList:
                title, price = book.split(',')
                print(f'{title}      {price}')
        
        elif menu == 2:
            print('2. 추가')
            while True:
                title = input('제목: ')
                if len(title) > 5:
                    print('제목 5글자 이상 입력됨')
                else:
                    break
            while True:
                try:
                    price = int(input('가격: '))
                    break
                except ValueError:
                    print('가격은 숫자로 입력하세요')
            bookList.append(f'{title},{price}')
        
        elif menu == 3:
            print('3. 수정')
            while True:
                title = input('제목: ')
                if len(title) > 5:
                    print('제목 5글자 이상 입력됨')
                else:
                    break
            found = False
            for i, book in enumerate(bookList):
                book_title, book_price = book.split(',')
                if book_title == title:
                    while True:
                        try:
                            new_price = int(input('수정할 가격: '))
                            break
                        except ValueError:
                            print('가격은 숫자로 입력하세요')
                    bookList[i] = f'{title},{new_price}'
                    found = True
                    print('찾음')
                    break
            if not found:
                print('못찾음')
        
        elif menu == 4:
            print('4. 삭제')
            title = input('삭제할 제목: ')
            found = False
            for i, book in enumerate(bookList):
                book_title, book_price = book.split(',')
                if book_title == title:
                    del bookList[i]
                    found = True
                    print('찾음')
                    break
            if not found:
                print('못찾음')
        
        elif menu == 0:
            print('0. 종료')
            save_books(bookList)
            break
        
        else:
            print('잘못 입력')
    
    except ValueError:
        print('숫자로 입력하세요')
