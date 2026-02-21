CREATE TABLE IF NOT EXISTS sections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS problems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    section_id INTEGER,
    title TEXT NOT NULL,
    description TEXT,
    submission_result TEXT DEFAULT 'US',
    total_of_correct_outputs INTEGER DEFAULT 0,
    FOREIGN KEY (section_id) REFERENCES sections(id)
);

CREATE TABLE IF NOT EXISTS test_cases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    problem_id INTEGER,
    input_value TEXT,
    expected_output TEXT,
    FOREIGN KEY (problem_id) REFERENCES problems(id)
);

-- ==========================================
-- POVOANDO OS DADOS (SEED)
-- ==========================================

INSERT OR IGNORE INTO sections (id, nome) VALUES 
(1, 'Iniciante'), 
(2, 'Algoritmos'), 
(3, 'Estrutura de Dados');

INSERT OR IGNORE INTO problems (id, section_id, title, description) 
VALUES (1, 1, 'Soma Simples', 'Leia dois valores e imprima a soma.');

INSERT OR IGNORE INTO test_cases (id, problem_id, input_value, expected_output) VALUES 
(1, 1, '2\n3', '5'),
(2, 1, '10\n-2', '8'),
(3, 1, '-9\n-5', '-14');

INSERT OR IGNORE INTO problems (id, section_id, title, description) 
VALUES (2, 1, 'Olá Mundo', 'Imprima a mensagem clássica de boas-vindas.');

INSERT OR IGNORE INTO test_cases (id, problem_id, input_value, expected_output) VALUES 
(4, 2, '', 'Hello World');