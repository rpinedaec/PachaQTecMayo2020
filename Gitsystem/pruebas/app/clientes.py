import utils
class clientes:
  __log = utils.log("Empresa")
  def __init__(self,idCliente, nombreCliente, nroIdentidicacionCliente,direccionCliente):
    self.idCliente = idCliente
    self.nombreCliente = nombreCliente
    self.nroIdentidicacionCliente=nroIdentidicacionCliente
    self.direccionCliente=direccionCliente 