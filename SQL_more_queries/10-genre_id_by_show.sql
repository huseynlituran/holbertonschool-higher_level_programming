-- this query show us how use import
SELECT tv_shows.title, tv_show_genres_id
FROM tv_shows
JOIN tv_shows_genres ON tv_shows_id = tv_show_genres.show_id
ORDER BY tv_shows.title , tv_shows_genres.genre_id
;
