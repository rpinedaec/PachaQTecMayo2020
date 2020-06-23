import logging
import os.path
from os import remove


class log:
    def __init__(self, nombreLogger):
        # create logger
        self.logger = logging.getLogger(nombreLogger)
        self.logger.filename = 'app.log'
        self.logger.setLevel(logging.DEBUG)
        # create console handler and set level to debug
        ch = logging.FileHandler("app.log", mode='a')
        ch.setLevel(logging.DEBUG)
        # create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # add formatter to ch
        ch.setFormatter(formatter)
        # add ch to logger
        self.logger.addHandler(ch)

    def debug(self, mensaje):
        self.logger.debug(mensaje)

    def info(self, mensaje):
        self.logger.info(mensaje)

    def warning(self, mensaje):
        self.logger.warning(mensaje)

    def error(self, mensaje):
        self.logger.error(mensaje)

    def critical(self, mensaje):
        self.logger.critical(mensaje)



class fileManager:
    logD = log("FileManager")
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
    
    def leerArchivo(self):
        try:
            file = open(self.nombreArchivo,'r')
            return file.read()    
        except Exception as e:
            return e
    
    def escribirArchivo(self, linea):
        try:
            path = os.getcwd()
            self.logD.debug(path)

            if(os.path.isfile(path+"\\"+self.nombreArchivo)):
                # Grabar
                try:
                    #Escribir en el archivo
                    file = open(self.nombreArchivo,'a')
                    file.write(linea+"\n")
                except Exception as e:
                    self.logD.debug(e)
                    print(e)
                finally:
                    file.close()
            else:
                file = open(self.nombreArchivo,'w') 
                file.close()
                file = open(self.nombreArchivo,'a')
                file.write(linea+"\n")
                
        except Exception as e:
            self.logD.debug(e)
            return e

    def borrarArchivo(self):
        path = os.getcwd()
        nombre = self.nombreArchivo
        if path.exists(path+"\\"+nombre):
            try:
                remove(path+"\\"+nombre)
            except Exception as error:
                self.logD.error(error)

