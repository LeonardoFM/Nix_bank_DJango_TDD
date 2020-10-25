from django.urls import path
from .views import (
    transaction_detail,
    transaction_detail_by_day,
    transaction_debit,
    transaction_credit,
    account_detail,
    create_account_detail,
    account_detail_by_data,
    extract )

urlpatterns = [
    path('transaction/<pk>', transaction_detail),
    path('transaction/date/<str:date>/', transaction_detail_by_day,name='day'),
    path('transaction/debit/<int:value>', transaction_debit,name='debit'),
    path('transaction/credit/<int:value>', transaction_credit,name='credit'),
    path('account/<pk>', account_detail, name='account'),
    path('account/data/', account_detail_by_data, name='account_data'),
    path('account/create/', create_account_detail, name='account_create'),
    path('account/extract/', extract, name='extract')
]
