CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    username varchar(100) UNIQUE NOT NULL,
    password varchar(100) NOT NULL
);
