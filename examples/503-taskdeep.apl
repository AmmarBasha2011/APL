# 503 · المهام الموزعة العميقة — taskdeep
# celery / kombu / billiard / amqp
#
# Run:  python apl.py examples/503-taskdeep.apl

اطبع "=== طوابير kombu ==="
المتغير ط = كومبو_طابور("مهام")
اطبع "اسم الطابور:", ط.name

المتغير ت = كومبو_مهام_exchange("تبادل")
اطبع "اسم التبادل:", ت.name

اطبع "=== جدولة celery ==="
المتغير ج = مهام_crontab(minute="*/15")
اطبع "الجدول:", ج
