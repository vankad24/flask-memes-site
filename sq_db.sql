CREATE TABLE IF NOT EXISTS users(
  id integer PRIMARY KEY AUTOINCREMENT,
  nickname text NOT NULL,
  password text NOT NULL
);

CREATE TABLE IF NOT EXISTS posts(
  id integer PRIMARY KEY AUTOINCREMENT,
  user_nick integer NOT NULL,
  message text,
  image text NOT NULL,
  likes integer,
  dislikes integer,
  time text NOT NULL,
  FOREIGN KEY (user_nick) REFERENCES users(nickname)
);
INSERT INTO users(id, nickname, password) VALUES('0', 'Admin', '12345');
