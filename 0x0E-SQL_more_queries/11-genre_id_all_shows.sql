-- lists all shows contained in hbtn_0d_tvshows and their genre id.
-- Uses SELECT with JOIN statement to lists them.
SELECT title, genre_id
FROM tv_shows LEFT OUTER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
ORDER BY title ASC, genre_id ASC;
