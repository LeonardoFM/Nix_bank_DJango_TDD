from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase
from credit_debit_api.views import transaction_detail
from mixer.backend.django import mixer
import pytest

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