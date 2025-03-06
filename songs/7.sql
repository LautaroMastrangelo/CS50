SELECT AVG(energy) FROM songs WHERE artist_id IN (SELECT artists.id FROM artists WHERE name = 'Drake');
