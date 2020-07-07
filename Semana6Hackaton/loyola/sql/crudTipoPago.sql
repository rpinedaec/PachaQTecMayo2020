INSERT INTO tipopago(descTipoPago)VALUES('Efectivo');

Select idtipopago,
descTipoPago as Descripcion
from tipopago;
Select idtipopago,
descTipoPago as Descripcion
from tipopago where descTipoPago = 'Efectivo';

update tipopago set descTipoPago = 'Credito' where idtipopago = 1;
delete from tipopago where idtipopago = 1;

