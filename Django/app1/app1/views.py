from django.shortcuts import render
from rest_framework.views import APIView
from instagram.models import Feed


class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()
        return render(request, 'app1/main.html', context=dict(feed_list=feed_list))