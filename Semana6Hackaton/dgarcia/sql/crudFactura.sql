INSERT INTO faccabecera (idempresa, idtipoPago, idcliente, subtotalFacCabecera, igvFacCabecera, totalFacCabecera, estadoFactura)
VALUES ('2', '2', '2', '20', '0.18', '20.18', 'C');
SELECT idfacCabecera,
    idempresa  as idEmpresa,
    idtipoPago as idTipoPago,
    idcliente as idCliente,
    fechaFacCabecera as fecha,
    subtotalFacCabecera as Subtotal,
    0.18 * subtotalFacCabecera as IGV,
    totalFacCabecera=subtotalFacCabecera+igvFacCabecera as Total,
    estadoFactura as Estado,
    created_at as creado,
    updated_at as actualizado
FROM faccabecera;
UPDATE faccabecera
SET
subtotalFacCabecera = '35',
estadoFactura = 'P'
WHERE idempresa = 1 ;
DELETE FROM faccabecera
WHERE idfacCabecera = 1 ;