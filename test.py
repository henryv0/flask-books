def validateBook(bookObject):
    if (
        "name" in bookObject 
        and "price" in bookObject
        and "isbn" in bookObject
    ):
        return True
    else:
        return False

#  Test cases

valid_object = {
    'name': 'Valid book',
    'price': 9.95,
    'isbn': 123456,
}

missing_name = {
    'price': 9.95,
    'isbn': 123456,
}

missing_price = {
    'name': 'Book 1',
    'isbn': 123456,
}

missing_isbn = {
    'name': 'Book 1',
    'price': 9.95,
}