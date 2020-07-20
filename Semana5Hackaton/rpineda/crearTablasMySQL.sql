-- MySQL Workbench Synchronization
-- Generated: 2020-06-27 12:05
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: rpineda

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `rpineda` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `rpineda`.`alumno` (
  `idalumno` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreAlumno` VARCHAR(45) NOT NULL,
  `edadAlumno` INT(11) NOT NULL,
  `correoAlumno` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idalumno`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `rpineda`.`profesor` (
  `idprofesor` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreProfesor` VARCHAR(45) NOT NULL,
  `edadProfesor` INT(11) NOT NULL,
  `correoProfesor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idprofesor`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `rpineda`.`curso` (
  `idcurso` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreCurso` VARCHAR(45) NOT NULL,
  `idprofesor` INT(11) NOT NULL,
  `idsemestre` INT(11) NOT NULL,
  PRIMARY KEY (`idcurso`),
  INDEX `fk_curso_profesor_idx` (`idprofesor` ASC) VISIBLE,
  INDEX `fk_curso_semestre1_idx` (`idsemestre` ASC) VISIBLE,
  CONSTRAINT `fk_curso_profesor`
    FOREIGN KEY (`idprofesor`)
    REFERENCES `rpineda`.`profesor` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_curso_semestre1`
    FOREIGN KEY (`idsemestre`)
    REFERENCES `rpineda`.`semestre` (`idsemestre`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `rpineda`.`salon` (
  `idsalon` INT(11) NOT NULL AUTO_INCREMENT,
  `nombreSalon` VARCHAR(45) NOT NULL,
  `idalumno` INT(11) NOT NULL,
  `idprofesor` INT(11) NOT NULL,
  PRIMARY KEY (`idsalon`),
  INDEX `fk_salon_alumno1_idx` (`idalumno` ASC) VISIBLE,
  INDEX `fk_salon_profesor1_idx` (`idprofesor` ASC) VISIBLE,
  CONSTRAINT `fk_salon_alumno1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `rpineda`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_salon_profesor1`
    FOREIGN KEY (`idprofesor`)
    REFERENCES `rpineda`.`profesor` (`idprofesor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `rpineda`.`notas` (
  `idnotas` INT(11) NOT NULL AUTO_INCREMENT,
  `idalumno` INT(11) NOT NULL,
  `idcurso` INT(11) NOT NULL,
  `descNota` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idnotas`),
  INDEX `fk_notas_alumno1_idx` (`idalumno` ASC) VISIBLE,
  INDEX `fk_notas_curso1_idx` (`idcurso` ASC) VISIBLE,
  CONSTRAINT `fk_notas_alumno1`
    FOREIGN KEY (`idalumno`)
    REFERENCES `rpineda`.`alumno` (`idalumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_notas_curso1`
    FOREIGN KEY (`idcurso`)
    REFERENCES `rpineda`.`curso` (`idcurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `rpineda`.`semestre` (
  `idsemestre` INT(11) NOT NULL AUTO_INCREMENT,
  `descSemestre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idsemestre`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
-- Table: public.alumno

-- DROP TABLE public.alumno;

CREATE TABLE public.alumno
(
    idalumno integer NOT NULL DEFAULT nextval('alumno_idalumno_seq'::regclass),
    nombrealumno character varying(45) COLLATE pg_catalog."default" NOT NULL,
    edadalumno integer NOT NULL,
    correoalumno character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT alumno_pkey PRIMARY KEY (idalumno)
)

TABLESPACE pg_default;

ALTER TABLE public.alumno
    OWNER to postgres;

-- Table: public.curso

-- DROP TABLE public.curso;

CREATE TABLE public.curso
(
    idcurso integer NOT NULL DEFAULT nextval('curso_idcurso_seq'::regclass),
    nombrecurso character varying(45) COLLATE pg_catalog."default" NOT NULL,
    idprofesor integer NOT NULL,
    idsemestre integer NOT NULL,
    CONSTRAINT curso_pkey PRIMARY KEY (idcurso),
    CONSTRAINT fk_curso_profesor FOREIGN KEY (idprofesor)
        REFERENCES public.profesor (idprofesor) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_curso_semestre1 FOREIGN KEY (idsemestre)
        REFERENCES public.semestre (idsemestre) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.curso
    OWNER to postgres;

-- Table: public.notas

-- DROP TABLE public.notas;

CREATE TABLE public.notas
(
    idnotas integer NOT NULL DEFAULT nextval('notas_idnotas_seq'::regclass),
    idalumno integer NOT NULL,
    idcurso integer NOT NULL,
    descnota character varying(45) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT notas_pkey PRIMARY KEY (idnotas),
    CONSTRAINT fk_notas_alumno1 FOREIGN KEY (idalumno)
        REFERENCES public.alumno (idalumno) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_notas_curso1 FOREIGN KEY (idcurso)
        REFERENCES public.curso (idcurso) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.notas
    OWNER to postgres;

-- Table: public.profesor

-- DROP TABLE public.profesor;

CREATE TABLE public.profesor
(
    idprofesor integer NOT NULL DEFAULT nextval('profesor_idprofesor_seq'::regclass),
    nombreprofesor character varying(45) COLLATE pg_catalog."default" NOT NULL,
    edadprofesor integer NOT NULL,
    correoprofesor character varying(45) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT profesor_pkey PRIMARY KEY (idprofesor)
)

TABLESPACE pg_default;

ALTER TABLE public.profesor
    OWNER to postgres;

-- Table: public.salon

-- DROP TABLE public.salon;

CREATE TABLE public.salon
(
    idsalon integer NOT NULL DEFAULT nextval('salon_idsalon_seq'::regclass),
    nombresalon character varying(45) COLLATE pg_catalog."default" NOT NULL,
    idalumno integer NOT NULL,
    idprofesor integer NOT NULL,
    CONSTRAINT salon_pkey PRIMARY KEY (idsalon),
    CONSTRAINT fk_salon_alumno1 FOREIGN KEY (idalumno)
        REFERENCES public.alumno (idalumno) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_salon_profesor1 FOREIGN KEY (idprofesor)
        REFERENCES public.profesor (idprofesor) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.salon
    OWNER to postgres;

-- Table: public.semestre

-- DROP TABLE public.semestre;

CREATE TABLE public.semestre
(
    idsemestre integer NOT NULL DEFAULT nextval('semestre_idsemestre_seq'::regclass),
    descsemestre character varying(45) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT semestre_pkey PRIMARY KEY (idsemestre)
)

TABLESPACE pg_default;

ALTER TABLE public.semestre
    OWNER to postgres;

    