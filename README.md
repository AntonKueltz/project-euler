# Project Euler
### About
[Project Euler](http://projecteuler.net/) is an excellent website that requires programming to solve mathematical problems, usually on extremely large input sets, and in under 1 minute running time. This means solution algorithms need to be very efficient, and often require some mathematical insights to reduce their time complexity. Solutions are written mostly in Python, sometimes C when I really need the performance. The Haskell solutions are purely for fun and approaching the problems with a different programming paradigm. Solutions run on a 2014 MacBook Air (i5).

### Dependencies
[numpy](http://www.numpy.org) ```pip install numpy```
<br/>
[scipy](http://www.scipy.org) ```pip install scipy```

### Usage
##### Python
```
python euler[#].py
``` 
[#] is the problem number. If you'd like to time the runtime there is a decorator in euler_util.py called "timed". Simply put ```@timed``` on the line before ```def euler[x]():``` to time the problem. For some of the higher problems Python really struggles to run in under 1 minute, even with an (imo) optimal appraoch to the problem. In these (rare) instances I'd recommend using [pypy](http://pypy.org) rather than the standard python interpreter.
##### C++
```
./build [#]
./run
```
[#] is the problem number, in this case 0 padded to 3 digits (e.g. to build problem 1 the number is 001).

### Miscellaneous
I can't keep anyone from cheating and just using these to submit answers, however you won't learn anything that way and are just cheating yourself out of learning how to solve these problems. Rather, I'd hope people who see this code see an approach a bit different from their solution, or a way of expressing their solution in a different programming language. Final Note -  I don't solve many of these anymore mainly because the remaining problems require significant time for me to solve, time that I don't often have.
