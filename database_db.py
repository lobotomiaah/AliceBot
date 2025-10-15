import sqlite3
import os

DB_DIR = "database"
os.makedirs(DB_DIR, exist_ok=True)

DB_PATH = os.path.join(DB_DIR, "fichas.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fichas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    rank TEXT NOT NULL,
    classe TEXT NOT NULL,
    persona TEXT NOT NULL,
    nivel INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()

print(f"✅ Banco de dados e tabela 'fichas' criados com sucesso em {DB_PATH}!")
