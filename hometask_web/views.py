from django import views
from django.shortcuts import render_to_response

from hometask_web.mappers import PCMapper, AdapterMapper


class PCView(views.View):
    def get(self, request):
        pc = PCMapper().select()
        return render_to_response("pc_list.html", {"pcs": pc})


def adapters(request):
    pc = AdapterMapper().select()
    return render_to_response("adapters_list.html", {"adapters": pc})
