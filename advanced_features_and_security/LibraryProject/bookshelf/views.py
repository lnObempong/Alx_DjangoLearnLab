# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book, Category
from .forms import BookForm

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Safe filtering using Django ORM, validated parameters
    q = request.GET.get("q", "").strip()
    if q:
        # ORM parameterization prevents SQL injection
        books = Book.objects.filter(title__icontains=q)
    else:
        books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books, "q": q})


@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Create"})


@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/form_example.html", {"form": form, "action": "Edit", "book": book})


@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
