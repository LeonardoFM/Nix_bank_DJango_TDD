from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    DestroyAPIView)

from credit_debit_api.models import Transaction, VirtualAccount

from .serializers import TransactionSerializer, VirtualAccountSerializer

def data_view(transaction) -> dict:
    data = {
        'id': transaction.id,
        'description': transaction.description,
        'balance': transaction.balance,
        'debit': transaction.debit,
        'credit': transaction.credit,
        'status': transaction.status,
        'date': str(transaction.date),
        'account': transaction.account
    }
    return data

@api_view(['GET'])
def transaction_detail(request, pk):
    # print(request.user)
    transaction = get_object_or_404(Transaction, pk=pk)
    data = data_view(transaction)
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET'])
def transaction_detail_by_day(request, date):
    # print(request.user)
    data = []
    transaction = Transaction.objects.filter(date=date)
    for trs in transaction:
        data.append(data_view(trs))
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['POST'])
def transaction_debit(request, value):
    account_id = int(dict(request.query_params)['account_id'][0])
    transaction = Transaction.objects.last()
    balance = transaction.balance - value
    
    if balance < 0:
        stat = 'D'
    else:
        stat = 'C'

    t = Transaction.objects.create(
        description = 'DEBITO',
        balance = balance,
        debit = value,
        credit = 0,
        status = stat,
        account_id = account_id
    )    
    t.save()

    return Response(data={'id':t.id},status=status.HTTP_200_OK)

@api_view(['POST'])
def transaction_credit(request, value):
    account_id = int(dict(request.query_params)['account_id'][0])
    transaction = Transaction.objects.last()
    balance = transaction.balance + value
    
    if balance < 0: stat = 'D'
    else: stat = 'C'

    t = Transaction.objects.create(
        description = 'CREDITO',
        balance = balance,
        debit = value,
        credit = 0,
        status = stat,
        account_id = account_id)

    t.save()

    return Response(data={'id':t.id},status=status.HTTP_200_OK)

@api_view(['GET'])
def account_detail(request, pk):
    va = get_object_or_404(VirtualAccount, pk=pk)
    data = {
        "id": va.id,
        "name":va.name,
        "agency": va.agency,
        "current_account": va.current_account}
    return Response(data=data,status=status.HTTP_200_OK)

@api_view(['GET'])
def account_detail_by_data(request):
    data = dict(request.query_params)
    
    va = VirtualAccount.objects.filter(
        name=data['name'][0],
        agency=data['agency'][0],
        current_account=data['current_account'][0])
    
    if len(va) == 1:
        data = { "account_id":va[0].id }
        return Response(data=data,status=status.HTTP_200_OK)

    elif len(va) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_account_detail(request, data):

    va = VirtualAccount.objects.create(
        name = data['name'],
        agency = data['agency'],
        current_account = data['current_account'])

    return Response(data={'account_id':va.id},status=status.HTTP_200_OK)

@api_view(['GET'])
def extract(request):
    agency = request.data['agency']
    current_account = request.data['current_account']
    account = VirtualAccount.objects.filter(agency=agency,
        current_account=current_account)

    transactions = Transaction.objects.filter(account=account[0])
    data = {}
    for t in transactions:
        data.update({
            "date":t.date,
            "description":t.description,
            "balance":t.balance,
            "debit":t.debit,
            "credit":t.credit,
            "status":t.status
        })
    
    return Response(data=data,status=status.HTTP_200_OK)

