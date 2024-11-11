"""
URL configuration for USED_STUDY_MATERIAL project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from MATERIAL import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('logout/',views.logout),

    path('change_password/',views.change_password),
    path('change_password_post/',views.change_password_post),
    path('forget_password/',views.forget_password),
    path('forget_password_post/',views.forget_password_post),
    path('institution_type/', views.institution_type),
    path('type_add_post/',views.type_add_post),
    path('view_type/',views.view_type),
    path('serch_type/',views.serch_type),
    path('type_edit/<id>',views.type_edit),
    path('type_edit_post/',views.type_edit_post),
    path('type_delete/<id>', views.type_delete),
    path('add_category/',views.add_category),
    path('add_category_post/',views.add_category_post),
    path('view_category/<id>',views.view_category),
    path('delete_category/<id>',views.delete_category),
    path('edit_category/<id>',views.edit_category),
    path('edit_post/',views.edit_post),
    path('search_view_category/',views.search_view_category),
    path('view_user/',views.view_user),
    path('search_user/',views.search_user),
    path('search_feedback/',views.search_feedback),
    path('view_feedback/',views.view_feedback),
    path('search_feedback/',views.search_feedback),
    path('view_complaints/',views.view_complaints),
    path('search_complaints/',views.search_complaints),
    path('reply/<id>',views.reply),
    path('reply_post/',views.reply_post),
    path('admin_home/',views.admin_home),
#=====user============

    path('user_register/',views.user_register),
    path('user_register_post/',views.user_register_post),
    path('user_profile/',views.user_profile),
    path('user_edit_profile/',views.user_edit_profile),
    path('user_editprofile_post/',views.user_editprofile_post),
    path('user_change_password/',views.user_change_password),
    path('user_change_password_post/',views.user_change_password_post),
    path('user_view_Type/',views.user_view_Type),
    path('user_view_Type_post/',views.user_view_Type_post),
    path('user_view_category/<id>',views.user_view_category),
    path("user_search_category/",views.user_search_category),
    path('user_manage_material/',views.user_manage_material),
    path('search_user_manage_material/',views.search_user_manage_material),
    path('user_add_material/',views.user_add_material),
    path('user_add_materials_post/',views.user_add_materials_post),
    path('user_update_material/<id>',views.user_update_material),
    path('user_update_materials_post/',views.user_update_materials_post),
    path('delete_material/<id>',views.delete_material),
    path('user_my_request/',views.user_my_request),
    path('search_user_my_request/',views.search_user_my_request),
    path('user_my_request_send/',views.user_my_request_send),
    path('search_user_my_request_send/',views.search_user_my_request_send),
    path('user_p_manage_request/<id>',views.user_p_manage_request),
    # path('user_p_manage_request/',views.user_p_manage_request),
    path('search_user_p_manage_request/',views.search_user_p_manage_request),
    path('approve_manage/',views.approve_manage),
    path('user_p_request_approve/',views.user_p_request_approve),
    path('approve/<id>',views.approve),
    path('search_user_p_request_approve/',views.search_user_p_request_approve),
    path('user_p_request_reject/',views.user_p_request_reject),
    path('reject/<id>',views.reject),
    path('search_user_p_request_reject/',views.search_user_p_request_reject),
    path('user_send_complaint/',views.user_send_complaint),
    path('user_send_complaint_post/',views.user_send_complaint_post),
    path('user_view_complaint/',views.user_view_complaint),
    path('search_user_view_complaint/',views.search_user_view_complaint),
    path('user_send_feedback/',views.user_send_feedback),
    path('user_send_feedback_post/',views.user_send_feedback_post),
    path('user_view_feedback/',views.user_view_feedback),
    path('search_user_view_feedback/',views.search_user_view_feedback),
    path('user_home/',views.user_home),
    path('view_other_user_materials/',views.view_other_user_materials),
    path('send_request/<id>',views.send_request),
    path('approve_request/<id>',views.approve_request),
    path('reject_request/<id>',views.reject_request),

    path('view_other_request/', views.view_other_request),
    path('user_p_request_rejects/', views.user_p_request_rejects),
    path('chat/<toid>', views.chat),
    path('chat_view/<tid>',views.chat_view),
    path('chat_send/<msg>',views.chat_send),
    # path('chat_view/',views.chat_view),
    # path('chat_view/',views.chat_view),
    # path('chat_view/',views.chat_view),


]
