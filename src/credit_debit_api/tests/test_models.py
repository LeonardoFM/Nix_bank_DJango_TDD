from mixer.backend.django import mixer
import pytest

# mock

@pytest.fixture
def transaction(request, db):
    return mixer.blend('credit_debit_api.Transaction', status=request.param)

@pytest.mark.parametrize('transaction', ['D'],indirect=True)
def test_Transaction_is_in_debit(transaction):
    # as Transaction = Transaction.upjects.create(...)
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