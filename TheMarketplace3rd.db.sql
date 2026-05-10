BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Categories" (
	"catId"	INTEGER NOT NULL UNIQUE,
	"category"	TEXT NOT NULL,
	PRIMARY KEY("catId" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "Product" (
	"productId"	INTEGER NOT NULL,
	"productName"	TEXT NOT NULL,
	"productDesc"	TEXT,
	"productImage"	TEXT NOT NULL,
	"productLocation"	TEXT NOT NULL,
	"price"	INTEGER,
	"createdAt"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"createdBy"	INTEGER NOT NULL,
	"productCategory"	INTEGER,
	PRIMARY KEY("productId" AUTOINCREMENT),
	FOREIGN KEY("createdBy") REFERENCES "User"("userId"),
	FOREIGN KEY("productCategory") REFERENCES "Categories"("catId")
);
CREATE TABLE IF NOT EXISTS "User" (
	"userId"	INTEGER NOT NULL UNIQUE,
	"firstName"	TEXT NOT NULL,
	"lastName"	TEXT,
	"location"	TEXT NOT NULL,
	"createdAt"	TEXT NOT NULL DEFAULT current_timestamp,
	PRIMARY KEY("userId" AUTOINCREMENT)
);
INSERT INTO "Categories" VALUES (1,'Vehicle');
INSERT INTO "Categories" VALUES (2,'Tech');
INSERT INTO "Categories" VALUES (3,'Home');
INSERT INTO "Product" VALUES (1,'Audi A3','110,000 Miles, Good conditon','car.png','Brighton',10000,'2026-05-06 10:34:34',3,1);
INSERT INTO "Product" VALUES (2,'Mercedes C Class','70,000 Miles, Good runner some dings, call to find out more','car.png','Brighton',8000,'2026-05-06 10:36:17',2,1);
INSERT INTO "Product" VALUES (3,'BMW 220i','30,0000 Miles','car.png','Brighton',9000,'2026-05-06 10:37:00',1,1);
INSERT INTO "Product" VALUES (4,'Vauxhall Corsa','130,000 Miles','car.png','Brighton',3000,'2026-05-06 10:37:32',1,1);
INSERT INTO "Product" VALUES (5,'Nissan Micra','60,000 Miles','car.png','Brighton',1000,'2026-05-06 10:37:57',6,1);
INSERT INTO "Product" VALUES (6,'Nissan 300zx','100,000 Miles','car.png','Brighton',12000,'2026-05-06 10:38:34',5,1);
INSERT INTO "Product" VALUES (7,'Kettle','brand new never used','car.png','Brighton',20,'2026-05-06 10:50:12',8,3);
INSERT INTO "Product" VALUES (8,'Ironing Board','lightly used','car.png','Brighton',5,'2026-05-06 10:50:59',10,3);
INSERT INTO "Product" VALUES (9,'Laptop','Upgraded no longer needed','car.png','Brighton',100,'2026-05-06 10:51:45',10,2);
INSERT INTO "Product" VALUES (10,'TV','40" LCD','car.png','Brighton',30,'2026-05-06 10:52:11',11,2);
INSERT INTO "Product" VALUES (11,'Apple TV 4k','','car.png','Brighton',100,'2026-05-06 10:52:30',11,2);
INSERT INTO "Product" VALUES (12,'iPhone 13','good condition some scratches to screen','car.png','Brighton',100,'2026-05-06 10:53:16',2,2);
INSERT INTO "Product" VALUES (13,'Keyboard and Mouse','good condition','car.png','Brighton',10,'2026-05-06 10:53:41',2,2);
INSERT INTO "Product" VALUES (14,'iPod Classic 7th gen','needs battery replacement','car.png','Brighton',40,'2026-05-06 10:54:24',3,2);
INSERT INTO "User" VALUES (1,'James','Harding','Brighton','2026-05-06 10:17:53');
INSERT INTO "User" VALUES (2,'Keely','Wesling','Brighton','2026-05-06 10:18:31');
INSERT INTO "User" VALUES (3,'Fred','James','Hove','2026-05-06 10:18:53');
INSERT INTO "User" VALUES (4,'Kass','Nova','Brighton','2026-05-06 10:19:19');
INSERT INTO "User" VALUES (5,'Jessica','Mitchell','Hove','2026-05-06 10:19:36');
INSERT INTO "User" VALUES (6,'Jeff','Wise','Brighton','2026-05-06 10:20:14');
INSERT INTO "User" VALUES (7,'Patrick','Nice','Brighton','2026-05-06 10:39:07');
INSERT INTO "User" VALUES (8,'Nick','Long','Brighton','2026-05-06 10:39:38');
INSERT INTO "User" VALUES (9,'Flint','Stone','Brighton','2026-05-06 10:40:02');
INSERT INTO "User" VALUES (10,'Michael','Scott','Brighton','2026-05-06 10:40:11');
INSERT INTO "User" VALUES (11,'Dwight','Shrute','Hove','2026-05-06 10:40:31');
COMMIT;
