select * from alumno;
INSERT INTO public.alumno("nombreAlumno", "edadAlumno", "correoAlumno") VALUES ('Anival Salas', 33, 'anibals2012@gmail.com');
UPDATE public.alumno SET "nombreAlumno"='asalas', "edadAlumno"=30, "correoAlumno"='anibals2012@gmail.com' WHERE idalumno=1;
DELETE FROM public.alumno WHERE idalumno=1;