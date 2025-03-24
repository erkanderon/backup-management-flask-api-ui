DROP TABLE IF EXISTS images;

CREATE TABLE images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    version TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('PENDING', 'FAILED', 'COMPLETED')),
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO images (version, name, status) VALUES ('v1.0', 'Project A', 'PENDING');
INSERT INTO images (version, name, status) VALUES ('v1.1', 'Project B', 'FAILED');
INSERT INTO images (version, name, status) VALUES ('v1.2', 'Project C', 'COMPLETED');