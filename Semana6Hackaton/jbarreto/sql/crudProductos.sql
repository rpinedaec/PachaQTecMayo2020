INSERT INTO productos
(
nombreProducto,
valorProducto,
igvProducto)
VALUES
(
'mesas',
30.50,
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
FROM productos where nombreProducto = 'tvs';
UPDATE productos
SET
nombreProducto = 'tvs',
valorProducto = 50.99,
igvProducto= 0
WHERE idproducto = 1;
DELETE FROM productos
WHERE idproducto = 1
