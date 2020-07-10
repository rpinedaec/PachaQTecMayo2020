select * from public.curso
INSERT INTO public.curso("nombreCurso", idprofesor, idsemestre) VALUES ('Backend', 1, 1);
UPDATE public.curso SET  "nombreCurso"='Backend con Python', idprofesor=1, idsemestre=1 WHERE idcurso=1;
DELETE FROM public.curso WHERE idcurso=1;