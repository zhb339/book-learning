#include <stdlib.h>
#include <stdio.h>

#include "mysql.h"

MYSQL conn_ptr;
MYSQL_RES *res_ptr;
MYSQL_ROW sqlrow;

int main(int argc, char *argv[])
{
	int res;

	mysql_init(&conn_ptr);

	if (mysql_real_connect(&conn_ptr, "localhost", "rick", "338", "foo", 0, NULL, 0)) {
		printf("Connection success\n");
		res = mysql_query(&conn_ptr, "SELECT childno, fname, age FROM children WHERE age > 5");
		if (res) {
			printf("SELECT error: %s\n", mysql_error(&conn_ptr));			
		} else {
			res_ptr = mysql_store_result(&conn_ptr);
			if (res_ptr) {
				printf("Retrieved %lu rows\n", (unsigned long)mysql_num_rows(res_ptr));
				while (sqlrow = mysql_fetch_row(res_ptr)) {
					printf("Fetched data ...\n");
				}
				if (mysql_errno(&conn_ptr)) {
					printf("Retrieve error: %s\n", mysql_error(&conn_ptr));
				}
				mysql_free_result(res_ptr);
			}
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
