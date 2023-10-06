from django.shortcuts import render

def postlist(request):
    return render(request, 'blog/postlist.html')

def postdetail(request):
    return render(request, 'blog/postdetail.html')

def write(request):
    return render(request, 'blog/write.html')

def edit(request):
    return render(request, 'blog/edit.html')

def delete(request):
    return render(request, 'blog/delete.html')

def new_comment(request):
    return render(request, 'blog/new_comment.html')

def update_comment(request):
    return render(request, 'blog/update_comment.html')

def delete_comment(request):
    return render(request, 'blog/delete_comment.html')

def category_page(request):
    return render(request, 'blog/category_page.html')

def tag_page(request):
    return render(request, 'blog/tag_page.html')

# Create your views here.
