INSERT INTO productos
(
nombreproducto,
valorproducto,
igvproducto)
VALUES
(
'Cuchillos',
50.22,
1);

SELECT idproducto,
    nombreproducto as Nombre,
    valorproducto as Valor,
    igvproducto as IGV
FROM productos;
SELECT idproducto,
    nombreproducto as Nombre,
    valorproducto as Valor,
    igvproducto as IGV
FROM productos where nombreproducto = 'Cuchillos';
UPDATE productos
SET
nombreproducto = 'Cuchillos',
valorproducto = 50.99,
igvproducto= 0
WHERE idproducto = 1;
DELETE FROM productos
WHERE idproducto = 1
