from django.contrib import admin
from django.urls import path
from blog.views import index, a, b, c, d, e, about, blogdetails


# path(url, url 연결 함수)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('a/', a),
    path('b/', b),
    path('c/', c),
    path('d/', d),
    path('e/', e),
    path('about/', about),
    # path('blogdetails/<int:pk>', blogdetails),
    # path('blogdetails/<str:s>', blogdetails),
]

def blogdetails(request, s): # urls.py에서 pk로 해주었으면 pk, s로 해주었으면 s
    print(s)
    return render(request, 'blog/blogdetails.html')