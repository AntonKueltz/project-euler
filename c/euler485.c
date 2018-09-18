#include <stdio.h>
#include <stdlib.h>

unsigned long * gen_div_count(unsigned long n){
	unsigned long * divs = (unsigned long *)malloc((n+1)*sizeof(unsigned long));

	for(unsigned long i = 0; i <= n; ++i) divs[i] = 1;

	for(unsigned long d = 2; d < n+1; ++d){
		unsigned long fac = d;
		while(fac <= n){
			divs[fac] += 1;
			fac += d;
		}
	}

	return divs;
}

unsigned long max(unsigned long * arr, unsigned long len, unsigned long * idx){
	unsigned long high = 0;
	for(int i = 0; i < len; ++i){
		if(arr[i] > high){ 
			high = arr[i];
			*idx = i;
		}
	}
	return high;
}


unsigned long long euler485(unsigned long u, unsigned long k){
	unsigned long * divs = gen_div_count(u);
	unsigned long start = 1;
	unsigned long end = start+k;
	unsigned long long sum = 0;
	unsigned long high = 0;
	unsigned long high_idx = 0;

	while(start <= u-k+1){
		unsigned long * window = &divs[start];

		if(high_idx < start){
			high = max(window, k, &high_idx);
			high_idx += start;
		}

		sum += high;

		unsigned long next_el = divs[end];
		if(next_el > high){
			high = next_el;
			high_idx = end;
		}

		++start;
		++end;
	}

	free(divs);
	return sum;
}

/* run using gcc flag -std=c99, pass 100000000 100000 as command line args */
int main(int argc, char * argv[]){
	unsigned long u = atol(argv[1]);
	unsigned long k = atol(argv[2]);
	printf("%llu\n", euler485(u, k));
}