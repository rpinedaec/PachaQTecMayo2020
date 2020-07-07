INSERT INTO empresa (rucEmpresa, nombreEmpresa)
VALUES
('20601137985',
 'UNAY');
SELECT idempresa,
    rucEmpresa as RUC,
    nombreEmpresa as NOMBRE
FROM empresa where rucEmpresa = '20601137985';
UPDATE empresa
SET
rucEmpresa = '20602157432',
nombreEmpresa = 'Antikuna'
WHERE idempresa = 1;
DELETE FROM empresa
WHERE idempresa = 2;


