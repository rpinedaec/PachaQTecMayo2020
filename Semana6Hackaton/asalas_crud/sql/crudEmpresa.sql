
INSERT INTO empresa
(
rucempresa,
nomempresa)
VALUES
('20202020',
'prueba');

select idempresa, rucempresa as RUC, nomempresa as Nombre from empresa;

select idempresa, rucempresa as RUC, nomempresa as Nombre from empresa where rucempresa='20202020';

UPDATE empresa
SET
rucempresa = '21212121',
nomempresa = 'Pachaqutec2'
WHERE idempresa = 1;

delete from empresa where idempresa=1

