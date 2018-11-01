#include <stdlib.h>
#include <stdio.h>

#include "mysql.h"

int main(int argc, char *argv[])
{
	MYSQL conn_ptr;
	MYSQL_RES *res_ptr;
	MYSQL_ROW sqlrow;
	int res;

	mysql_init(&conn_ptr);

	if (mysql_real_connect(&conn_ptr, "localhost", "rick", "338", "foo", 0, NULL, 0)) {
		printf("Connection success\n");
		res = mysql_query(&conn_ptr, "INSERT INTO children(fname, age) VALUES ('ROBERT', 7)");
		if (!res) {
			printf("Updated %lu rows\n", (unsigned long)mysql_affected_rows(&conn_ptr));
		} else {
			fprintf(stderr, "Insert error %d: %s\n", mysql_errno(&conn_ptr), mysql_error(&conn_ptr));
		}

		res = mysql_query(&conn_ptr, "SELECT LAST_INSERT_ID()");
		if (res) {
			printf("SELECT error: %s\n", mysql_error(&conn_ptr));
		} else {
			res_ptr = mysql_use_result(&conn_ptr);
			if (res_ptr) {
				while (sqlrow = mysql_fetch_row(res_ptr)) {
					printf("We insertd childno %s\n", sqlrow[0]);
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
