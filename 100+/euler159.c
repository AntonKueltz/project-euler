#include <stdio.h>
#include <stdlib.h>

int digital_root(int n){
    if(n == 0) return 0;
    else if(n % 9 == 0) return 9;
    else return n % 9;
}

int * mdrs(int n){
    int * drs = (int *)malloc(n * sizeof(int));
    for(int i = 0; i < n; ++i) drs[i] = 0;
	
    for(int i = 2; i < n; ++i){
        drs[i] = (drs[i] > digital_root(i)) ? drs[i] : digital_root(i);
			   
        for(int fac = 2; fac <= i; ++fac){
            int cur = i * fac;
            if(cur >= n) break;
            drs[cur] = (drs[cur] > drs[i]+drs[fac]) ? drs[cur] : drs[i]+drs[fac]; 
		}
	}

    return drs;
}

/*
 * for this problem the command line arg should be 1000000
 * compile with flag std=c99 in gcc
 */
int main(int argc, char * argv[]){
    long long sum = 0;
    int * drs = mdrs(atoi(argv[1]));
    for(int i = 2; i < atoi(argv[1]); ++i) sum += drs[i];
    printf("%lld\n", sum);
}
        
