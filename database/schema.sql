CREATE TABLE IF NOT EXISTS fichas (
    usuario_id INTEGER NOT NULL,
    nome TEXT NOT NULL,
    persona TEXT NOT NULL,
    rank TEXT NOT NULL,
    classe TEXT NOT NULL,
    nivel INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0,
    PRIMARY KEY (usuario_id, nome)
);