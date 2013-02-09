from __future__ import division
from random import randrange

from ffnet import ffnet, mlgraph, readdata, savenet

# Generate standard layered network architecture and create network
conec = mlgraph((2, 50, 1))
net = ffnet(conec)

N = 10
limit = 100
hr_data = range(0, 2000) #[randrange(60,100) for x in range(100)]
pa_data = range(0, 4000, 2) #[randrange(60,100) for x in range(100)]
pa_data = []
start = 0
for x in range(2000):
  start += x
  pa_data.append(start)

hr_input = [sum(hr_data[x:x+N])/N for x in range(0, limit-N, N)]
hr_target = [sum(hr_data[x:x+N])/N for x in range(N, limit, N)]

pa_diffs = [abs(pa_data[x]-pa_data[x+1]) for x in range(limit-N)]
pa_input = [sum(pa_diffs[x:x+N])/N for x in range(0, limit-N, N)]


input = map(list, zip(hr_input, pa_input))
target = [[n] for n in hr_target]
print input[:10]
print target[:10]


net.train_tnc(input, target)


#output, regression = net.test(input, hr_target, iprint=3)
output, regression = net.test(input, target, iprint=2)
print
#print output
#print regression


savenet(net, 'hrnet.net')

