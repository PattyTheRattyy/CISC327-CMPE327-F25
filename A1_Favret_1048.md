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
