from credit_debit_api.models import VirtualAccount, Transaction
from mixer.backend.django import mixer
import pytest

# mock


@pytest.mark.django_db
def test_VirtualAccount_model():
    virtual_account = VirtualAccount.objects.create(
        name='AccountTest',agency='000-1',current_account='0000000-1')
    assert str(virtual_account) == 'AccountTest'    
    assert virtual_account.has_agency == True
    assert virtual_account.current_account == '0000000-1'

@pytest.fixture
def account(request, db):
    return mixer.blend('credit_debit_api.VirtualAccount', status=request.param)

@pytest.mark.parametrize('account', [''], indirect=True)
def test_VirtualAccount_name(account):
    assert account.name != ''

@pytest.mark.django_db
def test_Transaction_model():
    virtual_account = VirtualAccount.objects.create(
        name='AccountTest', agency='000-1', current_account='0000000-1')
    transaction = Transaction.objects.create(
        date = '2020-10-25',
        description = 'DEBIT',
        balance = 0,
        debit = 400,
        credit = 0,
        status = 'D',
        account = virtual_account)
    assert str(transaction) == 'DEBIT'    
    assert transaction.balance == 0
    assert transaction.debit == 400
    assert transaction.credit == 0

@pytest.fixture
def transaction(request, db):
    return mixer.blend('credit_debit_api.Transaction', status=request.param)

@pytest.mark.parametrize('transaction', ['D'], indirect=True)
def test_Transaction_is_in_debit(transaction):
    assert transaction.is_in_debit == True

@pytest.mark.parametrize('transaction', ['C'], indirect=True)
def test_Transaction_is_not_in_debit(transaction):
    assert transaction.is_in_debit == False

@pytest.mark.parametrize('transaction', ['C'], indirect=True)
def test_Transaction_is_in_credit(transaction):
    assert transaction.is_in_credit == True

@pytest.mark.parametrize('transaction', ['D'], indirect=True)
def test_Transaction_is_not_in_credit(transaction):
    assert transaction.is_in_credit == False