-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT DISTINCT s.title AS "title" 
FROM tv_shows s 
JOIN tv_show_genres sg 
ON sg.show_id = s.id 
JOIN tv_genres g 
ON sg.genre_id = g.id 
WHERE g.name = "Comedy" 
ORDER BY title;
