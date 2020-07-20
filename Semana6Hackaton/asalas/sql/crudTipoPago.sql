INSERT INTO tipopago(desctipoPago)VALUES('Efectivo');

Select idtipopago,
desctipoPago as Descripcion
from tipopago;

Select idtipopago,
desctipoPago as Descripcion
from tipopago where desctipoPago = 'Efectivo';

update tipopago set desctipoPago = 'Credito' where idtipopago = 1;
delete from tipopago where idtipopago = 1;

