with open('books.txt') as f:
    books = f.readlines()
    for line in books:
        print(line.strip())
