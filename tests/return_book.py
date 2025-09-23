import pytest
from library_service import (
    return_book_by_patron
)

# positive
def test_return_book_borrowed():
    """Test returning book that was borrowed by the patron."""
    success, message = return_book_by_patron("654321", 1)
    
    assert success == True
    assert "successfully returned" in message.lower()

# negative
def test_return_book_not_borrowed():
    """Test returning book that was not borrowed by the patron."""
    success, message = return_book_by_patron("123456", 2)
    
    
    assert success == False
    assert "not borrowed" in message.lower()


# positive
def test_return_book_update_available_copies():
    """Test returning book and updating available copies."""
    success, message = return_book_by_patron("930140", 3)
    
    assert success == True
    assert "successfully returned" in message.lower()

# positive
def test_return_book_calculate_late_fees():
    """Test returning book and calculate late fees."""
    success, message = return_book_by_patron("341383", 4)
    
    assert success == True
    assert "successfully returned" in message.lower()

# negative
def test_return_book_patron_does_not_exist():
    """Test returning book with a patron that doesnt exist."""
    success, message = return_book_by_patron("931943", 5)
    
    
    assert success == False
    assert "does not exist" in message.lower()












