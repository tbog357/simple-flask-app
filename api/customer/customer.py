from api.main.core.database import PostgresClient


class Customer:
    # Contain operations for a single user
    # Each user is unique by email
    def __init__(self, **customer_data) -> None:
        self.db_client = PostgresClient(dbname="appdb")
        # Assume no validation on email
        self.email = customer_data.get("email")
        self.fields = [
            "email",
            "phone",
            "address",
            "name",
            "status",
        ]
        self.request_data = customer_data
        self.db_data = None
        self.is_exist_in_db = None
        self.is_deleted = None

    def __is_customer_exist(self):
        query = f"SELECT email, phone, address, name, status FROM customer WHERE customer.email={self.email}"
        result = self.db_client.get_query_result(query)
        if result is None:
            return None
        elif len(result) == 1:
            self.db_data = dict(zip(self.fields, result))
            return True
        elif len(result) == 0:
            return False
        else:
            return None

    def __insert_customer(self):
        query = f"INSERT INTO customer (email) VALUES ({self.email}) RETURNING *;"
        result = self.db_client.get_query_result(query)
        return result

    def __update_customer(self, fields: list):
        query = f"UPDATE customer SET "

    # Main
    def create(self):
        # Create new customer by email
        is_exist = self.__is_customer_exist()
        if is_exist is False:
            return self.__insert_customer()
        elif is_exist is True:
            return {
                "success": False,
                "error_message": "Customer had already existed in database",
            }

    def read(self):
        # Get customer information
        is_exist = self.__is_customer_exist()
        if is_exist is True:
            return {
                "success": True,
                "customer": self.db_data,
            }
        elif is_exist is False:
            return {
                "success": False,
                "error_message": "Customer did not existed in database",
            }

    def update(self):
        # Update customer information
        # phone, address, name
        is_exist = self.__is_customer_exist()
        if is_exist is True:
            self.__update_customer(fields=["phone", "address", "name"])
        elif is_exist is False:
            return {
                "success": False,
                "error_message": "Customer did not existed in database",
            }

    def delete(self):
        # Delete customer
        is_exist = self.__is_customer_exist()
        if is_exist is True:
            self.request_data.update("status", "deleted")
            self.__update_customer(fields=["status"])
        elif is_exist is False:
            return {
                "success": False,
                "error_message": "Customer did not existed in database",
            }
