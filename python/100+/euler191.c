#include <stdio.h>

unsigned long long prizes = 0;

void genPrizeStr(unsigned consec_absent, unsigned late_days, unsigned days){
	if(days == 30) prizes += 1;
	else{
		if(consec_absent != 2)
			genPrizeStr(consec_absent+1, late_days, days+1);
		if(late_days != 1)
			genPrizeStr(0, late_days+1, days+1);

		genPrizeStr(0, late_days, days+1);
	}
}

int main(int argc, char * argv[]){
	genPrizeStr(0, 0, 0);
	printf("%llu\n", prizes);
}