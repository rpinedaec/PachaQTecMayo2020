INSERT INTO tipopago(descTipoPago)VALUES('Efectivo');

Select idtipoPago,
descTipoPago as Descripcion,
created_at as creado,
updated_at as actualizado
from tipopago;
Select idtipopago,
descTipoPago as Descripcion,
created_at as creado,
updated_at as actualizado
from tipopago where descTipoPago = 'Efectivo';

update tipopago set descTipoPago = 'Credito' where idtipoPago = 1;
delete from tipopago where idtipoPago = 1;
