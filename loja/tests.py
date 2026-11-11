import json
from django.test import TestCase
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse
from .models import Produto


class CheckoutTests(TestCase):
    def setUp(self):
        self.client.force_login(User.objects.create_user('demo'))
        self.a = Produto.objects.create(nome='A', preco=10, quantidade=5)
        self.b = Produto.objects.create(nome='B', preco=20, quantidade=1)
        session = self.client.session
        session[settings.CART_SESSION_ID] = {
            str(self.a.pk): {'quantidade': 2, 'preco': '10'},
            str(self.b.pk): {'quantidade': 2, 'preco': '20'},
        }
        session.save()

    def test_checkout_failure_keeps_all_stock(self):
        self.assertEqual(self.client.post(reverse('checkout')).status_code, 302)
        self.a.refresh_from_db()
        self.assertEqual(self.a.quantidade, 5)
        self.assertIn(settings.CART_SESSION_ID, self.client.session)

    def test_checkout_requires_post(self):
        self.assertEqual(self.client.get(reverse('checkout')).status_code, 405)

    def test_cart_render_preserves_json_session(self):
        self.assertEqual(self.client.get(reverse('ver_carrinho')).status_code, 200)
        json.dumps(self.client.session[settings.CART_SESSION_ID])

    def test_success_decrements_and_clears(self):
        self.b.quantidade = 3
        self.b.save()
        self.assertEqual(self.client.post(reverse('checkout')).status_code, 200)
        self.a.refresh_from_db()
        self.b.refresh_from_db()
        self.assertEqual((self.a.quantidade, self.b.quantidade), (3, 1))
        self.assertFalse(self.client.session.get(settings.CART_SESSION_ID))
