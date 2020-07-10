

INSERT INTO empresa
(
rucEmpresa,
nombreEmpresa)
VALUES
('2020202020202',
'UNI SA');
SELECT idempresa,
    rucEmpresa as RUC,
    nombreEmpresa as Nombre
FROM empresa;
SELECT idempresa,
    rucEmpresa as RUC,
    nombreEmpresa as Nombre
FROM empresa where rucEmpresa = '25457858789' ;
UPDATE empresa
SET
rucEmpresa = '25457858789',
nombreEmpresa  = 'Lima SA'
WHERE idempresa = 1;
DELETE FROM empresa
WHERE idEmpresa = 2;

