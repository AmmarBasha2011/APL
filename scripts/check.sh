#!/usr/bin/env bash
# check.sh — كل الفحوص المحلية في أمر واحد.
#
# الاستخدام:
#   ./scripts/check.sh            # كل الفحوص
#   ./scripts/check.sh --quiet    # من غير التفاصيل
#
# نفس الخطوات اللي بتشتغل في CI.
set -e
cd "$(dirname "$0")/.."

PY="${PYTHON:-python3}"
Q=""
[ "$1" = "--quiet" ] && Q="--quiet"

echo "== سلامة المكتبات =="
"$PY" scripts/check_libraries.py $Q

echo
echo "== لا تكرار في العناصر =="
"$PY" scripts/check_duplicates.py

echo
echo "== لا أسماء غير معرَّفة في الأمثلة والتوثيق =="
"$PY" scripts/check_undefined_names.py

echo
echo "== نظافة الريبو واتساق التوثيق =="
"$PY" scripts/check_repo.py $Q

echo
echo "== الأمثلة =="
"$PY" test_examples.py

echo
echo "✓ كل الفحوص نجحت"
