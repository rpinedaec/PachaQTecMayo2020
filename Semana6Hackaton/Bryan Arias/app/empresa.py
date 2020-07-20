import utils
class empresa:
    __log = utils.log("Empresa")
    def __init__(self,idempresa, rucEmpresa,nombreEmpresa):
        self.idempresa =idempresa
        self.rucEmpresa=rucEmpresa
        self.nombreEmpresa =nombreEmpresa