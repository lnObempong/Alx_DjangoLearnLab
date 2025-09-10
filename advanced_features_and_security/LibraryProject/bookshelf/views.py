# LibraryProject/bookshelf/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Category


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        isbn = request.POST.get("isbn")
        category_id = request.POST.get("category")
        category = Category.objects.get(id=category_id) if category_id else None

        Book.objects.create(title=title, author=author, isbn=isbn, category=category)
        return redirect("book_list")

    categories = Category.objects.all()
    return render(request, "bookshelf/book_form.html", {"categories": categories})


@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.isbn = request.POST.get("isbn")
        category_id = request.POST.get("category")
        book.category = Category.objects.get(id=category_id) if category_id else None
        book.save()
        return redirect("book_list")

    categories = Category.objects.all()
    return render(request, "bookshelf/book_form.html", {"book": book, "categories": categories})


@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")

    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
