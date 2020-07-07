select * from public.salon
INSERT INTO public.salon("nombreSalon", idalumno, idprofesor) VALUES ('Virtual_5A',1, 1);
UPDATE public.salon SET "nombreSalon"='Virtual_4A', idalumno=1, idprofesor=1 WHERE idsalon=1
DELETE FROM public.salon WHERE idsalon=1;