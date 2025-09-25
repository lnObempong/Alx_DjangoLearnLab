from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# --- BOOK GENERIC VIEWS ---

# 1. List all books
class BookListView(generics.ListAPIView):
    """
    GET /books/ → List all books
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # open for read
    search_fields = ["title", "author__name"] 


# 2. Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/ → Retrieve details of a single book
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# 3. Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/ → Create a new book
    Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # restrict


# 4. Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<id>/update/ → Update a book
    PATCH /books/<id>/update/ → Partially update
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# 5. Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete/ → Delete a book
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
