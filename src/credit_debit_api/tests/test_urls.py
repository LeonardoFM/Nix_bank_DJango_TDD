from django.urls import reverse, resolve

class TestUrls:

    def test_detail_url(self):
        # give us the path back
        path = reverse('description',kwargs={'pk':1})
        # so this should return the correct function
        assert resolve(path).view_name == 'description'