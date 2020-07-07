INSERT INTO tipoPago (descTipoPago) VALUES ('Efectivo');
SELECT idtipoPago, descTipoPago as Descripcion FROM tipoPago;
SELECT idtipoPago, descTipoPago as Descripcion FROM tipoPago WHERE descTipoPago = 'Efectivo';
UPDATE tipoPago SET descTipoPago = 'Cash' WHERE idtipoPago = 1;
DELETE FROM idtipoPago WHERE idtipoPago = 1;