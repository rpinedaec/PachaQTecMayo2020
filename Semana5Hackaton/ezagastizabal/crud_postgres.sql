SELECT * FROM alumnos
INSERT INTO alumnos (nombre_alumno,edad_alumno,correo_alumno) VALUES('Edwin Zagastizabal','27','eazg@gmail.com');
UPDATE alumnos SET correo_alumno = 'edwin.zagastizabal@gmail.com' WHERE id_alumno = 1;
DELETE FROM alumnos WHERE id_alumno = 1

SELECT * FROM profesor
INSERT INTO profesor(nombre_profesor, edad_profesor, correo_profesor) VALUES('Alberto Pineda','35','rp@gmail,com');
UPDATE profesor SET nombre_profesor = 'Roberto Pineda' WHERE id_profesor = 1;
DELETE FROM profesor WHERE id_profesor = 1

SELECT * FROM semestre
INSERT INTO semestre (desc_semestre) VALUES ('2020-1');
UPDATE semestre SET desc_semestre = '2020-I' WHERE id_semestre = 1;
DELETE FROM semestre WHERE id_semestre = 1

SELECT * FROM curso
INSERT INTO curso (nombre_curso, profesor_curso, id_profesor, id_semestre) VALUES('Back-end','Roberto Pineda',2,2);
UPDATE curso SET nombre_curso = 'Desarrollo Back-end' WHERE id_curso = 1;
DELETE FROM curso WHERE id_curso = 1

SELECT * FROM notas
INSERT INTO notas (desc_notas,id_alumno,id_curso) VALUES ('Aprobado',2,2);
UPDATE notas SET desc_notas = 'Desaprobado' WHERE id_alumno = 2
DELETE FROM notas WHERE id_alumno = 2