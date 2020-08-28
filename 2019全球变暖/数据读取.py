from netCDF4 import Dataset

group = Dataset('./data/sst.nc', 'w')
print(group)