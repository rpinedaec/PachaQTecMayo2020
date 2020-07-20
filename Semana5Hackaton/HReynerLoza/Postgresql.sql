/*

HENNIO REYNER LOZA 

*/
CREATE TABLE alumnos (
    alumno_id SERIAL PRIMARY KEY,
    alumno_nombre VARCHAR(30) NOT NULL,
    alumno_apellido VARCHAR(30) NOT NULL,
    alumno_fecha_nacimiento DATE,
    alumno_email VARCHAR(50) UNIQUE,
    alumno_pension NUMERIC (6, 2) NOT NULL,
    salon_id INT REFERENCES salones(salon_id);
);
CREATE TABLE salones (
    salon_id SERIAL PRIMARY KEY,
    profesor_id INT REFERENCES profesores(profesor_id),
    pabellon_id INT REFERENCES pabellones (pabellon_id)
);
CREATE TABLE pabellones(
    pabellon_id SERIAL PRIMARY KEY 
    pabellon_ubicacion VARCHAR(15),
);
CREATE TABLE profesores(
    profesor_id SERIAL PRIMARY KEY,
    profesor_nombre VARCHAR(30) NOT NULL,
    profesor_apellido VARCHAR(30) NOT NULL,
    profesor_fecha_nacimiento DATE,
    profesor_email VARCHAR(50) UNIQUE,
    profesor_sueldo NUMERIC(6, 2) NOT NULL,
);
CREATE TABLE alumnos_profesores (
    alumno_id INT REFERENCES alumnos(alumno_id),
    profesor_id INT REFERENCES profesores(profesor_id)
);
CREATE TABLE notas(
    nota_id SERIAL PRIMARY KEY,
    nota_valor NUMERIC (4, 2) NOT NULL,
    nota_fecha DATE NOT NULL,
    alumno_id INT REFERENCES alumnos(alumno_id),
    curso_id INT REFERENCES cursos(curso_id)
);
CREATE TABLE cursos (
    curso_id SERIAL PRIMARY KEY,
    curso_nombre VARCHAR(30) NOT NULL,
    curso_grado VARCHAR(10) NOT NULL,
    profesor_id INT REFERENCES profesores(profesor_id)
);