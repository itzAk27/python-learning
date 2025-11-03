from loguru import logger 


class labors:
    def __init__(self, first_name, last_name, wage, role, crud):
        self.first_name = first_name
        self.last_name = last_name 
        self.wage = wage 
        self.role = role
        self.crud = crud
        self.__save_to_database(crud)

 
    def __save_to_database(self, curd):
        query = """ SELECT * FROM labors WHERE lower(first_name) = %s and lower(last_name) = %s """
        ret = curd.read_from_mysql(query, (self.first_name, self.last_name))

        if ret:
            logger.info("Labor Already Exists")
            logger.info(f"RESULT: {ret}")
            return
        
        logger.info(f"Labor Not Exists")

        insert_query = """  INSERT INTO labors(first_name, last_name, wage, role, email)
                            VALUES (%s, %s, %s, %s, %s)
                        """
        email = self.first_name + self.last_name + "@gmail.com"
        ret = curd.insert_into_mysql(insert_query, (self.first_name, self.last_name, self.wage, self.role, email))
        print(f"ret: {ret}")
        if ret:
            logger.info("Labor Added")
            return

        
