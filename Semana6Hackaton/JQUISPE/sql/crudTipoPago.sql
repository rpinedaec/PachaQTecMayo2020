INSERT INTO tipopago(descTipoPago)VALUES('Efectivo');
SELECT idtipopago, descTipoPago AS Descripcion FROM tipopago;
SELECT idtipopago, descTipoPago AS Descripcion FROM tipopago WHERE descTipoPago = 'Efectivo';
UPDATE tipopago SET descTipoPago = 'Credito' WHERE idtipopago = 1;
DELETE FROM tipopago WHERE idtipopago = 1;