from django.contrib import admin
from.models import User
from.models import Tweet
from.models import Follow
from.models import Like
from.models import Comment


admin.site.register(User)
admin.site.register(Tweet)
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Comment)

# Register your models here.
