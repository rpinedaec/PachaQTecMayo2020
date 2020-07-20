select * from semestre;
INSERT INTO public.semestre("descSemestre") VALUES ('2020-1');
UPDATE public.semestre SET "descSemestre"='2020-secuencial' WHERE idsemestre=1;
DELETE FROM public.semestre WHERE idsemestre=1;