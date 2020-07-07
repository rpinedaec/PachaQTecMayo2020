INSERT INTO productos
(nombreProducto,
 valorProducto,
 igvProducto)
VALUES
('Laptop',
 '5000.00',
 '18.00');
 SELECT idproductos,
	nombreProducto as Nombre,
    valorProducto as Precio,
    igvProducto as IGV
FROM productos;
UPDATE productos
SET
nombreProducto = 'Teclado',
valorProducto = '100.00',
igvProducto = '18.00'
WHERE idproductos = 1;
DELETE FROM productos
WHERE idproductos = 1


