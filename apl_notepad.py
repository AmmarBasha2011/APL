#!/usr/bin/env python3
# APL Notepad - محرر لغة البرمجة عمار (RTL - واجهة عربية)

import sys, os, io, re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from threading import Thread

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apl

BG_TOP = "#0F0520"
BG_BOTTOM = "#2D1B69"
BG_EDIT = "#0D0418"
FG = "#E0D0FF"
FONT = ("Cascadia Code", 12, "bold")
FONT_OUT = ("Cascadia Code", 10)
LN_BG = "#0A0312"
LN_FG = "#605080"
LINE_FG = "#E0D0FF"
CURSOR = "#C792EA"
INSERT = "#C792EA"
SEL_BG = "#3D2B6B"
TAB_W = 4

APL_KEYWORDS = [
    "المتغير", "اطبع", "ادخل", "لو", "الا", "طالما", "لكل",
    "دالة", "ارجع", "توقف", "اكمل", "حاول", "إمسك", "امسك", "استورد",
    "من", "في", "و", "أو", "ليس", "مثل",
    "صحيح", "نص", "عشري", "منطق", "قائمة", "مجموعة", "مصفوفة", "قاموس", "بايت",
    "نطاق", "طول", "مطلق", "قوة", "جذر", "أكبر", "أصغر", "مقرب", "مجموع", "مفرز",
    "صواب", "خطأ", "لا_شيء",
]

APL_METHODS = [
    "تقسيم", "أضف", "ضم", "عكس", "فرز", "حذف", "نسخ", "عد", "بحث", "أزل", "وسع", "أدخل",
]

C = {
    "keyword": "#7FC1FF",
    "string":  "#FFD866",
    "comment": "#6A9955",
    "number":  "#F78C6C",
    "method":  "#C792EA",
    "builtin": "#FF5370",
    "oper":    "#89DDFF",
    "decor":   "#C792EA",
    "normal":  "#EEFFFF",
}


