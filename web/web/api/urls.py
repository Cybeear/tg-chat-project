from django.urls import path, re_path
from .views import apiOverview, FaqList, FaqDetail, BlockWriteDetail, UserWriteList, UserWriteDetail, BlockWriteList


urlpatterns = [
    path('', apiOverview),
    path('faq', FaqList.as_view()),
    path('faq/<str:title>', FaqDetail.as_view()),
    path('block', BlockWriteList.as_view()),
    re_path(r'^block/(?P<user>\d+)$', BlockWriteDetail.as_view()),
    path('user', UserWriteList.as_view()),
    re_path(r'^user/(?P<user_id_tg>\d+)$', UserWriteDetail.as_view()),
]
