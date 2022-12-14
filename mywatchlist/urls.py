from django.urls import path
from mywatchlist.views import  show_xml, show_json, show_json_by_id, show_xml_by_id, show_html


# menambah path dan meminta request pada view
app_name ='watchlist'
urlpatterns = [
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('html/', show_html, name='show_html'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),

]