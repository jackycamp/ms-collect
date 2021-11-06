import csv
from functools import reduce

from ms_collect.collection import Collection
from ms_collect.envelope import Envelope
from ms_collect.point import Point
from ms_collect.scope import Scope

MS_POINT_TESTING_FILE = './ms_points.csv'

#### TODO:
## Rest assured: Automated unit testing coming soon!!

pts = []
with open(MS_POINT_TESTING_FILE) as csvfile:
	reader = csv.reader(csvfile)
	for index, row in enumerate(reader):
		print("Index: ", index)
		print("Row: ", row)
		if index == 0: continue

		new_pt = Point(mz=row[0], rt=row[1], intensity=row[2])
		pts.append(new_pt)

# for pt in pts:
# 	print(pt.as_string())


# col = Collection(points=pts)
# col = Collection()

# print("avg something?: ", reduce(lambda a, b: a.rt + b.rt, pts))
# print("Avg m/z: ", col.avg_mz())
# print("Avg RT: ", col.avg_rt())
# print("Avg intensity: ", col.avg_intensity())
# print("Cum intensity: ", col.cumulative_intensity())
# mz_sum = 0.0
# for pt in pts:
# 	mz_sum += pt.mz

# print("MZ SUM: ", mz_sum)
# cvx_hull = col.convex_hull()
# hull = cvx_hull.hull()
# print("Hull: ", hull)

min_mz = 437.844
max_mz = 438.94
min_rt = 946.004
max_rt = 981.107

scp = Scope([min_mz, max_mz, min_rt, max_rt])
my_envelope = Envelope(scope=scp)

pts_to_add = []
for pt in pts:
	if my_envelope.point_belongs(pt):
		pts_to_add.append(pt)

my_envelope.add_points(pts_to_add)
print("Number of envelope points: ", len(my_envelope.points))
print("Cumulative intensity: ", my_envelope.cumulative_intensity())

ch = my_envelope.convex_hull()
print("Convex hull: ", ch.hull())

