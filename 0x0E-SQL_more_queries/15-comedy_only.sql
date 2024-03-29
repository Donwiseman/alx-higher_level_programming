-- lists all Comedy shows in the database hbtn_0d_tvshows.
-- Uses INNER JOIN with SELECT clause to produce output.
SELECT title
FROM tv_shows INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
WHERE name = 'Comedy'
ORDER BY title ASC;
