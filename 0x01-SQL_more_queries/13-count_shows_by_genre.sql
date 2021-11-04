-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: tv_genres.name - number of shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT a.name AS genre, COUNT(b.genre_id) AS number_of_shows
FROM tv_genres a
JOIN tv_show_genres b
ON a.id = b.genre_id
GROUP BY b.genre_id
ORDER BY number_of_shows DESC;
