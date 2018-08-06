select * from dwhproj.pivot a inner join dwhproj.langpivot b
on a.Geoname=b.Geoname
where a.Geoname='Halifax';