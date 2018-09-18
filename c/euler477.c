#include <stdio.h>

unsigned long long max(unsigned long long n, unsigned long long m) 
{ return (n > m ? n : m); }
unsigned long long min(unsigned long long n, unsigned long long  m) 
{ return (n < m ? n : m); }

unsigned long long play_game(const int len){
	unsigned long long lookup[len];
	unsigned long long partial[len];
	unsigned long long seq[len];
	seq[0] = 0; // sequence base case
	
	// generate the sequence
	for(int i = 1; i < len; ++i){
		unsigned long long prev = seq[i-1];
		seq[i] = (prev*prev + 45) % 1000000007;
		lookup[i-1] = max(seq[i], seq[i-1]);
	}
	
	// fill intermediate results until we reach the end
	for(int i = 2 ; i <= len;  i += 2){

		for(int j = 0; j < (len - i - 1); ++j){
			partial[j] = max(min(lookup[j+1], lookup[j+2]) + seq[j], \
			                 min(lookup[j], lookup[j+1]) + seq[j+i+1]);
		}
		for(int k = 0; k < len; ++k){
			lookup[k] = partial[k];
		}
	}
	return partial[0];
}
	
unsigned long long euler477(){
	// these "magic numbers" were precomputed, start by searching the list
	// everytime a new element was added until a double was found, cycle_len
	// by computing the distance between the duplicate elements
	const int start = 64576;
	const int cycle_len = 7248;
	const int end = start + cycle_len;
	const unsigned long long repetitions = (100000000 - start) / cycle_len;
	
	// use cycles to our advantage to reduce work
	unsigned long long before_cycle_val = play_game(start);
	unsigned long long up_through_cycle_val = play_game(end);
	unsigned long long diff = up_through_cycle_val - before_cycle_val;
	return (repetitions * diff) + before_cycle_val;
}

int main(){
	unsigned long long result = euler477();
	printf("%llu\n", result);
}
