select Geoname,ii851_65_years_and_over
from dwhproj.pivot
group by Geoname,ii851_65_years_and_over DESC;