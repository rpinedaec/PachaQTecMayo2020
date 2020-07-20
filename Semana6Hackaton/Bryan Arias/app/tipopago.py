import utils
class tipopago:
    __log = utils.log("Tipo de Pago")
    def __init__(self, idtipopago, desctipopago):
        self.idtipopago = idtipopago
        self.desctipopago = desctipopago