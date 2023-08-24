from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):
    """
        Check CustomUser:
            create_user, create_superuser
    """
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='alan',email='alan@email.com',password='testpass123')
        self.assertEqual(user.username, 'alan')
        self.assertEqual(user.email, 'alan@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
            
        )
        self.assertEqual(admin_user.username,'superadmin')
        self.assertEqual(admin_user.email,'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)