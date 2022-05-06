CREATE DATABASE "appdb"
   WITH OWNER "postgres"
   ENCODING 'UTF8';

\c appdb;

CREATE TABLE IF NOT EXISTS appdb.public.customer(
   id           SERIAL PRIMARY KEY NOT NULL,
   email        VARCHAR(50) UNIQUE NOT NULL,
   phone        VARCHAR(50),
   address      VARCHAR(50),
   name         VARCHAR(50) NOT NULL,
   status       VARCHAR(50) NOT NULL,
   created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
