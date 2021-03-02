--  lists all shows contained in the database hbtn_0d_tvshows
SELECT DISTINCT s.title, g.genre_id 
FROM tv_shows s 
LEFT JOIN tv_show_genres g 
ON g.show_id = s.id 
WHERE g.show_id IS NULL
ORDER BY s.title ,g.genre_id;
