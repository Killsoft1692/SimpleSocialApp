import channels.layers
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .models import Group


class IndexView(View):
    def get(self, request):
        qs = Group.objects.all()
        for group in qs:
            group.like_count = group.likes.count()
            if request.user in group.likes.all():
                group.is_liked = True
            else:
                group.is_liked = False

        return render_to_response('groups/index.html', {'objects': qs})


class LikeView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        group_id = request.POST.get('group_id')
        user_id = request.POST.get('user_id')

        obj = Group.objects.get(pk=group_id)
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                user = request.user
        else:
            user = request.user

        if user in obj.likes.all():
            obj.likes.remove(user)
        else:
            obj.likes.add(user)

        like_count = obj.likes.count()

        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.group_send)('likes', {'type': 'send_likes_number', 'group_id': group_id,
                                                          'likes_number': like_count})

        return JsonResponse({'ok': True})
