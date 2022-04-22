-- For every season, check if a teamname occurs twice for a matchnumber 
-- spottet errors occur twice
SELECT a.country, a.season, a.matchnumber, a.hometeamname, a.awayteamname, a.hometeamgoals, a.awayteamgoals, '-'AS space , b.country, b.season, b.matchnumber, b.hometeamname, b.awayteamname, b.hometeamgoals, b.awayteamgoals
  FROM matches a
  INNER JOIN (SELECT * FROM matches) b ON (a.hometeamname = b.hometeamname AND a.season = b.season AND a.matchnumber = b.matchnumber AND a.awayteamname != b.awayteamname)  
		OR (a.awayteamname = b.awayteamname AND a.season = b.season AND a.matchnumber = b.matchnumber AND a.hometeamname != b.hometeamname)
		OR (a.hometeamname = b.awayteamname AND a.season = b.season AND a.matchnumber = b.matchnumber AND a.awayteamname != b.hometeamname)
		OR (a.awayteamname = b.hometeamname AND a.season = b.season AND a.matchnumber = b.matchnumber AND a.hometeamname != b.awayteamname)
WHERE a.season = '14-15'
 ORDER BY a.country, a.season, a.matchnumber
 
 
 