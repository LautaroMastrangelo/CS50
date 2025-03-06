SELECT title FROM movies WHERE movies.id IN
    (SELECT stars.movie_id FROM stars WHERE stars.person_id IN
        (SELECT people.id FROM people WHERE (people.name = 'Bradley Cooper')))
AND movies.id IN(SELECT stars.movie_id FROM stars WHERE stars.person_id IN
(SELECT people.id FROM people WHERE (people.name = 'Jennifer Lawrence')));


