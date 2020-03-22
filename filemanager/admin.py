import requests
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.auth import get_permission_codename

PERMISSION_API = "http://permission.sso.com/has_perm?user={}&perm_code={}"

from .models import Post, Category, Tag, Rate

class PostInline(admin.TabularInline):
    fields = ('title','desc')
    extra = 1
    model = Post

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","status","is_nav","created_time","intro")
    fields = ("name","status","is_nav","intro")
    inlines = [PostInline, ]
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form,change)
    def post_count(self,obj):
        return obj.post_set.count()
    
    post_count.short_description = '文章数量'
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name","status","created_time","intro")
    fields = ('name','status','intro')
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
            'title','category','status',
            'created_time', 'operator','rate',
            ]
    list_display_links = []
    
    list_filter = ['category','tag','created_time','rate']
    search_fields = ['title', 'category_name','tag_name']
    
    actions_on_top = True
    actions_on_bottom = True
    #编辑页面
    save_one_top = True
    
    fields = (
            ('category', 'title'),
            'desc',
            'status',
            'content',
            'tag',
            'rate',
            )
    def operator(self, obj):
        return format_html(
                '<a href="{}">编辑</a>',
                reverse('admin:filemanager_post_change',args=(obj.id,))
                )
    operator.short_description = '操作'
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)
    
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ("name","status","created_time","score")
    fields = ('name','status','score')
    inlines = [PostInline, ]
    
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(RateAdmin, self).save_model(request, obj, form, change)
    #def has_add_permission(self, request):
        #opts = self.opts
        #codename = get_permission_codename('add', opts)
        #perm_code = "%s.%s" % (opts.app_label, codename)
        #resp = requests.get(PERMISSION_API.format(request.user.username, perm_code))
        
        #if resp.status_code == 200:
            #return True
        #else:
            #return False
        
        
    
