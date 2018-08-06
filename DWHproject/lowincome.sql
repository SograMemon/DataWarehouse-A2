select Geoname, lowincome4
from proj.pivot
group by Geoname, lowincome4
order by Geoname;