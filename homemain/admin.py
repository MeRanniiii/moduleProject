from django.contrib import admin
from accounts.models import Users
from board.models import NoticeBoardPost,Comment


# Register your models here.
admin.site.register(Users)
admin.site.register(NoticeBoardPost)
admin.site.register(Comment)