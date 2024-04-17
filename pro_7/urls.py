from django.urls import path
from .import views
urlpatterns=[
    path('fun',views.fun,name='fun'),
    path('',views.fun_1,name='fun_1'),
    path('teacherr_views',views.teacherr_views,name='teacherr_views'),
    path('teacherr_edit/<int:id1>',views.teacherr_edit,name='teacherr_edit'),
    path('teacherr_delete/<int:id1>',views.teacherr_delete,name='teacherr_delete'),
    path('search',views.search,name='search'),
    path('teacherr_login',views.teacherr_login,name='teacherr_login'),
    path('user_home',views.user_home,name='user_home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('logt',views.logt,name='logt'),
    path('profile_edit',views.profile_edit,name='profile_edit'),
    path('fun_2',views.fun_2,name='fun_2'),
    path('fun_3',views.fun_3,name='fun_2'),
    # path('view',views.view,name='view'),
    # path('edits/<int:id1>',views.edits,name='edits'),


]