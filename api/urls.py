from django.urls import path
from .views import CourseListView, SchoolListView, CommentListView, TeacherListView, register_user, RegisterListView
from .views import RegisterDetail, CourseDetail, TeacherDetail, SchoolDetail, CommentDetail

from .views import CourseRuListView, CourseEnListView, SchoolRuListView, SchoolEnListView \
                ,CommentRuListView, CommentEnListView, TeacherRuListView, TeacherEnListView

from .views import CourseRuDetail, CourseEnDetail, SchoolRuDetail, SchoolEnDetail \
                , CommentRuDetail, CommentEnDetail, TeacherRuDetail, TeacherEnDetail

urlpatterns = [
    path('uz/courses/', CourseListView.as_view(), name='course-list'), # Serverdagi malumotni korish
    path('uz/courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'), # serverdagi malumotni ozgartirish
    path('ru/courses/', CourseRuListView.as_view(), name='course-ru-list'), # Serverdagi malumotni korish
    path('ru/courses/<int:pk>/', CourseRuDetail.as_view(), name='course-ru-detail'), # serverdagi malumotni ozgartirish
    path('en/courses/', CourseEnListView.as_view(), name='course-en-list'), # Serverdagi malumotni korish
    path('en/courses/<int:pk>/', CourseEnDetail.as_view(), name='course-en-detail'), # serverdagi malumotni ozgartirish


    path('uz/schools/', SchoolListView.as_view(), name='school-list'), # Serverdagi malumotni korish
    path('uz/schools/<int:pk>/', SchoolDetail.as_view(), name='school-detail'), # serverdagi malumotni ozgartirish
    path('ru/schools/', SchoolRuListView.as_view(), name='school-ru-list'), # Serverdagi malumotni korish
    path('ru/schools/<int:pk>/', SchoolRuDetail.as_view(), name='school-ru-detail'), # serverdagi malumotni ozgartirish
    path('en/schools/', SchoolEnListView.as_view(), name='school-en-list'), # Serverdagi malumotni korish
    path('en/schools/<int:pk>/', SchoolEnDetail.as_view(), name='school-en-detail'), # serverdagi malumotni ozgartirish


    path('uz/comments/', CommentListView.as_view(), name='comment-list'), # Serverdagi malumotni korish
    path('uz/comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'), # serverdagi malumotni ozgartirish
    path('ru/comments/', CommentRuListView.as_view(), name='comment-ru-list'), # Serverdagi malumotni korish
    path('ru/comments/<int:pk>/', CommentRuDetail.as_view(), name='comment-ru-detail'), # serverdagi malumotni ozgartirish
    path('en/comments/', CommentEnListView.as_view(), name='comment-en-list'), # Serverdagi malumotni korish
    path('en/comments/<int:pk>/', CommentEnDetail.as_view(), name='comment-en-detail'), # serverdagi malumotni ozgartirish


    path('uz/teachers/', TeacherListView.as_view(), name='teacher-list'), # Serverdagi malumotni korish
    path('uz/teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'), # serverdagi malumotni ozgartirish
    path('ru/teachers/', TeacherRuListView.as_view(), name='teacher-ru-list'), # Serverdagi malumotni korish
    path('ru/teachers/<int:pk>/', TeacherRuDetail.as_view(), name='teacher-ru-detail'), # serverdagi malumotni ozgartirish
    path('en/teachers/', TeacherEnListView.as_view(), name='teacher-en-list'),
    path('en/teachers/<int:pk>/', TeacherEnDetail.as_view(), name='teacher-en-detail'), # serverdagi malumotni ozgartirish
    

    path('register/', RegisterListView.as_view(), name='register-user'), # Serverdagi malumotni korish
    path('register/add/', register_user, name='register-user'),  # serverga malumot yangi malumot qo'shish
    path('register/<int:pk>/', RegisterDetail.as_view(), name='register-update-destroy'), # serverdagi malumotni ozgartirish
]