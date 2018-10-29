#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

#define ONE_K 1024

int main()
{
	char *some_memory;

	some_memory = (char *)malloc(ONE_K);
	if (some_memory != NULL) {
		free(some_memory);
		printf("Memory allocated and freed again \n");
		exit(EXIT_SUCCESS);
	}
	
	exit(EXIT_FAILURE);
}
