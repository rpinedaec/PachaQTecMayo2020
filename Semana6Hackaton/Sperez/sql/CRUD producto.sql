INSERT INTO productos(nombreProducto,valorProducto,igvProducto) VALUES ('Ropero',200.3,1);
SELECT idproducto, nombreProducto as Nombre, valorProducto as Precio, igvProducto as IGV FROM productos where igvProducto = 1;
UPDATE productos SET nombreProducto = 'Escritorio', valorProducto = 350.9, igvProducto = 2 WHERE idproducto = 1;
DELETE FROM productos WHERE idproducto = 1;


