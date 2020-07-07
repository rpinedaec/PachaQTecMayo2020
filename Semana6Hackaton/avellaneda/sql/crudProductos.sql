-- CRUD
-- productos

#AÑADIR ELEMENTO
INSERT INTO productos (nombreProducto, valorProducto, igvProducto) VALUES ('cuchara', '10.50', 1);

#BUSCAR ELEMENTO
SELECT idproductos, nombreProducto AS Nombre, valorProducto AS Valor, igvProducto AS IGV FROM productos;

#BUSCAR ELEMENTO POR VARIABLE QUE SE PIDA, EN ESTE CASO ES EL NOMBRE
SELECT idproductos, nombreProducto AS Nombre, valorProducto AS Valor, igvProducto AS IGV FROM productos WHERE nombreProducto = 'cuchara';

#MODIFICAR O ACTUALIZAR ELEMENTO BUSCADO POR ID O POR LO QUE SE PIDA, ACÁ ES CON ID
UPDATE productos SET nombreProducto = 'tenedor', valorProducto = '15.56', igvProducto = 1 WHERE idproductos = 1;

#ELIMINAR ELEMENTO POR ID.
DELETE FROM productos WHERE idproductos = 2;