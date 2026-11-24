const run = document.getElementById('run');
run.addEventListener('click', async () => {
  run.disabled = true;
  const status = document.getElementById('status');
  const output = document.getElementById('output');
  status.textContent = 'جارٍ التشغيل';
  try {
    const response = await fetch('/run', {
      method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({source: document.getElementById('source').value})
    });
    const result = await response.json();
    output.textContent = result.output || result.error || 'انتهى التشغيل بدون مخرجات.';
    status.textContent = response.ok ? `${result.status} / ${result.exit_code ?? 'توقف'}` : 'تعذر التشغيل';
  } catch (_) {
    output.textContent = 'الخدمة غير متاحة. تحقق من تشغيل Docker والخادم المحلي.';
    status.textContent = 'غير متاح';
  } finally { run.disabled = false; }
});
