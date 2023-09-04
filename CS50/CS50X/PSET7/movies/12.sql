SELECT title
FROM movies, people, stars
WHERE people.id = stars.person_id AND stars.movie_id = movies.id AND people.name = 'Bradley Cooper'
INTERSECT
SELECT title
FROM movies, people, stars
WHERE people.id = stars.person_id AND stars.movie_id = movies.id AND people.name = 'Jennifer Lawrence';