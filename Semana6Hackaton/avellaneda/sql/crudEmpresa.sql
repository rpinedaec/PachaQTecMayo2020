-- CRUD
-- empresa
INSERT INTO empresa (rucEmpresa, nombreEmpresa) VALUES ('2019181716', 'PachaQtec');
SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa;
SELECT idempresa, rucEmpresa as RUC, nombreEmpresa as Nombre FROM empresa where rucEmpresa = '2019181716';
UPDATE empresa SET rucEmpresa = '2021222324', nombreEmpresa = 'PachaQtec9000' WHERE idempresa = 1;
DELETE FROM empresa WHERE idempresa = 1;