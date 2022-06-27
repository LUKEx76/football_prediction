

SELECT m.country, m.season, m.matchnumber, m.hometeamname, m.awayteamname, 
	sh.avgchancedifference AS hometeamcurrchancediff, sa.avgchancedifference AS awayteamcurrchancediff,
	sh1.avgchancedifference AS hometeamchancediff1, sa1.avgchancedifference AS awayteamchancediff1,
	sh2.avgchancedifference AS hometeamchancediff2, sa2.avgchancedifference AS awayteamchancediff2,
	sh3.avgchancedifference AS hometeamchancediff3, sa3.avgchancedifference AS awayteamchancediff3,
	h.valueinmio AS hometeamvalue, a.valueinmio AS awayteamvalue
  FROM matches m
  
  JOIN teams h ON m.hometeamname = h.teamname AND m.season = h.season
  JOIN teams a ON m.awayteamname = a.teamname AND m.season = a.season
  
  JOIN standings sh ON m.season = sh.season AND m.matchnumber = sh.matchnumber AND m.hometeamname = sh.teamname
  JOIN standings sa ON m.season = sa.season AND m.matchnumber = sa.matchnumber AND m.awayteamname = sa.teamname
  
  LEFT JOIN (SELECT * FROM standings WHERE matchnumber = 34 AND season = '17-18') sh1 ON m.hometeamname = sh1.teamname
  LEFT JOIN (SELECT * FROM standings WHERE matchnumber = 34 AND season = '16-17') sh2 ON m.hometeamname = sh2.teamname
  LEFT JOIN (SELECT * FROM standings WHERE matchnumber = 34 AND season = '15-16') sh3 ON m.hometeamname = sh3.teamname
  
  LEFT JOIN (SELECT * FROM standings WHERE matchnumber = 34 AND season = '17-18') sa1 ON m.awayteamname = sa1.teamname
  LEFT JOIN (SELECT * FROM standings WHERE matchnumber = 34 AND season = '16-17') sa2 ON m.awayteamname = sa2.teamname
  LEFT JOIN (SELECT * FROM standings WHERE matchnumber = 34 AND season = '15-16') sa3 ON m.awayteamname = sa3.teamname
  
  WHERE m.season = '18-19' AND m.country = 'GER'
  
 ORDER BY m.season ASC, m.matchnumber ASC, m.country ASC


