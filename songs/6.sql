SELECT name FROM songs WHERE Artist_id IN (SELECT artists.id from artists WHERE name = 'Post Malone');
