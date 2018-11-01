#include <stdlib.h>
#include <stdio.h>

#include "mysql.h"

int main(int argc, char *argv[])
{
	MYSQL *conn_ptr;

	conn_ptr = mysql_init(NULL);
	if (!conn_ptr) {
		fprintf(stderr, "mysql_init_failed\n");
		return EXIT_FAILURE;
	}

	conn_ptr = mysql_real_connect(conn_ptr, "localhost", "rick", "338", "foo", 0, NULL, 0);

	if (conn_ptr) {
		printf("Connection success\n");
	} else {
		printf("Connection failed\n");
	}

	mysql_close(conn_ptr);

	return EXIT_SUCCESS;
}
