INSERT INTO productos
(
nombreProducto,
valorProducto,
igvProducto)
VALUES
(
'Lapiz',
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
FROM productos where nombreProducto = 'Cuadernos';
UPDATE productos
SET
nombreProducto = 'Cuadernos',
valorProducto = 50.99,
igvProducto= 0
WHERE idproducto = 1;
DELETE FROM productos
WHERE idproducto = 1


