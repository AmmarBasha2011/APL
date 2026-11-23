# مثال 176 — تسجيل الأحداث بمستويات
# Logging with levels
# Demonstrates: logging، المستويات، التنسيق
#
# Run:  python apl.py examples/176-logging-levels.apl

import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logging.debug("رسالة تصحيح لن تظهر")
logging.info("بدأ البرنامج")
logging.warning("تحذير: مساحة قليلة")
logging.error("خطأ غير قاتل")

اطبع "انتهى التسجيل (راجع stderr أعلاه)."
