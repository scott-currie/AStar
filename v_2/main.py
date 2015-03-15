from gamemap import Map

rows = 15
columns = 15

gmap = Map(rows, columns)

start = gmap.get_random_free_cell()
print('start',start)
gmap.put_in_cell(start, '1')

end = gmap.get_random_free_cell()
print('end',end)
gmap.put_in_cell(end, '2')

gmap.print_map()