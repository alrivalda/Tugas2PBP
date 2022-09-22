from urllib import response
from django.test import TestCase, Client 

# Create your tests here.

class Testingmywatchlist(TestCase):
    # untuk melakukan testing
    def tes_mywatchlist_showhtml(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEquals(response.status_code,200)

    def tes_mywatchlist_showxmll(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEquals(response.status_code,200)
    
    def tes_mywatchlist_showjson(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEquals(response.status_code,200)
