-- Table: public.apoderado

-- DROP TABLE public.apoderado;

CREATE TABLE public.apoderado
(
    idapoderado integer NOT NULL DEFAULT nextval('apoderado_idapoderado_seq'::regclass),
    nom_apoderado character varying(45) COLLATE pg_catalog."default" NOT NULL,
    correo_apoderado character varying(45) COLLATE pg_catalog."default" NOT NULL,
    telefono_apoderado integer,
    CONSTRAINT apoderado_pkey PRIMARY KEY (idapoderado)
)

TABLESPACE pg_default;

ALTER TABLE public.apoderado
    OWNER to postgres;


-- Table: public.alumno

-- DROP TABLE public.alumno;

CREATE TABLE public.alumno
(
    idalumno integer NOT NULL DEFAULT nextval('alumno_idalumno_seq'::regclass),
    nom_alumno character varying(45) COLLATE pg_catalog."default" NOT NULL,
    cod_alumno integer NOT NULL,
    edad_alumno integer NOT NULL,
    correo_alumno character varying COLLATE pg_catalog."default" NOT NULL,
    direccion_alumno character varying(100) COLLATE pg_catalog."default",
    apoderado_idapoderado integer,
    CONSTRAINT alumno_pkey PRIMARY KEY (idalumno),
    CONSTRAINT fk_alumno_apoderado1 FOREIGN KEY (apoderado_idapoderado)
        REFERENCES public.apoderado (idapoderado) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE public.alumno
    OWNER to postgres;


-- Table: public.profesor

-- DROP TABLE public.profesor;

CREATE TABLE public.profesor
(
    idprofesor integer NOT NULL DEFAULT nextval('profesor_idprofesor_seq'::regclass),
    nom_profesor character varying(45) COLLATE pg_catalog."default" NOT NULL,
    cod_profesor integer NOT NULL,
    edad_profesor integer NOT NULL,
    correo_profesor character varying COLLATE pg_catalog."default" NOT NULL,
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
    nom_salon character varying(45) COLLATE pg_catalog."default" NOT NULL,
    profesor_idprofesor integer NOT NULL,
    alumno_idalumno integer NOT NULL,
    CONSTRAINT salon_pkey PRIMARY KEY (idsalon),
    CONSTRAINT fk_salon_alumno1 FOREIGN KEY (alumno_idalumno)
        REFERENCES public.alumno (idalumno) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_salon_profesor FOREIGN KEY (profesor_idprofesor)
        REFERENCES public.profesor (idprofesor) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.salon
    OWNER to postgres;


-- Table: public.curso

-- DROP TABLE public.curso;

CREATE TABLE public.curso
(
    idcurso integer NOT NULL DEFAULT nextval('curso_idcurso_seq'::regclass),
    nom_curso character varying(45) COLLATE pg_catalog."default" NOT NULL,
    profesor_idprofesor integer NOT NULL,
    bimestre_idbimestre integer NOT NULL,
    CONSTRAINT curso_pkey PRIMARY KEY (idcurso),
    CONSTRAINT fk_curso_bimestre1 FOREIGN KEY (bimestre_idbimestre)
        REFERENCES public.bimestre (idbimestre) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_curso_profesor1 FOREIGN KEY (profesor_idprofesor)
        REFERENCES public.profesor (idprofesor) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.curso
    OWNER to postgres;


-- Table: public.nota

-- DROP TABLE public.nota;

CREATE TABLE public.nota
(
    idnota integer NOT NULL DEFAULT nextval('nota_idnota_seq'::regclass),
    desc_nota character varying(45) COLLATE pg_catalog."default" NOT NULL,
    alumno_idalumno integer NOT NULL,
    curso_idcurso integer NOT NULL,
    CONSTRAINT nota_pkey PRIMARY KEY (idnota),
    CONSTRAINT fk_nota_alumno1 FOREIGN KEY (alumno_idalumno)
        REFERENCES public.alumno (idalumno) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_nota_curso1 FOREIGN KEY (curso_idcurso)
        REFERENCES public.curso (idcurso) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE public.nota
    OWNER to postgres;


-- Table: public.bimestre

-- DROP TABLE public.bimestre;

CREATE TABLE public.bimestre
(
    idbimestre integer NOT NULL DEFAULT nextval('bimestre_idbimestre_seq'::regclass),
    desc_bimestre character varying(45) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT bimestre_pkey PRIMARY KEY (idbimestre)
)

TABLESPACE pg_default;

ALTER TABLE public.bimestre
    OWNER to postgres;