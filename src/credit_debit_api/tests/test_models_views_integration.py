from django.test import TestCase, RequestFactory
from mixer.backend.django import mixer
import pytest
from django.urls import reverse
from credit_debit_api import rest
from credit_debit_api.models import Transaction

@pytest.fixture
def account(request, db):
    return mixer.blend('credit_debit_api.VirtualAccount', status=request.param)

@pytest.mark.parametrize('account', [''], indirect=True)
def test_post_debit_authenticated_by_virtual_account_id(account):
    # if the user request debit method with own account
    value = 11234
    path = reverse('debit', kwargs={'value':value})
    mixer.blend('credit_debit_api.Transaction')
    factory = RequestFactory()
    request = factory.post(path)
    post_response = rest.views.transaction_debit(request, value=value, account_id=account.id)
    assert post_response.status_code == 200
    # then the post should have the same account
    pk = post_response.data['id']
    request.method = 'GET'
    get_response = rest.views.transaction_detail(request,pk=pk)
    assert get_response.status_code == 200
    assert get_response.data['account'] == account

@pytest.mark.parametrize('account', [''], indirect=True)
def test_post_credit_authenticated_by_virtual_account(account):
    # if the user request debit method
    value = 11234
    path = reverse('credit', kwargs={'value':value})
    mixer.blend('credit_debit_api.Transaction')
    factory = RequestFactory()
    request = factory.post(path)
    post_response = rest.views.transaction_credit(
        request, value=value, account_id=account.id)
    assert post_response.status_code == 200
    # then the post should have the same account
    pk = post_response.data['id']
    request.method = 'GET'
    get_response = rest.views.transaction_detail(request, pk=pk)
    assert get_response.status_code == 200
    assert get_response.data['account'] == account
