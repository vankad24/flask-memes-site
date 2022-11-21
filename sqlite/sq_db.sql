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
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(0, 0, "Oops, I posted water", 'war_and_peace.jpg', 11, 0, '18-11-2022 21:22');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(1, 0, 'Python', '001.jpg', 6, 0, '18-11-2022 21:22');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(2, 1, 'Hahahahhhaha-hahahah', 'ha-ha.jpeg', 7, 0, '19-11-2022 12:11');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(3, 24, 'The best meme', 'cpp.jpg', 2000, 0, '20-11-2022 21:55');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(4, 24, '', 'dragon.jpg', 24, 0, '20-11-2022 21:55');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(5, 24, '', 'bob.jpg', 35, 0, '20-11-2022 23:00');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(6, 24, '', 'chrome.jpg', 70, 0, '20-11-2022 23:00');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(7, 24, '', 'cpp2.jpg', 80, 0, '20-11-2022 23:00');
INSERT INTO posts(id, id_user, message, image, likes, dislikes, time) VALUES(8, 24, '', 'python2.jpg', 75, 0, '20-11-2022 23:00');
