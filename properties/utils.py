from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging


def get_all_properties():
    all_properties = cache.get('all_properties')
    if not all_properties:
        all_properties = list(Property.objects.all())
        cache.set('all_properties', all_properties, 3600)  # 1 hour
    return all_properties


def get_redis_cache_metrics():
    conn = get_redis_connection("default")
    info = conn.info()
    hits = info.get('keyspace_hits', 0)
    misses = info.get('keyspace_misses', 0)
    hit_ratio = hits / (hits + misses) if (hits + misses) > 0 else 0
    logging.info(f"Redis Cache Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2f}")
    return {"hits": hits, "misses": misses, "hit_ratio": hit_ratio}
