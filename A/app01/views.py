from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, requeste):
        return render(requeste,"index.html")

