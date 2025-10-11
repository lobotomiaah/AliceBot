import sqlite3
import os


os.makedirs("database", exist_ok=True)

caminho_db = os.path.join("database", "rpg.db")

conn = sqlite3.connect(caminho_db)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fichas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    classe TEXT NOT NULL,
    persona TEXT NOT NULL,
    nivel INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0
)
""")

conn.commit()
conn.close()

print("✅ Banco de dados e tabela 'fichas' criados com sucesso!")
