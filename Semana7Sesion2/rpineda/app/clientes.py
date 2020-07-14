class clientes:
    def __init__(self, idCliente , nombreCliente, nroIdentificacionCliente, direccionCliente):
        self.idCliente = idCliente
        self.nombreCliente = nombreCliente
        self.nroIdentificacionCliente = nroIdentificacionCliente
        self.direccionCliente = direccionCliente
    def toDic(self):
        d = {
            "idCliente": self.idCliente,
            "nombreCliente": self.nombreCliente,
            "nroIdentificacionCliente": self.nroIdentificacionCliente,
            "direccionCliente": self.direccionCliente
        }
        return d