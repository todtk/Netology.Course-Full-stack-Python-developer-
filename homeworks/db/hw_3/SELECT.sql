--название и год выхода альбомов, вышедших в 2018 году
SELECT title, age
FROM albums
WHERE age = 2018 ;

--название и продолжительность самого длительного трека
SELECT title, duration
FROM tracks
ORDER BY  duration DESC LIMIT 1 ;

--название треков, продолжительность которых не менее 3,5 минуты
SELECT title
FROM tracks
WHERE duration >= 210 ;

--названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT name
FROM compilations
WHERE year >= 2018 AND year <= 2020 ;

--исполнители, чье имя состоит из 1 слова
SELECT name
FROM performers
WHERE (LENGTH(name) - LENGTH(replace(name, ' ', ''))) = 0 ;

--название треков, которые содержат слово "мой"/"my"
SELECT title
FROM tracks
WHERE title LIKE '%My%' ;