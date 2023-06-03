--количество исполнителей в каждом жанре
SELECT 
	title AS "Жанр",
	COUNT(gp.performer_id) AS "Кол-во исполнителей" 
FROM genres AS g
JOIN genres_performers AS gp
	ON g.id = gp.genre_id
JOIN performers AS p
	ON gp.performer_id = p.id
GROUP BY g.title ;

--количество треков, вошедших в альбомы 2019-2020 годов
SELECT COUNT(album_id) AS "Кол-во"
FROM tracks AS t
JOIN albums AS a
	ON t.album_id = a.id
WHERE a.age
	BETWEEN 2019
		AND 2020 ;

--средняя продолжительность треков по каждому альбому
SELECT 
	a.title AS "Альбом",
	AVG(t.duration) AS "Ср.прод-сть"
FROM albums AS a
JOIN tracks AS t
	ON a.id = t.album_id
GROUP BY  a.title, t.album_id ;

--все исполнители, которые не выпустили альбомы в 2020 году
SELECT name AS "Без альбома в 2020"
FROM performers AS p
WHERE p.name NOT IN 
	(SELECT name
	FROM performers AS p
	JOIN performers_albums AS pa
		ON p.id = pa.performer_id
	JOIN albums AS a
		ON pa.album_id = a.id
	WHERE a.age = 2020) ;

--названия сборников, в которых присутствует конкретный исполнитель
SELECT DISTINCT c.name AS "Название сборника"
FROM compilations AS c
JOIN compilations_tracks AS ct
	ON c.id = ct.compilations_id
JOIN tracks AS t
	ON ct.tracks_id = t.id
JOIN albums AS a
	ON t.album_id = a.id
JOIN performers_albums AS pa
	ON a.id = pa.album_id
JOIN performers AS p
	ON pa.performer_id = p.id
WHERE p.name = 'Nothing But Thieves' ;

--название альбомов, в которых присутствуют исполнители более 1 жанра
SELECT title AS "Название альбома"
FROM albums AS a
JOIN performers_albums AS pa
	ON a.id = pa.album_id
JOIN performers AS p
	ON pa.performer_id = p.id
JOIN genres_performers AS gp
	ON p.id = gp.performer_id
GROUP BY  title
HAVING COUNT(*) > 1 ;

--наименование треков, которые не входят в сборники
SELECT 
	title AS "Название трека"
FROM tracks AS t
LEFT JOIN compilations_tracks AS ct
	ON t.id = ct.tracks_id
WHERE ct.compilations_id IS NULL ;

--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)
SELECT name AS "Исполнитель"
FROM performers AS p
JOIN performers_albums AS pa
	ON p.id = pa.performer_id
JOIN albums AS a
	ON pa.album_id = a.id
JOIN tracks AS t
	ON a.id = t.album_id
WHERE t.duration = 
	(SELECT MIN(duration)
	FROM tracks) ;
	
--название альбомов, содержащих наименьшее количество треков
SELECT t.title AS "Название альбома"
FROM albums AS a
JOIN tracks AS t
	ON t.album_id = a.id
WHERE t.album_id IN 
	(SELECT t2.album_id
	FROM tracks AS t2
	GROUP BY  t2.album_id
	HAVING COUNT(t2.album_id) = 
		(SELECT COUNT(t3.album_id)
		FROM tracks t3
		GROUP BY  t3.album_id
		ORDER BY  count LIMIT 1)) ;