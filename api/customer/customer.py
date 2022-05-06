from tkinter.messagebox import NO
from api.main.core.database import PostgresClient

# local import
from api.model.model_customer import ModelCustomer


class Customer:
    # Contain operations for a single user
    # Each customer is unique by email
    def __init__(self, model_customer: ModelCustomer) -> None:
        if model_customer.email is None:
            raise ValueError("email must not be None")

        # Store request customer data
        self.request_customer_data = model_customer

        # Store db customer data
        self.db_client = PostgresClient(dbname="appdb")
        self.db_filter_fields = [
            "email",
            "phone",
            "address",
            "name",
            "status",
        ]
        self.db_customer_data = None
        self.is_customer_exist = self.__is_customer_exist()

        # Check if the customer already deleted
        self.is_customer_deleted = False
        if self.db_customer_data is not None:
            self.is_customer_deleted = self.db_customer_data.get("status") == "deleted"

    def __is_customer_exist(self):
        # Build and run query
        email = self.request_customer_data.email
        query = f"SELECT email, phone, address, name, status FROM customer WHERE customer.email='{email}'"
        result = self.db_client.get_query_result(query)

        # Check result
        if result is None:
            return None
        elif len(result) == 1:
            self.db_customer_data = dict(zip(self.db_filter_fields, result[0]))
            return True
        elif len(result) == 0:
            return False
        else:
            return None

    def __insert_customer(self):
        # Build query and run
        columns, values = [], []
        for key, value in self.request_customer_data.to_dict().items():
            columns.append(key)
            values.append("'" + value + "'")
        columns_sql = ", ".join(columns)
        values_sql = ", ".join(values)
        query = f"INSERT INTO customer ({columns_sql}) VALUES ({values_sql}) RETURNING {columns_sql};"
        result = self.db_client.get_query_result(query)
        result = dict(zip(columns, result[0]))
        return result

    def __update_customer(self, fields: list):
        key_value = []
        for key, value in self.request_customer_data.to_dict().items():
            if key in fields:
                key_value.append(f"{key} = '{value}'")
        key_value = ", ".join(key_value)

        email = self.request_customer_data.email
        columns_sql = ", ".join(self.db_filter_fields)
        query = f"UPDATE customer SET {key_value} WHERE email='{email}' RETURNING {columns_sql};"
        result = self.db_client.get_query_result(query)
        result = dict(zip(self.db_filter_fields, result[0]))
        result.pop("status", None)
        return result

    # Main
    def create(self):
        if self.is_customer_exist is False and not self.is_cutomer_deleted:
            # Create new customer by email
            self.request_customer_data.status = "active"
            self.db_customer_data = self.__insert_customer()
            if self.db_customer_data is not None:
                return {
                    "success": True,
                    "customer_data": self.db_customer_data,
                }
            else:
                return {
                    "success": False,
                }
        elif self.is_customer_exist is True and self.is_customer_deleted:
            # Re-ctive deleted customer
            self.request_customer_data.status = "active"
            result = self.__update_customer(fields=["status"])
            return {"success": True, "customer_data": result}
        elif self.is_customer_exist is True:
            # Customer existed
            return {
                "success": False,
                "error_message": "Customer had already existed in database",
            }

    def read(self):
        # Get customer information
        if self.is_customer_exist and not self.is_customer_deleted:
            self.db_customer_data.pop("status", None)
            return {
                "success": True,
                "customer": self.db_customer_data,
            }
        elif self.is_customer_exist is False:
            return {
                "success": False,
                "error_message": "Customer did not existed in database or deleted",
            }

    def update(self):
        # Update customer information
        # phone, address, name
        if self.is_customer_exist is True:
            result = self.__update_customer(fields=["phone", "address", "name"])
            return {
                "success": True,
                "new_data": self.request_customer_data.to_dict(),
                "old_data": result,
            }
        elif self.is_customer_exist is False:
            return {
                "success": False,
                "error_message": "Customer did not existed in database",
            }

    def delete(self):
        # Delete customer
        if self.is_customer_exist and not self.is_customer_deleted:
            self.request_customer_data.status = "deleted"
            self.__update_customer(fields=["status"])
            return {
                "success": True,
            }
        elif self.is_customer_exist is False:
            return {
                "success": False,
                "error_message": "Customer did not existed in database",
            }
