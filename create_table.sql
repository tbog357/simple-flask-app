CREATE TABLE CUSTOMER(
   id           serial PRIMARY KEY NOT NULL,
   email        VARCHAR(50)  UNIQUE  NOT NULL,
   phone        VARCHAR(50) ,
   address      VARCHAR(50),
   name         VARCHAR(50) NOT NULL,
   status       VARCHAR(50) NOT NULL,
   created_at
   updated_at
);
