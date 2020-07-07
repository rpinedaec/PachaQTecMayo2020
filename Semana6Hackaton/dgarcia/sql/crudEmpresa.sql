
INSERT INTO empresa
(rucEmpresa,
nombreEmpresa)
VALUES
('202020202020',
'Pachaqtec');
SELECT idempresa,
    rucEmpresa as RUC,
	nombreEmpresa as Nombre,
    created_at as creado,
    updated_at as actualizado
FROM empresa WHERE rucEmpresa = '202020202020';
UPDATE empresa
SET
rucEmpresa = '212121212121',
nombreEmpresa = 'Pachaqtec2'
WHERE idempresa = 1 ;
DELETE FROM empresa
WHERE idempresa = 1 ;



