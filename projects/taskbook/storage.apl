استورد sqlite3

def افتح(المسار):
    قاعدة = sqlite3.connect(المسار)
    قاعدة.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER DEFAULT 0)")
    return قاعدة

def أضف(قاعدة, عنوان):
    قاعدة.execute("INSERT INTO tasks(title) VALUES (?)", (عنوان,))
    قاعدة.commit()

def أكمل(قاعدة, رقم):
    قاعدة.execute("UPDATE tasks SET done=1 WHERE id=?", (رقم,))
    قاعدة.commit()

def اعرض(قاعدة):
    return قاعدة.execute("SELECT id, title, done FROM tasks ORDER BY id").fetchall()
