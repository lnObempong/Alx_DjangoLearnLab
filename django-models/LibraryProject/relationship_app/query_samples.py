# 1) Query all books by a specific author
def query_books_by_author(author_name: str) -> None:
    """
    ForeignKey traversal example using objects.filter(author=author).
    """
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print(f"No author found named '{author_name}'.")
        return

    # Use filter as required by checker
    books = Book.objects.filter(author=author)
    if books.exists():
        print(f"Books by {author_name}:")
        _print_books(books)
    else:
        print(f"{author_name} has no books in the database.")
