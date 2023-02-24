from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from .models import Member
import requests


class PrivatePostList(ListView):
    model = Member
    paginate_by = 10
    context_object_name = 'users'
    template_name = 'member_list.html'

    # def get_queryset(self):
    #     """
    #     Список наших объектов будет состоять лишь из приватных и не удаленных статей
    #     """
    #     return Member.objects


class MemberListView(ListView):
    paginate_by = 10
    model = Member
    ordering = ['name']

    def addMember(request, pk):
        user = get_object_or_404(Member,pk=pk)
        data = {
        'id': user.id,
        'name': f'{user.name} Приветсвую!',
        'lastname':user.lastname,
        'age': user.age
    }
        requests.post('http://127.0.0.1:5000/addmember', data=data)
        return HttpResponseRedirect('/')



