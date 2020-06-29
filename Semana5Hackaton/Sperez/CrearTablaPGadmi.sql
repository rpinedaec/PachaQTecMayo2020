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
    descnotas character varying(45) COLLATE pg_catalog."default" NOT NULL,
    idalumno integer NOT NULL,
    idcurso integer NOT NULL,
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