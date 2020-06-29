-- SELECT INNER JOIN --  
SELECT
idnotas, "nombresAlumno", nombrecurso, descnota
FROM emadrid.notas nn inner join emadrid.alumno aa on nn.idalumno = aa.idalumno
								inner join emadrid.curso cc on nn.idcurso = cc.idcurso;

-- SELECT --                                
SELECT idnotas, idalumno, idcurso, descnota, nota1, nota2, nota3
	FROM emadrid.notas;

-- INSERT --    	
INSERT INTO emadrid.notas(
	idalumno, idcurso, descnota, nota1, nota2, nota3)
	VALUES (2, 2,upper('Aprobado'), 18, 15, 17);

-- UPDATE --    	
UPDATE emadrid.notas
	SET idalumno='3', idcurso='1', descnota=upper('aprobado'), nota1='15', nota2='16', nota3='19'
	WHERE idnotas=1;
    
-- DELETE --    	
DELETE FROM emadrid.notas
	WHERE idnotas=1;