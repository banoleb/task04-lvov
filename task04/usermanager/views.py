from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

User = get_user_model()


@login_required
def showall(request):

    all_users = User.objects.order_by('id')
    str = request.GET.get('sorted', None)
    sort_list = ['id', 'username', 'is_active']
    if request.method == 'GET' and str is not None:
        selected = sort_list[int(str)]
        all_users = User.objects.order_by(selected)
        print(str)
    context = {
        'form': all_users,
    }

    if request.method == 'POST':
        users = request.POST.getlist('users')
        # print(users)
        final_str = ""
        current_user = request.user
        print(current_user.username)
        for i in users:
            final_str = final_str + i + ", "
        if len(users) == 0:
            messages.error(request, 'Select one ore more users')
            return redirect("/app")
        elif 'block' in request.POST:
            User.objects.filter(username__in=users).update(is_active = False)
            if current_user.username in users:
                logout(request)
                messages.success(request,
                                 'You have Blocked yourself successfully.')
            else:
                messages.success(request,
                                 f'You have Blocked {final_str} successfully.')
            return redirect("/app")
        elif 'unblock' in request.POST:
            User.objects.filter(username__in=users).update(is_active = True)
            messages.success(request,
                             f'You have Unblocked {final_str}  successfully.')
            return redirect("/app")
        elif "delete" in request.POST:
            User.objects.filter(username__in=users).delete()
            messages.success(request,
                             f'You have Delete {final_str}  successfully.')
            return redirect("/app")
        else:
            return redirect("/app")
    return render(request, 'manager/index.html', context)


def redir(req):
    return redirect("/app")
