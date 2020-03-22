import requests
from django.contrib import admin
from django.contrib.auth import get_permission_codename

from .models import Comment
# Register your models here.
PERMISSION_API = "http://permission.sso.com/has_perm?user={}&perm_code={}"
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target','content','wesite','created_time')


    
    #def has_add_permission(self, request):
        #opts = self.opts
        #codename = get_permission_codename('add', opts)
        #perm_code = "%s.%s" % (opts.app_label, codename)
        #resp = requests.get(PERMISSION_API.format(request.user.username, perm_code))
        
       # if resp.status_code == 200:
        #    return True
        #else:
          #  return False