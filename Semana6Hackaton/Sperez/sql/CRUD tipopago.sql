INSERT INTO tipopago(descTipoPago) VALUES('Efectivo');
SELECT idtipoPago, descTipoPago as Descripcion FROM tipopago;
SELECT idtipoPago, descTipoPago as Descripcion FROM tipopago where descTipoPago = 'Efectivo';
UPDATE tipopago SET descTipoPago = 'Credito' WHERE idtipoPago = 1;
DELETE FROM tipopago WHERE idtipoPago = 1;


