-- Iterativly insert the matchnumber for one season
-- GER has a limit of 9!
WITH cte AS (
   (SELECT *
   FROM   matches    
   WHERE season = '18-19'
 	    AND country = 'ENG'
 	    AND matchnumber IS NULL
 	ORDER BY startdate ASC
   LIMIT  10)
   UNION
   ( SELECT *
   FROM   matches    
   WHERE season = '18-19'
 	    AND country = 'ESP'
 	    AND matchnumber IS NULL
 	ORDER BY startdate ASC
   LIMIT  10)
   UNION
   (SELECT *
   FROM   matches    
   WHERE season = '18-19'
 	    AND country = 'FRA'
 	    AND matchnumber IS NULL
 	ORDER BY startdate ASC
   LIMIT  10)
   UNION
   (SELECT *
   FROM   matches    
   WHERE season = '18-19'
 	    AND country = 'ITA'
 	    AND matchnumber IS NULL
 	ORDER BY startdate ASC
   LIMIT  10)
   )
UPDATE matches a
SET    matchnumber = 1
FROM cte
WHERE cte.season = a.season
		AND cte.country = a.country
		AND cte.hometeamname = a.hometeamname
		AND cte.awayteamname = a.awayteamname


