#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

#define ONE_K  1024

int main()
{
	char *some_memory;
	size_t size_to_allocate = ONE_K;
	int megs_obtained = 0;
	int ks_obtained = 0;

	while (1) {
		for (ks_obtained = 0; ks_obtained < 1024; ks_obtained++) {
			some_memory = (char *)malloc(size_to_allocate);
			if (some_memory != NULL) {				
				sprintf(some_memory, "Hello");							
			} else {
				exit(EXIT_FAILURE);
			}			
		}
		megs_obtained++;
		printf("now allocated %d Megabytes\n", megs_obtained);
	}
	exit(EXIT_SUCCESS);
}
