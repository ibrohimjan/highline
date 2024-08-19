from django.shortcuts import render
from django.views.generic import View

from common.models import HomeVideo


class HomeView(View):
    def get(self, request):
        video = HomeVideo.objects.last()

        context = {
                "video": video,
                }

        return render(request, "index.html", context)

