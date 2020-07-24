SELECT * FROM public.profesor;
INSERT INTO public.profesor("nombreProfesor", "edadProfesor", "correoProfesor") VALUES ( 'rOBERTO PINEDA', 37, 'ACASC');
UPDATE public.profesor SET  "nombreProfesor" = 'ROBERT PINEDA', "edadProfesor"=36, "correoProfesor"='aa@' WHERE idprofesor=1;
DELETE FROM public.profesor WHERE idprofesor=1;