select * from public.notas
INSERT INTO public.notas(idalumno, idcurso, "descNota") VALUES (1, 1, 'Backend');
UPDATE public.notas SET idalumno=1, idcurso=1, "descNota"='developer' WHERE idnotas=1;
DELETE FROM public.notas WHERE idnotas=1;