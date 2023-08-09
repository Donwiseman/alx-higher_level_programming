-- lists all genres of the show Dexter.
-- Uses INNER JOIN with SELECT clause to produce output.
SELECT name
FROM tv_genres INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
WHERE show_id = (
	SELECT id
	FROM tv_shows
	WHERE title = 'Dexter'
);
