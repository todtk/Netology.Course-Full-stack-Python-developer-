CREATE TABLE IF NOT EXISTS genres (
	id SERIAL PRIMARY KEY,
	title VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS performers (
	id SERIAL PRIMARY KEY,
	name VARCHAR(80) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS genres_performers (
	genre_id INTEGER REFERENCES genres(id),
	performer_id INTEGER REFERENCES performers(id),
	CONSTRAINT GP_pk PRIMARY KEY (genre_id, performer_id)
);

CREATE TABLE IF NOT EXISTS albums (
	id SERIAL PRIMARY KEY,
	title VARCHAR(80) UNIQUE NOT NULL,
	age INTEGER NOT null
	CHECK (age<=2022)
);

CREATE TABLE IF NOT EXISTS performers_albums (
	album_id INTEGER REFERENCES albums(id),
	performer_id INTEGER REFERENCES performers(id),
	CONSTRAINT AP_pk PRIMARY KEY (album_id, performer_id)
);

CREATE TABLE IF NOT EXISTS tracks (
	id SERIAL PRIMARY KEY,
	title VARCHAR(120) UNIQUE NOT NULL,
	duration INTEGER NOT NULL,
	album_id INTEGER REFERENCES albums(id)
);

CREATE TABLE IF NOT EXISTS compilations (
	id SERIAL PRIMARY KEY,
	name VARCHAR(80) UNIQUE NOT NULL,
	year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS compilations_tracks (
	compilations_id INTEGER REFERENCES compilations(id),
	tracks_id INTEGER REFERENCES tracks(id),
	CONSTRAINT CT_pk PRIMARY KEY (compilations_id, tracks_id)
);