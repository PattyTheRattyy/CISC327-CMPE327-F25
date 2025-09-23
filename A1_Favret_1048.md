Name: Patrick Favret
ID: 20351048
Group/Section: 001

# Report your findings in a table with columns function name, implementation status (complete/partial), what is missing (if any)

| function name               | implementation status | what is missing                                                                                                                                  |
| --------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| add_book_to_catalog         | complete              | N/A                                                                                                                                              |
| borrow_book_by_patron       | partial               | checks if current_borrowed > 5 but it should check if current_borrowed >= 5, otherwise complete                                                  |
| return_book_by_patron       | partial               | verify the book was borrowed by the patron, update available copies, display late fees                                                           |
| calculate_late_fee_for_book | partial               | calculate late fees, return JSON response with fee amount and days overdue                                                                       |
| search_books_in_catalog     | partial               | provide search functionality for books, support partial matching for title/author and exact matching for ISBN, return results in catalog display |
| get_patron_status_report    | partial               | display patron status with currently borrowed books and their due dates, late fees, number of currently borrowed books, and borrowing history    |
|                             |                       |                                                                                                                                                  |
|                             |                       |                                                                                                                                                  |
|                             |                       |                                                                                                                                                  |
|                             |                       |                                                                                                                                                  |
|                             |                       |                                                                                                                                                  |
|                             |                       |                                                                                                                                                  |
|                             |                       |                                                                                                                                                  |
|                             |                       |                                                                                                                                                  |

# Summary of Test Scripts:

### add_book.py:

- 2 positive tests
- 3 negative tests
- tests with valid inputs twice
- test with short ISBN
- test with too long of a title
- test without total copies

### borrow_book.py:

- 2 positive tests
- 3 negative tests
- tests with valid inputs twice
- test when patron has too many borrowed books
- test when book does not exist
- test when book has no available copies

### calculate_late_fee.py:

- 3 positive tests
- 2 negative tests
- tests with valid inputs and differing amounts of lateness
- test where book was not actually borrowed
- test where book does not exist

### get_patron_status.py:

- 3 positive tests
- 2 negative tests
- tests patron that has never borrowed
- tests patron that has no fees
- tests patron that has fees
- tests with patron ID that does not exist
- tests with an invalid format for the patron ID

### return_book.py:

- 3 positive tests
- 2 negative tests
- tests returning a book that was borrowed
- tests returning a book that was not borrowed
- tests returning a book and updating available copies
- tests returning a book and calculating late fees
- tests returning a book by a patron that does not exist

### search_books.py:

- 3 positive tests
- 2 negative tests
- tests search with exact ISBN
- tests search for book that does not exist
- tests search with invalid format
- tests search with partial title
- tests search with partial author
