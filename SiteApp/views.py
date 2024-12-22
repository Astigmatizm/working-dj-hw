from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages


class index()


# def show_request_params(request):
#     get_params = request.GET
#     post_params = request.POST
#
#     get_params_str = ', '.join([f"{key}: {value}" for key, value in get_params.items()]) # метод items() позволяет получить все ключи и значения в параметрах запроса.
#
#     post_params_str = ', '.join([f"{key}: {value}" for key, value in post_params.items()])
#
#     response_content = f"""
#     <html>
#         <body>
#             <h2>GET Parameters:</h2>
#             <p>{get_params_str if get_params else "Нету GET параметр"}</p>
#             <h2>POST Parameters:</h2>
#             <p>{post_params_str if post_params else "Нету POST параметр"}</p>
#         </body>
#     </html>
#     """
#
#     return HttpResponse(response_content)


def is_login(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'SiteApp/login.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'admin' and password == 'password':
            return HttpResponseRedirect(reverse('profile'))
        else:
            return HttpResponseRedirect(reverse('login') + '?error=1')

    return render(request, 'login.html')


def profile_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    return render(request, 'profile.html')