CREATE DATABASE db_ezagastizabal

CREATE TABLE IF NOT EXISTS alumnos(
id_alumno SERIAL,
nombre_alumno VARCHAR(150) NOT NULL,
edad_alumno INT NOT NULL,
correo_alumno VARCHAR(100) NOT NULL,
PRIMARY KEY(id_alumno)
)

CREATE TABLE IF NOT EXISTS profesor(
id_profesor SERIAL,
nombre_profesor VARCHAR(150) NOT NULL,
edad_profesor INT NOT NULL,
correo_profesor VARCHAR(100) NOT NULL,
PRIMARY KEY (id_profesor)
)

CREATE TABLE IF NOT EXISTS salon(
id_salon SERIAL,
nombre_salon VARCHAR(100) NOT NULL,
PRIMARY KEY (id_salon),
id_alumno INT NOT NULL,
FOREIGN KEY(id_alumno)
REFERENCES alumnos(id_alumno),
id_profesor INT NOT NULL,
FOREIGN KEY(id_profesor)
REFERENCES profesor(id_profesor)
)

CREATE TABLE IF NOT EXISTS semestre(
id_semestre SERIAL,
desc_semestre VARCHAR(100) NOT NULL,
PRIMARY KEY(id_semestre)
)

CREATE TABLE IF NOT EXISTS curso(
id_curso SERIAL,
nombre_curso VARCHAR(100) NOT NULL,
profesor_curso VARCHAR(150) NOT NULL,
PRIMARY KEY(id_curso),
id_profesor INT NOT NULL,
FOREIGN KEY(id_profesor)
REFERENCES profesor(id_profesor),
id_semestre INT NOT NULL,
FOREIGN KEY(id_semestre)
REFERENCES semestre(id_semestre)
)

CREATE TABLE IF NOT EXISTS notas(
id_notas SERIAL,
desc_notas VARCHAR(100) NOT NULL,
PRIMARY KEY (id_notas),
id_alumno INT NOT NULL,
FOREIGN KEY (id_alumno)
REFERENCES alumnos(id_alumno),
id_curso INT NOT NULL,
FOREIGN KEY (id_curso)
REFERENCES curso(id_curso)
)
