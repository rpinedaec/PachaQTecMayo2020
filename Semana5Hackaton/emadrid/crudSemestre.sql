-- Generated: 2020-06-28
-- Model: Colegio
-- Version: 1.0
-- Project: BD Colegio
-- Author: EMADRID

-- SELECT --
SELECT idsemestre, descsemestre, "lastUpdateSemestre"
	FROM emadrid.semestre;

-- INSERT --
INSERT INTO emadrid.semestre(
	descsemestre, "lastUpdateSemestre")
	VALUES ('2019-II', now());

-- UPDATE --
UPDATE emadrid.semestre
	SET idsemestre='2', descsemestre='2020-II', "lastUpdateSemestre"=now()
	WHERE idsemestre=3;

-- DELETE --
DELETE FROM emadrid.semestre
	WHERE idsemestre=2;