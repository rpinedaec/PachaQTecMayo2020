INSERT INTO producto
(
nombreProducto,
precioProducto,
igvProducto)
VALUES
(
'Cuchillos',
50.22,
1);

SELECT idproducto,
    nombreProducto as Nombre,
    precioProducto as Precio,
    igvProducto as IGV,
    created_at as creado,
    updated_at as actualizado
FROM producto;
SELECT idproducto,
    nombreProducto as Nombre,
    precioProducto as Precio,
    igvProducto as IGV,
    created_at as creado,
    updated_at as actualizado
FROM producto where nombreProducto = 'Cuchillos';
UPDATE producto
SET
nombreProducto = 'Cuchillos',
precioProducto = 50.99,
igvProducto= 0
WHERE idproducto = 1;
DELETE FROM productos
WHERE idproducto = 1
