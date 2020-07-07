INSERT INTO tipopago
(descTipoPago)
VALUES
('Tarjeta');
SELECT idtipoPago as ID, descTipoPago as 'Tipo de pago'
FROM tipopago;
UPDATE tipopago
SET
descTipoPago = 'Efectivo'
WHERE idtipoPago = 1;
DELETE FROM tipopago
WHERE idtipoPago = 2;


