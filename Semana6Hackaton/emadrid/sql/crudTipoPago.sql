INSERT INTO tipopago(descTipoPago)VALUES('Tarjeta');

Select idtipopago,
descTipoPago as Descripcion
from tipopago;
Select idtipopago,
descTipoPago as Descripcion
from tipopago where descTipoPago = 'Tarjeta';

update tipopago set descTipoPago = 'Efectivo' where idtipopago = 1;
delete from tipopago where idtipopago = 1;