class APLNotepad:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("APL Notepad - محرر لغة البرمجة عمار")
        self.root.geometry("950x720")
        self.current_file = None
        self.modified = False
        self.highlight_timer = None
        self._rtl_lines = True
        self._build_gradient()
        self._build_ui()
        self._build_menu()
        self._bind_events()
        self._update_title()

    def _build_gradient(self):
        w, h = 950, 720
        self._gradient = tk.PhotoImage(width=w, height=h)
        blue_start = (15, 5, 32)
        purple_end = (45, 27, 105)
        buf = ""
        for y in range(h):
            r = int(blue_start[0] + (purple_end[0] - blue_start[0]) * y / h)
            g = int(blue_start[1] + (purple_end[1] - blue_start[1]) * y / h)
            b = int(blue_start[2] + (purple_end[2] - blue_start[2]) * y / h)
            for x in range(w):
                buf += f"#{r:02x}{g:02x}{b:02x} "
            buf += " "
            if y % 10 == 0 or y == h - 1:
                self._gradient.put(buf, (0, y - (y % 10), w, y + 1))
                buf = ""

    def _build_menu(self):
        m = tk.Menu(self.root)
        self.root.config(menu=m)
        f = tk.Menu(m, tearoff=0)
        f.add_command(label="جديد (New)", command=self.new_file, accelerator="Ctrl+N")
        f.add_command(label="فتح (Open)", command=self.open_file, accelerator="Ctrl+O")
        f.add_command(label="حفظ (Save)", command=self.save_file, accelerator="Ctrl+S")
        f.add_command(label="حفظ باسم (Save As)", command=self.save_as, accelerator="Ctrl+Shift+S")
        f.add_separator()
        f.add_command(label="خروج (Exit)", command=self.root.quit)
        m.add_cascade(label="ملف", menu=f)
        r = tk.Menu(m, tearoff=0)
        r.add_command(label="تشغيل (Run)", command=self.run_code, accelerator="F5")
        r.add_command(label="RTL عكس الاتجاه", command=self._toggle_rtl)
        m.add_cascade(label="تشغيل", menu=r)
        h = tk.Menu(m, tearoff=0)
        h.add_command(label="الأوامر", command=self.show_cmds)
        h.add_command(label="عن APL", command=self.show_about)
        m.add_cascade(label="مساعدة", menu=h)

    def _build_ui(self):
        self._grad_label = tk.Label(self.root, image=self._gradient)
        self._grad_label.place(x=0, y=0, relwidth=1, relheight=1)

        paned = ttk.PanedWindow(self.root, orient=tk.VERTICAL)
        paned.place(x=0, y=0, relwidth=1, relheight=1)
        style = ttk.Style()
        style.configure("TPanedWindow", background=BG_TOP)

        eframe = tk.Frame(paned, bg=BG_TOP)
        paned.add(eframe, weight=3)

        self.ln = tk.Text(eframe, width=5, padx=6, pady=6,
            bg=LN_BG, fg=LN_FG, font=FONT, state=tk.DISABLED,
            wrap=tk.NONE, takefocus=0, relief=tk.FLAT, cursor="arrow")
        self.ln.pack(side=tk.LEFT, fill=tk.Y)

        tf = tk.Frame(eframe, bg=BG_TOP)
        tf.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        xs = tk.Scrollbar(tf, orient=tk.HORIZONTAL)
        ys = tk.Scrollbar(tf, orient=tk.VERTICAL)
        self.text = tk.Text(tf, wrap=tk.NONE, undo=True, font=FONT,
            bg=BG_EDIT, fg=FG, insertbackground=CURSOR,
            insertwidth=2, relief=tk.FLAT, padx=10, pady=6,
            xscrollcommand=xs.set, yscrollcommand=ys.set,
            tabs=(30,), selectbackground=SEL_BG,
            inactiveselectbackground=SEL_BG, highlightthickness=0,
            bd=0,
        )
        xs.config(command=self.text.xview)
        ys.config(command=self.text.yview)
        xs.pack(side=tk.BOTTOM, fill=tk.X)
        ys.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.pack(fill=tk.BOTH, expand=True)
        self.text.lift()

        oframe = tk.Frame(paned, bg="#0A0312")
        paned.add(oframe, weight=1)

        olab = tk.Label(oframe, text="⚡ المخرجات (Output):",
            anchor="w", font=("Segoe UI", 9, "bold"),
            bg="#0A0312", fg="#B8A0D8")
        olab.pack(fill=tk.X, padx=4, pady=(2, 0))

        self.out = tk.Text(oframe, height=5, font=FONT_OUT,
            bg="#06020C", fg="#D0C0E0", state=tk.DISABLED,
            wrap=tk.WORD, relief=tk.FLAT, padx=6, pady=4,
            insertbackground=CURSOR, selectbackground=SEL_BG,
            highlightthickness=0, bd=0,
        )
        ys2 = tk.Scrollbar(oframe, orient=tk.VERTICAL, command=self.out.yview)
        self.out.config(yscrollcommand=ys2.set)
        ys2.pack(side=tk.RIGHT, fill=tk.Y)
        self.out.pack(fill=tk.BOTH, expand=True)

    def _bind_events(self):
        self.text.bind("<KeyRelease>", self._on_key)
        self.text.bind("<<Modified>>", self._on_mod)
        self.text.bind("<Control-n>", lambda e: self.new_file())
        self.text.bind("<Control-N>", lambda e: self.new_file())
        self.text.bind("<Control-o>", lambda e: self.open_file())
        self.text.bind("<Control-O>", lambda e: self.open_file())
        self.text.bind("<Control-s>", lambda e: self.save_file())
        self.text.bind("<Control-S>", lambda e: self.save_file())
        self.text.bind("<Control-Shift-S>", lambda e: self.save_as())
        self.text.bind("<Control-Shift-s>", lambda e: self.save_as())
        self.root.bind("<F5>", lambda e: self.run_code())
        self.text.bind("<Tab>", self._tab)
        self.text.bind("<Return>", self._enter)
        self.text.bind("<BackSpace>", self._bs)
        self.text.bind("<ButtonRelease>", lambda e: self._highlight())
        self.text.bind("<MouseWheel>", lambda e: self._on_scroll(e))
        self.ln.bind("<MouseWheel>", lambda e: self._on_scroll(e))

    def _on_scroll(self, event):
        self.text.yview_scroll(int(-1 * event.delta / 120), "units")
        self._sync_scroll()

    def _sync_scroll(self):
        self.ln.yview_moveto(self.text.yview()[0])

    def _on_key(self, event):
        if event.keysym in ("Shift_L","Shift_R","Control_L","Control_R","Alt_L","Alt_R"):
            return
        if self.highlight_timer:
            self.root.after_cancel(self.highlight_timer)
        self.highlight_timer = self.root.after(120, self._highlight)

    def _on_mod(self, e=None):
        if self.text.edit_modified():
            self.modified = True
            self._update_title()
            self._update_lines()
            self.text.edit_modified(False)

    def _tab(self, e):
        self.text.insert(tk.INSERT, " " * 4)
        return "break"

    def _enter(self, e):
        line = self.text.get("insert linestart", "insert")
        ind = len(line) - len(line.lstrip())
        ex = 4 if line.strip().endswith(":") else 0
        self.text.insert(tk.INSERT, "\n" + " " * (ind + ex))
        return "break"

    def _bs(self, e):
        p = self.text.index(tk.INSERT)
        ls = self.text.index(f"{p} linestart")
        t = self.text.get(ls, p)
        if t and t.strip() == "" and len(t) % 4 == 0 and len(t) > 0:
            self.text.delete(f"{ls} -4c", p)
            return "break"

    def _update_lines(self):
        n = len(self.text.get("1.0", "end-1c").split("\n"))
        txt = "\n".join(str(i+1) for i in range(n))
        self.ln.config(state=tk.NORMAL)
        self.ln.delete("1.0", tk.END)
        self.ln.insert("1.0", txt)
        self.ln.config(state=tk.DISABLED)
        self._sync_scroll()

    def _update_title(self):
        t = "APL Notepad"
        if self.current_file:
            t += f" - {os.path.basename(self.current_file)}"
        else:
            t += " - [غير محفوظ]"
        if self.modified:
            t += " *"
        self.root.title(t)

    def _toggle_rtl(self):
        self._rtl_lines = not self._rtl_lines
        self._reload_text()

    def _reload_text(self):
        content = self._get_text()
        self.text.delete("1.0", tk.END)
        self.text.insert("1.0", content)
        self._highlight()

    def _get_text(self):
        return self.text.get("1.0", "end-1c")

    def _out(self, text, err=False):
        self.out.config(state=tk.NORMAL)
        if err:
            self.out.insert(tk.END, text, "e")
            self.out.tag_config("e", foreground="#F14C4C")
        else:
            self.out.insert(tk.END, text)
        self.out.see(tk.END)
        self.out.config(state=tk.DISABLED)

    def _out_clear(self):
        self.out.config(state=tk.NORMAL)
        self.out.delete("1.0", tk.END)
        self.out.config(state=tk.DISABLED)

    def new_file(self):
        if self.modified and not messagebox.askyesno("APL", "حفظ التغييرات؟"):
            return
        self.text.delete("1.0", tk.END)
        self.current_file = None
        self.modified = False
        self._out_clear()
        self._update_title()

    def open_file(self):
        p = filedialog.askopenfilename(title="فتح ملف APL",
            filetypes=[("APL files","*.apl"),("All files","*.*")])
        if not p:
            return
        try:
            with open(p, "r", encoding="utf-8") as f:
                c = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert("1.0", c)
            self.current_file = p
            self.modified = False
            self._update_title()
            self._highlight()
            self._out_clear()
        except Exception as e:
            messagebox.showerror("خطأ", f"لا يمكن فتح الملف:\n{e}")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w", encoding="utf-8") as f:
                    f.write(self._get_text())
                self.modified = False
                self._update_title()
            except Exception as e:
                messagebox.showerror("خطأ", f"لا يمكن الحفظ:\n{e}")
        else:
            self.save_as()

    def save_as(self):
        p = filedialog.asksaveasfilename(title="حفظ باسم",
            defaultextension=".apl",
            filetypes=[("APL files","*.apl"),("All files","*.*")])
        if p:
            self.current_file = p
            self.save_file()

    def run_code(self):
        self._out_clear()
        c = self._get_text().strip()
        if not c:
            self._out("✗ الكود فارغ\n")
            return
        self._out("⏳ جاري التشغيل...\n")
        def _r():
            try:
                py = apl.transpile(c)
                so, se = io.StringIO(), io.StringIO()
                os, es = sys.stdout, sys.stderr
                sys.stdout, sys.stderr = so, se
                try:
                    exec(py, {})
                except Exception:
                    import traceback
                    se.write(traceback.format_exc())
                sys.stdout, sys.stderr = os, es
                self.root.after(0, lambda: self._show_result(so.getvalue(), se.getvalue()))
            except (SyntaxError, Exception) as e:
                self.root.after(0, lambda: self._out(f"✗ {e}\n", True))
        Thread(target=_r, daemon=True).start()

    def _show_result(self, o, e):
        self._out_clear()
        if o:
            self._out("▼ المخرجات:\n")
            self._out(o)
        if e:
            self._out("▼ الأخطاء:\n")
            self._out(e, True)
        if not o and not e:
            self._out("✓ تم بنجاح\n")

    def show_cmds(self):
        txt = "أوامر APL:\n\n" + "\n".join(f"  {k}" for k in APL_KEYWORDS)
        messagebox.showinfo("الأوامر", txt)

    def show_about(self):
        messagebox.showinfo("عن APL",
            "APL - لغة البرمجة عمار\nالإصدار 1.0\n\nلغة برمجة بالعربية تتحول إلى بايثون.\n\nAPL Notepad - محرر APL\nيدعم RTL والتلوين والوضع الداكن.")

    def _highlight(self):
        try:
            data = self._get_text()
            for t in self.text.tag_names():
                if t not in ("sel","tk_sel"):
                    self.text.tag_delete(t)
            for k, v in C.items():
                self.text.tag_config(k, foreground=v)
            self.text.tag_config("keyword", font=FONT)
            self.text.tag_config("builtin", font=FONT)

            idx, length = 0, len(data)
            while idx < length:
                c = data[idx]
                if data[idx:idx+1] == "#":
                    end = data.find("\n", idx)
                    if end == -1: end = length
                    self.text.tag_add("comment", f"1.{idx}", f"1.{end}")
                    idx = end

                elif c == '"':
                    end = data.find('"', idx + 1)
                    if end == -1: end = length
                    else: end += 1
                    self.text.tag_add("string", f"1.{idx}", f"1.{end}")
                    idx = end

                elif c == "'":
                    end = data.find("'", idx + 1)
                    if end == -1: end = length
                    else: end += 1
                    self.text.tag_add("string", f"1.{idx}", f"1.{end}")
                    idx = end

                elif c.isdigit() or (c == "." and idx > 0 and idx < length-1
                      and data[idx-1].isdigit()):
                    end = idx
                    while end < length and (data[end].isdigit() or data[end] == "."):
                        end += 1
                    self.text.tag_add("number", f"1.{idx}", f"1.{end}")
                    idx = end

                elif c in "+-*/%=<>!&|":
                    self.text.tag_add("oper", f"1.{idx}", f"1.{idx+1}")
                    idx += 1

                elif c == "." and idx + 1 < length:
                    rest = data[idx+1:]
                    ok = False
                    for m in APL_METHODS:
                        if rest.startswith(m) and (len(rest)==len(m) or not rest[len(m)].isalnum()):
                            self.text.tag_add("method", f"1.{idx}", f"1.{idx+1+len(m)}")
                            idx += 1 + len(m)
                            ok = True
                            break
                    if not ok: idx += 1

                elif c.isalpha() or c in "آأإة":
                    start = idx
                    while idx < length and (data[idx].isalnum() or data[idx]=="_"):
                        idx += 1
                    tok = data[start:idx]
                    if tok in APL_KEYWORDS:
                        self.text.tag_add("keyword", f"1.{start}", f"1.{idx}")
                else:
                    idx += 1
        except Exception:
            pass

    def run(self):
        self._update_lines()
        self._highlight()
        self.root.mainloop()


if __name__ == "__main__":
    APLNotepad().run()
