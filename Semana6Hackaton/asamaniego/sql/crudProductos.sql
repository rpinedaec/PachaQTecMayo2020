INSERT INTO productos
(
nombreProducto,
valorProducto,
igvProducto)
VALUES
(
'Cuchillos',
50.22,
1);

SELECT idproducto,
    nombreProducto as Nombre,
    valorProducto as Valor,
    igvProducto as IGV
FROM productos;
SELECT idproducto,
    nombreProducto as Nombre,
    valorProducto as Valor,
    igvProducto as IGV
FROM productos where nombreProducto = 'Cuchillos';
UPDATE productos
SET
nombreProducto = 'Cuchillos',
valorProducto = 50.99,
igvProducto= 0
WHERE idproducto = 1;
DELETE FROM productos
WHERE idproducto = 1


