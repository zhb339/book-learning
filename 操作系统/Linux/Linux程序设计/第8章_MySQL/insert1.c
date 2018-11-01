#include <stdlib.h>
#include <stdio.h>

#include "mysql.h"

int main(int argc, char *argv[])
{
	MYSQL conn_ptr;
	int res;

	mysql_init(&conn_ptr);

	if (mysql_real_connect(&conn_ptr, "localhost", "rick", "338", "foo", 0, NULL, 0)) {
		printf("Connection success\n");
		res = mysql_query(&conn_ptr, "UPDATE children set AGE = 4 WHERE fname='Ann'");
		if (!res) {
			printf("Updated %lu rows\n", (unsigned long)mysql_affected_rows(&conn_ptr));
		} else {
			fprintf(stderr, "Insert error %d: %s\n", mysql_errno(&conn_ptr), mysql_error(&conn_ptr));
		}
		mysql_close(&conn_ptr);
	} else {
		printf("Connection failed\n");
		if (mysql_errno(&conn_ptr)) {
			fprintf(stderr, "Connection error %d: %s\n", mysql_errno(&conn_ptr), mysql_error(&conn_ptr));
		}
	}

	

	return EXIT_SUCCESS;
}
