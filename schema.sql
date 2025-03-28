DROP TABLE IF EXISTS images;

CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    version TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('PENDING', 'FAILED', 'COMPLETED')),
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
);