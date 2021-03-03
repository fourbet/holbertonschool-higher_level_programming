-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.name AS "genre", COUNT(sg.genre_id) AS "number_of_shows" 
FROM tv_genres g 
JOIN tv_show_genres sg 
ON sg.genre_id = g.id 
GROUP BY genre 
ORDER BY number_of_shows DESC;
