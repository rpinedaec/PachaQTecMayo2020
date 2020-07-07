INSERT INTO empresa
(
rucEmpresa,
nombreEmpresa)
VALUES
('12345678901',
'Pachaqtec');
SELECT idempresa,
    rucEmpresa as RUC,
    nombreEmpresa as Nombre
FROM empresa;
SELECT idempresa,
    rucEmpresa as RUC,
    nombreEmpresa as Nombre
FROM empresa where rucEmpresa = '12345678901' ;
UPDATE empresa
SET
rucEmpresa = '10987654321',
nombreEmpresa  = 'Pachaqtec2'
WHERE idempresa = 1;
DELETE FROM empresa
WHERE idEmpresa = 2;