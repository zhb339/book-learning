#include <unistd.h>
#include <stdlib.h>

int main()
{
	if ((write(1, "here is some data\n", 19)) != 18)
		write(1, "here is error\n", 18);

	exit(0);
}
