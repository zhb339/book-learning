#include <stdlib.h>
#include <stdio.h>

#include "mysql.h"

int main(int argc, char *argv[])
{
	MYSQL conn_ptr;

	mysql_init(&conn_ptr);

	if (mysql_real_connect(&conn_ptr, "localhost", "rick", "339", "foo", 0, NULL, 0)) {
		printf("Connection success\n");
		mysql_close(&conn_ptr);
	} else {
		printf("Connection failed\n");
		if (mysql_errno(&conn_ptr)) {
			fprintf(stderr, "Connection error %d: %s\n", mysql_errno(&conn_ptr), mysql_error(&conn_ptr));
		}
	}

	

	return EXIT_SUCCESS;
}
