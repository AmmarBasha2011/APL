# سيرفر اللغة (LSP)

`editors/lsp/apl_lsp.py` سيرفر لغة للعمار بيشتغل مع أي محرر بيدعم LSP.
مكتوب بمكتبة Python القياسية بس: مفيش أي حاجة تتثبت.

## بيعمل إيه

- **أخطاء المترجم نفسه**: كل حفظ بيشغّل نفس خطوة الترجمة والتصريف اللي
  `عمار فحص` بيشغّلها، فالإيرور اللي بتشوفه هو اللي المفسّر هيقوله، برقم السطر
  والعمود وبالرسالة العربية.
- **تنبيهات `عمار فحص`** كتحذيرات: تاب، مسافات في آخر السطر، `=` جوه شرط،
  وTODO لسه موجود.
- **اقتراحات (completion)** لكلمات اللغة، ودوال المكتبات، وأسماء الـ 106 مكتبة
  المنشورة، والدوال والأصناف اللي في الملف اللي بتشتغل عليه.
- **شرح الكلمة (hover)** لأي كلمة في كتالوج اللغة.
- **فهرس الملف (outline)** لكل `دالة` و`صنف` في الملف.

السيرفر **مابيشغّلش** أي برنامج: تصريف وفحص بس.

## التشغيل

من جوه ريبو APL:

```
python editors/lsp/apl_lsp.py
```

أو من أي مكان، وانت بتقول للسيرفر فين الريبو:

```
APL_HOME=/path/to/APL python /path/to/APL/editors/lsp/apl_lsp.py
```

على ويندوز:

```
set APL_HOME=C:\path\to\APL
python C:\path\to\APL\editors\lsp\apl_lsp.py
```

## Neovim (0.8+، مفيش أي إضافة)

```lua
vim.filetype.add({ extension = { apl = "apl" } })

vim.api.nvim_create_autocmd("FileType", {
  pattern = "apl",
  callback = function(args)
    vim.lsp.start({
      name = "apl",
      cmd = { "python3", "/path/to/APL/editors/lsp/apl_lsp.py" },
      root_dir = vim.fs.dirname(vim.fs.find({ "apl.py" }, { upward = true })[1]),
    }, { bufnr = args.buf })
  end,
})
```

## Emacs (eglot، مدمج من 29)

```elisp
(add-to-list 'eglot-server-programs
             '(apl-mode . ("python3" "/path/to/APL/editors/lsp/apl_lsp.py")))
```

## VS Code

الـ VS Code مابيشغّلش سيرفرات LSP لوحده؛ استخدم إضافة عامة زي *GLSP* أو
*vscode-languageclient*-based generic client، وحطّ الأمر:

```
python3 /path/to/APL/editors/lsp/apl_lsp.py
```

وفي نفس المجلد `editors/vscode/` فيه إضافة التلوين والاقتراحات الجاهزة، وبتشتغل
من غير أي سيرفر.

## الاختبار

```
python tests/test_lsp.py
```

الاختبار بيشغّل السيرفر كعملية مستقلة وبيتكلم معاه LSP زي أي محرر، وبيتأكد من
الأخطاء والتحذيرات والاقتراحات والشرح والفهرس. وهو كمان جزء من
`python tests/run_tests.py`.
