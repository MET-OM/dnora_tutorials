clear
close all
filename='Ex1_Sula500_SWAN/Ex1_Sula500_20200120.nc';
lon=ncread(filename, 'longitude');
lat=ncread(filename,'latitude');
time=datetime(ncread(filename,'time'), 'convertfrom','posixtime');
hs=ncread(filename,'hs');
n=20;
h=pcolor(lon, lat, hs(:,:,n)');
set(h, 'EdgeColor', 'none');
xlabel('longitude')
ylabel('latitude')
a = colorbar;
a.Label.String = 'Hs (m)';
title(char(time(n)));