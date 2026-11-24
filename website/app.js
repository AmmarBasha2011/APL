// نسخ الكود وتصفية جدول المكتبات. بدون مكتبات خارجية.
document.querySelectorAll(".copy").forEach(function (b) {
  b.addEventListener("click", function () {
    var code = b.parentElement.querySelector("code").innerText;
    var done = function () { b.textContent = "تم النسخ"; setTimeout(function () { b.textContent = "نسخ"; }, 1500); };
    if (navigator.clipboard) { navigator.clipboard.writeText(code).then(done); } else { done(); }
  });
});
var f = document.getElementById("filter");
if (f) {
  f.addEventListener("input", function () {
    var q = f.value.trim().toLowerCase();
    document.querySelectorAll("#libs tbody tr").forEach(function (r) {
      r.hidden = q && r.textContent.toLowerCase().indexOf(q) === -1;
    });
  });
}
