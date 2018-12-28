#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt

R = 24
C = 2

if len(sys.argv) > 1: C = int(sys.argv[1])
if len(sys.argv) > 2: R = int(sys.argv[2])

N_max = C * R

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]
	
known_primes = primes(N_max)
max_primes = len(known_primes)
if C < 5: print known_primes

n_numbers = np.zeros(N_max)
r_numbers = np.zeros(N_max)
th_numbers = np.zeros(N_max)

n_primes = np.zeros(max_primes)
r_primes = np.zeros(max_primes)
th_primes = np.zeros(max_primes)

n = 0
p = 0
for c in range(C):
    for i in range(R):
        n_numbers[n] = n+1
        r_numbers[n]  = c+1
        th_numbers[n] = ( 2.*np.pi/float(R) ) * (i+1)
        
        if (p < max_primes) and (n_numbers[n] == known_primes[p]):
            n_primes[p]  = n_numbers[n]
            r_primes[p]  = r_numbers[n]
            th_primes[p] = th_numbers[n]
            p += 1
        else:
            pass

        n += 1
        
fig = plt.figure( figsize=(10., 10.) )
ax = fig.add_subplot(111, projection="polar")

points_size = 100
font_size = 12
if C > 10:
    points_size = 50  
    font_size = 6
if C > 30:
    points_size = 10  
    font_size = 0

for x, y, n in zip(th_numbers, r_numbers, n_numbers):
    ax.scatter( (x,), (y,), color="gray", s=points_size )
    if C < 30:
        plt.text(x,y,'%i' % n, fontsize=font_size )

for x, y, n in zip(th_primes, r_primes, n_primes):
    ax.scatter( (x,), (y,), color="red", s=points_size )
    if C < 30:
        plt.text(x,y,'%i' % n, fontsize=font_size )

ax.set_rticks([])
dth = 360 / R
ax.set_thetagrids( [-dth, dth, 90-dth, 90+dth, 180-dth, 180+dth, 270-dth, 270+dth], labels=['']*C )
if C > 1: ax.set_rgrids( np.arange(1,C), labels=['']*C ) 
ax.grid(True)

ext = "jpg"
plt.savefig("%s/primes_r%i_c%i.%s" % (ext, R,C, ext) )

plt.show()
