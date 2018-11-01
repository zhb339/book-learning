#include <stdlib.h>
#include <stdio.h>

#include "mysql.h"

MYSQL conn_ptr;
MYSQL_RES *res_ptr;
MYSQL_ROW sqlrow;

void display_row()
{
	unsigned int field_count;
	
	field_count = 0;
	while (field_count < mysql_field_count(&conn_ptr)) {
		printf("%s \n", sqlrow[field_count]);
		field_count++;
	}
	printf("\n");
}

void display_header()
{
	MYSQL_FIELD *field_ptr;

	printf("Column details:\n");
	while ((field_ptr = mysql_fetch_field(res_ptr)) != NULL) {
		printf("\t Name: %s\n", field_ptr->name);
		printf("\t Type: ");
		if (IS_NUM(field_ptr->type)) {
			printf("Numberic field\n");
		} else {
			switch (field_ptr->type) {
				case FIELD_TYPE_VAR_STRING:
					printf("VARCHAR\n");
					break;
				case FIELD_TYPE_LONG:
					printf("LONG\n");
					break;
				default:
					printf("Type is %d, check in mysql_com.h\n", field_ptr->type);
			}
		}
		
		printf("\t Max width %ld\n", field_ptr->length);
		if (field_ptr->flags & AUTO_INCREMENT_FLAG)
			printf("\t Auto increment\n");
		printf("\n");
	}
}

int main(int argc, char *argv[])
{
	int res;
	int first_row = 1;

	mysql_init(&conn_ptr);

	if (mysql_real_connect(&conn_ptr, "localhost", "rick", "338", "foo", 0, NULL, 0)) {
		printf("Connection success\n");
		res = mysql_query(&conn_ptr, "SELECT childno, fname, age FROM children WHERE age > 5");
		if (res) {
			printf("SELECT error: %s\n", mysql_error(&conn_ptr));			
		} else {
			res_ptr = mysql_use_result(&conn_ptr);
			if (res_ptr) {
				while (sqlrow = mysql_fetch_row(res_ptr)) {
					if (first_row) {
						display_header();
						first_row = 0;
					}
					display_row();
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
