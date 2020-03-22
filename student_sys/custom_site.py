from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Student_sys'
    site_title = 'Student_sys 管理后台'
    index_title = '首页'
    
custom_site = CustomSite(name = 'cus_admin')

    