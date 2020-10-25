from django.shortcuts import render, get_object_or_404
from .models import Transaction


def transaction_detail(request, pk):
    # print(request.user)
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transaction_detail.html', {'transaction':transaction})