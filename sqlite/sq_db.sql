CREATE TABLE IF NOT EXISTS users(
  id integer PRIMARY KEY AUTOINCREMENT,
  nickname text NOT NULL,
  password text NOT NULL
);

CREATE TABLE IF NOT EXISTS posts(
  id integer PRIMARY KEY AUTOINCREMENT,
  id_user integer NOT NULL,
  message text,
  image text NOT NULL,
  likes integer,
  dislikes integer,
  time text NOT NULL,
  FOREIGN KEY (id_user) REFERENCES users(id)
);
INSERT INTO users(id, nickname, password) VALUES(0, 'Admin', '12345');
INSERT INTO users(id, nickname, password) VALUES(1, 'Melon21', 'melon21');
INSERT INTO users(id, nickname, password) VALUES(24, 'Vanka', '242424');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(0, 0, "Ой, воду запостил", 'war_and_peace.jpg', 0, 0, '18-11-2022 21:22');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(1, 0, 'Python', '001.jpg', 0, 0, '18-11-2022 21:22');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(2, 1, 'Hahahahhhaha-hahahah', 'ha-ha.jpeg', 0, 0, '19-11-2022 12:11');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(3, 24, 'Жиза', 'cpp.jpg', 100, 0, '20-11-2022 21:55');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(4, 24, '', 'dragon.jpg', 24, 0, '20-11-2022 21:55');
