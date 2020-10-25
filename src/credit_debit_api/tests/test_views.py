from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase, RequestFactory
from credit_debit_api.views import transaction_detail
from credit_debit_api import rest
from mixer.backend.django import mixer
import pytest
import datetime

@pytest.mark.django_db
class TestRestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestRestViews, cls).setUpClass()
        mixer.blend('credit_debit_api.Transaction')
        cls.factory = RequestFactory()

    def test_get_transaction_detail(self):
        path = reverse('description', kwargs={'pk':1})
        request = self.factory.get(path)
        response = rest.views.transaction_detail(request,pk=1)
        assert response.status_code == 200
    
    def test_get_transaction_detail_by_day(self):
        path = reverse('day', kwargs={'date':1})
        request = self.factory.get(path)
        day = str(datetime.date.today())
        response = rest.views.transaction_detail_by_day(request,date=day)
        assert response.status_code == 200

    def test_post_debit(self):
        value = 11234
        path = reverse('debit', kwargs={'value':value})
        request = self.factory.get(path)
        request.method = 'POST'
        account = mixer.blend('credit_debit_api.VirtualAccount')
        response = rest.views.transaction_debit(request, value=value, account_id=account.id)
        assert response.status_code == 200
    
    def test_post_credit(self):
        """ test a logged user using credit method
        """
        value = 1234
        path = reverse('credit', kwargs={'value':value})
        request = self.factory.get(path)
        request.method = 'POST'
        account = mixer.blend('credit_debit_api.VirtualAccount')
        response = rest.views.transaction_credit(request, value=value, account_id=account.id)
        assert response.status_code == 200
    
    def test_get_virtual_account_detail(self):
        """ the view should return data by primary key (id)
        """
        path = reverse('account', kwargs={'pk':1})
        request = self.factory.get(path)
        response = rest.views.account_detail(request, pk=1)
        assert response.status_code == 200

    def test_post_create_account_detail(self):
        path = reverse('account_create')
        request = self.factory.get(path)
        request.method = 'POST'
        data = {
            'name':'teste3',
            'agency':'000-3',
            'current_account': '0000000-3'
        }
        response = rest.views.create_account_detail(request, data)
        assert response.status_code == 200
        



@pytest.mark.django_db
class TestViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestViews, cls).setUpClass()
        mixer.blend('credit_debit_api.Transaction')
        cls.factory = RequestFactory()

    def test_transaction_detail_authenticated(self):
        path = reverse('description', kwargs={'pk':1})
        request = self.factory.get(path)
        request.user = mixer.blend(User)

        response = transaction_detail(request,pk=1)
        assert response.status_code == 200

    def test_transaction_detail_unauthenticated(self):
        path = reverse('description', kwargs={'pk':1})
        request = self.factory.get(path)
        request.user = AnonymousUser()

        response = transaction_detail(request,pk=1)
        assert response.status_code == 200