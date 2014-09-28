#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
    
void solve(int i, int depth, int * mults, int * path, int n){
    if (i > n || depth > mults[i]) 
		return;
            
	mults[i] = depth;
    path[depth] = i;
            
	for (int j = depth; j >= 0; --j)
        solve(i + path[j], depth+1, mults, path, n);
}
	
int * m(int n){
	int * mults = (int *)malloc((n+1) * sizeof(int));
    int * path = (int *)malloc((n+1) * sizeof(int));
          
    for(int i = 0; i <= n; ++i) 
		mults[i] = INT_MAX;

    solve(1, 0, mults, path, n);
	return mults;
}

/*
 * command line arg is 200
 * use gcc flag std=c99
 */
int main(int argc, char * argv[]){
	int n = atoi(argv[1]);
	int * ms = m(n);
	int sum = 0;
	for(int i = 2; i <= n; ++i) sum += ms[i];
	printf("%d\n", sum);
}