'''listar nombre de alumnos con apoderados'''
select nom_alumno,nom_apoderado from alumno inner join apoderado on alumno.apoderado_idapoderado = apoderado.idapoderado