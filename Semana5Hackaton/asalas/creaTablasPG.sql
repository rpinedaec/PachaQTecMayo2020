CREATE TABLE public.alumno
(
    idalumno integer NOT NULL DEFAULT nextval('alumno_idalumno_seq'::regclass),
    "nombreAlumno" character varying(45) COLLATE pg_catalog."default" NOT NULL,
    "edadAlumno" integer NOT NULL,
    "correoAlumno" character varying(45) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT alumno_pkey PRIMARY KEY (idalumno)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.alumno
    OWNER to postgres;


/******************************************************************/

CREATE TABLE public.profesor
(
    idprofesor integer NOT NULL DEFAULT nextval('profesor_idprofesor_seq'::regclass),
    "nombreProfesor" character varying(45) COLLATE pg_catalog."default" NOT NULL,
    "edadProfesor" integer NOT NULL,
    "correoProfesor" character varying(45) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT profesor_pkey PRIMARY KEY (idprofesor)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.profesor
    OWNER to postgres;


/******************************************************************/


CREATE TABLE public.salon
(
    idsalon integer NOT NULL DEFAULT nextval('salon_idsalon_seq'::regclass),
    "nombreSalon" character varying(45) COLLATE pg_catalog."default" NOT NULL,
    idalumno integer NOT NULL,
    idprofesor integer NOT NULL,
    CONSTRAINT salon_pkey PRIMARY KEY (idsalon),
    CONSTRAINT fkidalumno FOREIGN KEY (idalumno)
        REFERENCES public.alumno (idalumno) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fkidprofesor FOREIGN KEY (idprofesor)
        REFERENCES public.profesor (idprofesor) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.salon
    OWNER to postgres;
/******************************************************************/

CREATE TABLE public.semestre
(
    idsemestre integer NOT NULL DEFAULT nextval('semestre_idsemestre_seq'::regclass),
    "descSemestre" character varying(45) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT semestre_pkey PRIMARY KEY (idsemestre)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.semestre
    OWNER to postgres;
/******************************************************************/

CREATE TABLE public.curso
(
    idcurso integer NOT NULL DEFAULT nextval('curso_idcurso_seq'::regclass),
    "nombreCurso" character varying(45) COLLATE pg_catalog."default" NOT NULL,
    idprofesor integer NOT NULL,
    idsemestre integer NOT NULL,
    CONSTRAINT curso_pkey PRIMARY KEY (idcurso),
    CONSTRAINT fkidprofesor FOREIGN KEY (idprofesor)
        REFERENCES public.profesor (idprofesor) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fkidsemestre FOREIGN KEY (idsemestre)
        REFERENCES public.semestre (idsemestre) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.curso
    OWNER to postgres;

/******************************************************************/
CREATE TABLE public.notas
(
    idnotas integer NOT NULL DEFAULT nextval('notas_idnotas_seq'::regclass),
    idalumno integer NOT NULL,
    idcurso integer NOT NULL,
    "descNota" character varying(45) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT notas_pkey PRIMARY KEY (idnotas),
    CONSTRAINT fkidalumno FOREIGN KEY (idalumno)
        REFERENCES public.alumno (idalumno) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fkidcurso FOREIGN KEY (idcurso)
        REFERENCES public.curso (idcurso) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.notas
    OWNER to postgres;