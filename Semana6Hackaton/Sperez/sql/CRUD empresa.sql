INSERT INTO empresa (rucEmpresa, nombreEmpresa) VALUES (28374625637,'J&S emprendedores');
SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa where rucEmpresa = 2837462563;
UPDATE empresa SET rucEmpresa = 56473890213, nombreEmpresa = 'JyS ganadores' WHERE idempresa = 1;
DELETE FROM empresa WHERE idempresa = 1;




