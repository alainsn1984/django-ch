from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView

class HomePageTests(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)
    
    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_home_url_name(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_home_template(self):
        self.assertTemplateUsed(self.response, 'home.html')
    
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response,'Hi there! I should not be on the page')
    
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')
    
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
        
class AboutPagesTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)
        
    def test_aboutpages_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_aboutpages_template(self):
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_about_contains_correct_html(self):
        self.assertContains(self.response, 'About Pages')
        
    def test_aboutpages_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there, I should not be on the page.')
        
    def test_aboutpages_url_resolves_aboutpages_view(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
        