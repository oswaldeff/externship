from django.conf import settings
from django_elasticsearch_dsl import Document, fields
from elasticsearch_dsl import analyzer
from elasticsearch_dsl.connections import connections
from django_elasticsearch_dsl.registries import registry
from products.models import BaseMerchandise


# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])


nori_korean = analyzer(
    'nori_korean',
    tokenizer='nori_tokenizer',
    filter=['lowercase', 'stop'],
)


@registry.register_document
class MerchandiseDocument(Document):
    class Index:
        name = 'product_data'
    
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    
    name = fields.TextField(
        analyzer=nori_korean,
        fields={'raw': fields.KeywordField()}
    )
    description = fields.TextField(
        analyzer=nori_korean,
        fields={'raw': fields.KeywordField()}
    )
    
    class Django:
        model = BaseMerchandise