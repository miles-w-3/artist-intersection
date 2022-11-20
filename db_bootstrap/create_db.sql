CREATE DATABASE ART_INTERSECTION;
GRANT ALL PRIVILEGES ON ART_INTERSECTION.* TO 'webapp'@'%';
FLUSH PRIVILEGES;

USE ART_INTERSECTION;

-- Artist definitions
CREATE TABLE WorkType (
  type_id INT NOT NULL auto_increment,
  type_name VARCHAR(50) NOT NULL,

  CONSTRAINT pk PRIMARY KEY (type_id)
);

CREATE TABLE Artist (
  artist_id INT NOT NULL auto_increment,
  name VARCHAR(50) NOT NULL,
  favorite_works_id INT NOT NULL,
  date_of_birth DATE,
  num_works_sold INT NOT NULL DEFAULT 0,
  total_commission_amt DECIMAL(13, 2) DEFAULT 0.00,
  location VARCHAR(30) NOT NULL,

  CONSTRAINT pk PRIMARY KEY (artist_id),
  CONSTRAINT fk_artist_favorite FOREIGN KEY (favorite_works_id)
    REFERENCES WorkType (type_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE TABLE Collector (
  collector_id INT NOT NULL auto_increment,
  name VARCHAR(50) NOT NULL,
  favorite_works_id INT NOT NULL,
  date_of_birth DATE,
  num_works_purchased INT NOT NULL DEFAULT 0,
  total_spend_amt DECIMAL(13, 2) DEFAULT 0.00,

  CONSTRAINT pk PRIMARY KEY (collector_id),
  CONSTRAINT fk_collector_favorite FOREIGN KEY (favorite_works_id)
    REFERENCES WorkType (type_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT

);

CREATE TABLE Works (
  work_id INT NOT NULL auto_increment,
  work_type_id INT NOT NULL,
  creator_id INT NOT NULL,
  title VARCHAR(30) NOT NULL,
  date_created DATETIME DEFAULT CURRENT_TIMESTAMP,
  current_price DECIMAL(13, 2),
  purchsed_by_id INT,

  CONSTRAINT pk PRIMARY KEY (work_id),
  CONSTRAINT fk_work_type FOREIGN KEY (work_type_id)
    REFERENCES WorkType (type_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_created_by FOREIGN KEY (creator_id)
    REFERENCES Artist (artist_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_purchased_by FOREIGN KEY (purchsed_by_id)
    REFERENCES Collector (collector_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE TABLE Admin (
  name VARCHAR(50) NOT NULL,
  admin_id INT NOT NULL auto_increment,
  date_of_birth DATE,

  CONSTRAINT pk PRIMARY KEY (admin_id)
);

CREATE TABLE SuspendedArtist (
  suspended_id INT NOT NULL,
  suspended_by INT NOT NULL,
  reason VARCHAR(200),

  CONSTRAINT fk_artist FOREIGN KEY (suspended_id)
    REFERENCES Artist (artist_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_admin FOREIGN KEY (suspended_by)
    REFERENCES Admin (admin_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);


CREATE TABLE CommissionRequest (
  title VARCHAR(50) NOT NULL,
  info TEXT NOT NULL,
  request_id INT NOT NULL auto_increment,
  work_type_id INT NOT NULL,
  requestor INT NOT NULL,
  accepted_id INT,

  CONSTRAINT fk_commission_type FOREIGN KEY (work_type_id)
    REFERENCES WorkType (type_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT fk_requestor FOREIGN KEY (requestor)
    REFERENCES Collector (collector_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT fk_accepted FOREIGN KEY (accepted_id)
    REFERENCES Artist (artist_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT pk PRIMARY KEY (request_id)
);

-- Insert work types
INSERT INTO WorkType (type_name)
VALUES ('Mixed Media'), ('Painting'), ('Sculpture'), ('Drawing');

-- Insert Artist values
INSERT INTO Artist (name, favorite_works_id, date_of_birth, location)
VALUES ('Thomas Redman', 4, '1950-05-15', 'Zaragoza'),
  ('Alyce Romaint', 4, '1979-11-2', 'Aranitas'),
  ('Larry Sesser', 1, '1992-12-10', 'Lazaro Cardenas'),
  ('Claude Wearne', 2, '1935-05-31', 'Guayabal'), ('Katharina Goadby', 3, '1987-06-14', 'Gamagōri'),
  ('Vonnie Larkin', 3, '1989-04-09', 'Quimbaya'), ('Peirce Woolger', 4, '1946-06-03', 'Buzen'),
  ('Oralie Stranaghan', 3, '1951-02-15', 'Kajar'), ('Ives Button', 2, '1942-02-09', 'Kiev'),
  ('Herrick Fursey', 3, '1945-08-22', 'Xijiao');

-- Insert Artist Works
INSERT INTO Works (title, work_type_id, creator_id, current_price)
VALUES ('Stronghold', 1, 2, 7680.86), ('Fintone', 4, 4, 500.39),
  ('Konklab', 3, 7, 2822.66), ('Prodder', 3, 9, 4797.51), ('Y-find', 3, 7, 2748.58),
  ('Matsoft', 4, 6, 5348.33), ('Opela', 2, 4, 7878.03), ('Domainer', 4, 1, 6244.83),
  ('Daltfresh', 1, 8, 6694.75), ('Konklab', 1, 5, 6002.78);

-- Insert Admin
INSERT INTO Admin (name, date_of_birth)
VALUES ('Margalit Lipsett', '1981-03-05'), ('Kory Smallcombe', '1994-10-14'),
('Gussy Tinkham', '194-08-21'), ('Graham Boyn', '1936-12-08'),
('Lisette Pheby', '1967-06-01'), ('Tammi Perkis', '1975-03-13'),
('Nertie Trevor', '1998-11-07'), ('Yoshi Willerton', '1973-10-05'),
('Donny Arundale', '1947-01-16'), ('Pattie Severn', '1989-04-06');

-- Insert SuspendedArtist
INSERT INTO SuspendedArtist (suspended_id, suspended_by, reason)
VALUES (1, 1, "This is a test of the system, nothing personal");

-- Insert Collector
INSERT INTO Collector (name, favorite_works_id, date_of_birth)
VALUES ('Ashlie Ayrton', 2, '1995-06-13'), ('Marty Merrikin', 4, '1976-08-29'),
('Betsey Keizman', 1, '1970-10-24'), ('Ramsay Slayny', 3, '2000-05-17'),
('Sigvard Cristofor', 4, '1990-09-13'), ('Zonnya Oade', 1, '1951-06-16'),
('Carmina Kleinhaut', 4, '1985-07-29'), ('Tina Inchley', 3, '1977-02-21'),
('Maisey Cockshot', 4, '1974-04-09'), ('Shurlock Jerwood', 3, '1974-07-29');

-- Insert CommissionRequest
INSERT INTO CommissionRequest (title, info, work_type_id, requestor)
VALUES ('It', 'libero convallis eget eleifend luctus ultricies eu nibh quisque id justo', 2, 4),
  ('Mat Lam Tam', 'rutrum ac lobortis vel dapibus at diam nam tristique tortor eu', 3, 1),
  ('Zamit', 'nisl ut volutpat sapien arcu sed augue aliquam erat volutpat in congue etiam justo etiam pretium iaculis justo in', 3, 7),
  ('Toughjoyfax', 'sem mauris laoreet ut rhoncus aliquet pulvinar sed nisl nunc rhoncus dui vel', 3, 10),
  ('Namfix', 'tincidunt lacus at velit vivamus vel nulla eget eros elementum pellentesque quisque porta volutpat', 1, 2),
  ('Otcom', 'sapien quis libero nullam sit amet turpis elementum ligula vehicula consequat morbi a ipsum integer a nibh', 3, 2),
  ('Latlux', 'suspendisse accumsan tortor quis turpis sed ante vivamus tortor duis mattis egestas metus aenean fermentum', 2, 3),
  ('Tresom', 'blandit lacinia erat vestibulum sed magna at nunc commodo placerat', 1, 4),
  ('Fix San', 'ac nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit ligula in lacus curabitur', 2, 10),
  ('Hatity', 'molestie nibh in lectus pellentesque at nulla suspendisse potenti cras in', 1, 1);


