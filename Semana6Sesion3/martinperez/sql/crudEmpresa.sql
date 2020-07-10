

INSERT INTO empresa(rucEmpresa,nombreEmpresa)
VALUES ('20222525252','Pachaqtec Clases');

SELECT idempresa,rucEmpresa as RUC,nombreEmpresa as Nombre FROM empresa;

SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa where rucEmpresa = '20222525252';

UPDATE empresa SET
    rucEmpresa = '2121212121',
    nombreEmpresa  = 'Pachaqtec2'
    WHERE idempresa = 1;

DELETE FROM empresa
WHERE idEmpresa = 2;

