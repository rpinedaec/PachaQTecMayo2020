CREATE DATABASE colegio;

CREATE TABLE alumno(
id_alumno SERIAL PRIMARY KEY NOT NULL,
nombre_alumno VARCHAR(25) NOT NULL,
edad_alumno INT NOT NULL,
correo_alumno VARCHAR(25) NOT NULL
);

CREATE TABLE profesor(
id_profesor SERIAL NOT NULL PRIMARY KEY,
nombre_profesor varchar(25) NOT NULL,
edad_profesor INT NOT NULL,
correo_profesor varchar(25) NOT NULL
);

CREATE TABLE salon(
id_salon SERIAL NOT NULL PRIMARY KEY,
nombre_salon VARCHAR(25) NOT NULL
);

CREATE TABLE curso(
id_curso SERIAL NOT NULL PRIMARY KEY,
nombre_curso VARCHAR(25) NOT NULL
);

CREATE TABLE ano(
id_año SERIAL PRIMARY KEY NOT NULL,
nombre_año INT NOT NULL
);

CREATE TABLE nota(
id_nota SERIAL NOT NULL PRIMARY KEY,
valor_nota INT NOT NULL
)

CREATE TABLE bimestre(
id_bimestre SERIAL NOT NULL PRIMARY KEY,
nombre_bimestre VARCHAR(25),
fecha_inicio DATE NOT NULL,
fecha_fin DATE NOT NULL
);

ALTER TABLE alumno
ADD id_salon INT,
ADD FOREIGN KEY (id_salon) REFERENCES salon(id_salon);

ALTER TABLE salon
ADD id_profesor INT,
ADD FOREIGN KEY (id_profesor) REFERENCES profesor(id_profesor);

ALTER TABLE salon
ADD id_año INT,
ADD FOREIGN KEY (id_año) REFERENCES ano(id_año)

ALTER TABLE nota
ADD id_bimestre INT,
ADD FOREIGN KEY(id_bimestre) REFERENCES bimestre(id_bimestre);

ALTER TABLE nota
ADD id_año INT,
ADD FOREIGN KEY(id_año) REFERENCES ano(id_año);

ALTER TABLE nota
ADD id_alumno INT,
ADD FOREIGN KEY(id_alumno) REFERENCES alumno(id_alumno);

ALTER TABLE nota
ADD id_curso INT,
ADD FOREIGN KEY(id_curso) REFERENCES curso(id_curso);

ALTER TABLE bimestre
ADD id_año INT,
ADD FOREIGN KEY(id_año) REFERENCES ano(id_año);

ALTER TABLE curso
ADD id_profesor INT,
ADD FOREIGN KEY(id_profesor) REFERENCES profesor(id_profesor);

INSERT INTO ano(nombre_año)
VALUES 
	(2019),
	(2020);

INSERT INTO bimestre(nombre_bimestre,fecha_inicio,fecha_fin,id_año)
VALUES
	('I','01/03/2019','01/05/2019',1),
	('II','01/05/2019','01/07/2019',1),
	('II','01/07/2019','01/09/2019',1),
	('IV','01/03/2019','01/05/2019',1),
	('I','01/03/2020','01/05/2020',2),
	('II','01/05/2020','01/07/2020',2),
	('II','01/07/2020','01/09/2020',2),
	('IV','01/03/2020','01/05/2020',2);
	
INSERT INTO profesor(nombre_profesor,edad_profesor,correo_profesor)
VALUES
	('Roberto Pineda',35,'rpecu@gmail.com'),
	('Braulio Berlanga',27,'bberlanga@gmail.com'),
	('Pepito Perez',45,'pperez@gmail.com'),
	('Yola Polastri',65,'burbujitas@gmail.com');

INSERT INTO curso(nombre_curso,id_profesor)
VALUES
	('Matematicas Avanzadas',4),
	('SQL',1),
	('Como ser astronauta',2),
	('Alquimia',2),
	('Como ser maestro pokemon',4);

INSERT INTO salon(nombre_salon,id_profesor,id_año)
VALUES
	('A',1,2),
	('B',2,2),
	('C',3,2),
	('D',4,2);

INSERT INTO alumno(nombre_alumno,edad_alumno,correo_alumno,id_salon)
VALUES
	('Alejandro Toledo',15,'wishkyummy@gmail.com',1),
	('Pikachu Pokemon',14,'pikapika@gmail.com',1),
	('Micky Raton',14,'walt@gmail.com',1),
	('Martin Paredes',15,'martinp@gmail.com',1),
	('Lucia Linares',16,'llinares@gmail.com',1),
	('Leo Messi',17,'wishkyummy@gmail.com',2),
	('Carlos Carracedo',15,'wishkyummy@gmail.com',2),
	('Elias Perez',14,'wishkyummy@gmail.com',2),
	('Mirko Barack',14,'wishkyummy@gmail.com',2),
	('Boris Romero',15,'wishkyummy@gmail.com',2),
	('Power Ranger Rojo',17,'wishkyummy@gmail.com',3),
	('Arturito Walker',18,'wishkyummy@gmail.com',3),
	('Pablito Escobar',18,'wishkyummy@gmail.com',3),
	('Maria Pia Copello',14,'wishkyummy@gmail.com',3),
	('Magaly Medina',15,'wishkyummy@gmail.com',3),
	('Helga Pataki',15,'wishkyummy@gmail.com',4),
	('Mirian Matos',14,'wishkyummy@gmail.com',4),
	('Martha Schneider',15,'wishkyummy@gmail.com',4),
	('Carol Lituma',13,'wishkyummy@gmail.com',4);

INSERT INTO nota(valor_nota,id_bimestre,id_año,id_alumno,id_curso)
VALUES
	(ROUND(8+random()*100*0.1),53,2,1,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,2,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,3,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,4,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,5,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,6,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,7,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,8,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,9,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,10,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,11,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,12,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,13,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,14,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,15,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,16,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,17,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,18,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,19,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,1,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,2,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,3,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,4,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,5,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,6,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,7,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,8,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,9,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,10,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,11,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,12,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,13,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,14,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,15,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,1,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,2,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,3,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),53,2,4,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,5,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,6,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,7,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,8,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,9,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,10,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,11,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,12,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,13,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,14,ROUND(random()*100*0.04)+1),
	(ROUND(8+random()*100*0.1),54,2,15,ROUND(random()*100*0.04)+1);

SELECT nota.valor_nota,alumno.nombre_alumno,bimestre.nombre_bimestre,curso.nombre_curso FROM nota
INNER JOIN alumno on nota.id_alumno=alumno.id_alumno
INNER JOIN bimestre on nota.id_bimestre=bimestre.id_bimestre
INNER JOIN curso on nota.id_curso=curso.id_curso
	
	
	
	

	

