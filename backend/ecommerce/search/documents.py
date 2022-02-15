from django.conf import settings
from django_elasticsearch_dsl import Document, Index
from elasticsearch_dsl import analyzer
from elasticsearch_dsl.connections import connections
from django_elasticsearch_dsl.registries import registry
from products.models import BaseMerchandise


# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

@registry.register_document
class MerchandiseDocument(Document):
    class Index:
        name = 'product_data'
    
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    
    class Django:
        model = BaseMerchandise
        
        fields = [
            'name',
            'description',
        ]