from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item, Category

class ItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.category = Category.objects.create(name="Electronics")
        self.item = Item.objects.create(
            user=self.user,
            name="Test Item",
            description="A test item",
            price=10.00,
            category=self.category
        )

    def test_item_creation(self):
        self.assertEqual(self.item.description, "A test item")
        self.assertEqual(self.item.category.name, "Electronics")
        self.assertEqual(str(self.item), "Test Item")
