from django.urls import path
from . import generic_views
from . import views
from . import api
from rest_framework.urlpatterns import format_suffix_patterns



app_name = "polls"
# from . import page,info,html_render,heroname,calculate,simpleinterest,html_render_1,simple_int,temp_data
urlpatterns = [path("main/", views.page, name ="my_1st_page"),
               path("question/", views.info, name ="question"),
               # path("mypage/",html_render,name = "mypage"),
               path("filmactor/", views.heroname, name ="filmactor"),
               path("calculate/<int:principle>/<int:months>/<str:rate_of_interest>/", views.calculate, name ="calculate"),
               path("simpleinterest/<int:principal>/<int:time>/<str:roi>/", views.simpleinterest, name ="simpleinterest"),
               path("newpage/", views.html_render_1, name ="newpage"),
               path("simple_interst/<int:principle>/<int:months>/<str:rate_of_interest>/", views.simple_int, name ="simple_interst"),
               path("mypage/", views.temp_data, name ="my_page"),
               path("index/", views.index, name ="questions"),
               path("question/<int:question_id>/choices/", views.choice, name="choices"),
               path("create/question/", views.create_question, name="create-question"),
               path("create/<int:question_id>/choice/", views.create_choice, name="create-choice"),


               #email
               path("emails/", views.emails, name="all-emails"),  # email listing page
               path("email/create", views.create_email, name="create-email"),
               path("email/<int:pk>/", views.email_detail, name="detail-email"),
               path("email/<int:pk>/update/", views.edit_email, name="edit-email"),
               path("email/<int:pk>/edit-dj/", views.edit_dj_email, name="edit-dj-email"),


               #product enquiry
               path('enquiry/', views.enquiry_form, name='enquiry_form'),
               path('dealer/', views.dealer_list, name='dealer_list'),
               path('edit/<str:phone_number>/', views.edit_customer_details, name='edit_customer_details'),


               #generic views
               # generic views
               path("generic/emails/", generic_views.EmailListView.as_view(), name="generic-email-list"),
               path("generic/emails/create", generic_views.EmailCreateView.as_view(), name="generic-email-create"),
               path("generic/email/<int:pk>/", generic_views.EmailDetailView.as_view(), name="generic-email-detail"),
               path("generic/email/update/<int:pk>/", generic_views.EmailUpdateView.as_view(),
                    name="generic-email-update"),

               #auth
               path("login", views.user_login, name="fun-login"),
               ]

api_urlpatterns = [
    path('api/v1/emails/', api.EmailList.as_view()),
    path('api/v1/emails/<int:pk>/', api.EmailList.as_view()),
]

api_urlpatterns = format_suffix_patterns(api_urlpatterns)

urlpatterns += api_urlpatterns