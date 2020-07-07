/*

HENNIO REYNER LOZA 

*/
CREATE TABLE IF NO EXISTS alumnos (
    alumno_id INT NOT NULL AUTO_INCREMENT,
    alumno_nombre VARCHAR(30) NOT NULL,
    alumno_apellido VARCHAR(30) NOT NULL,
    alumno_fecha_nacimiento DATE,
    alumno_email VARCHAR(50) UNIQUE,
    alumno_pension NUMERIC (6, 2) NOT NULL,
    PRIMARY KEY(alumno_id),
    FOREIGN KEY salones(salon_id)
);
CREATE TABLE salones (
    salon_id INT NOT NULL AUTO_INCREMENT,
    profesor_id INT NOT NULL profesores(profesor_id),
    pabellon_id INT NOT NULL pabellones (pabellon_id)
    PRIMARY KEY(salon_id),
    FOREIGN KEY profesores(profesor_id),
    FOREIGN KEY pabellones(pabellon_id)
);
CREATE TABLE pabellones(
    pabellon_id INT NOT NULL AUTO_INCREMENT,
    pabellon_ubicacion VARCHAR(15),
    PRIMARY KEY (pabellon_id)
);
CREATE TABLE profesores(
    profesor_id INT NOT NULL AUTO_INCREMENT,
    profesor_nombre VARCHAR(30) NOT NULL,
    profesor_apellido VARCHAR(30) NOT NULL,
    profesor_fecha_nacimiento DATE,
    profesor_email VARCHAR(50) UNIQUE,
    profesor_sueldo NUMERIC(6, 2) NOT NULL,
    PRIMARY KEY(profesor_id)
);
CREATE TABLE alumnos_profesores (

    FOREIGN KEY alumnos(alumno_id),
    FOREIGN KEY profesores(profesor_id)
    REFERENCES alumnos(alumno_id),
    REFERENCES profesores(profesor_id),
);
CREATE TABLE notas(
    nota_id INT NOT NULL AUTO_INCREMENT,
    nota_valor NUMERIC (4, 2) NOT NULL,
    nota_fecha DATE NOT NULL,
    PRIMARY KEY(nota_id)
    FOREIGN KEY alumnos(alumno_id),
    REFERENCES alumnos(alumno_id),
    FOREIGN KEY cursos(curso_id)
    REFERENCES cursos(curso_id)
);
CREATE TABLE cursos (
    curso_id INT NOT NULL AUTO_INCREMENT,,
    curso_nombre VARCHAR(30) NOT NULL,
    curso_grado VARCHAR(10) NOT NULL,
    PRIMARY KEY(curso_id)
    FOREIGN KEY profesores(profesor_id)
    REFERENCES profesores(profesor_id),
);