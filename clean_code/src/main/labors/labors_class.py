from loguru import logger 
from datetime import datetime


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name + '.' + self.last_name + '@gmail.com'


    def print_details(self):
        return f"FIRST NAME: {self.first_name}, LAST NAME: {self.last_name} & EMAIL: {self.email}"
    

class labors(Person):
    def __init__(self, first_name, last_name, wage, role, crud, config):
        super().__init__(first_name, last_name)
        self.wage = wage 
        self.role = role
        self.crud = crud
        self.id = self.__save_to_database(crud)
        self.config = config
 
    def __save_to_database(self, curd):
        query = """ SELECT * FROM labors WHERE lower(first_name) = %s and lower(last_name) = %s """
        ret = curd.read_from_mysql(query, (self.first_name, self.last_name))

        if ret:
            logger.info("Labor Already Exists")
            logger.info(f"RESULT: {ret}")
            return ret[0][0]
        
        logger.info(f"Labor Not Exists")

        insert_query = """  INSERT INTO labors(first_name, last_name, wage, role, email)
                            VALUES (%s, %s, %s, %s, %s)
                        """
        
        ret = curd.insert_into_mysql(insert_query, (self.first_name, self.last_name, self.wage, self.role, self.email))
        print(f"ret: {ret}")
        if ret:
            logger.info("Labor Added")
            return ret[0][0]


    @staticmethod
    def login_logout(config, curd, id=None, first_name=None, last_name=None):
        if id is None:
            if first_name is None or last_name is None:
                logger.error("Particular Labor Not Found...!!!")
                return
            
            query = f"""
                SELECT id 
                FROM {config["db_tables"]["labor_tbl"]}
                where lower(first_name) = %s
                and   lower(last_name) = %s
            """
            logger.info(f"Query: {query}")

            try:
                ret = curd.read_from_mysql(query, (first_name, last_name))
                logger.info(f"Found ID: {ret[0][0]}")
                id = ret[0][0]
            except IndexError as e:
                logger.info(f"{e}")
            except Exception as e:
                logger.info("ID Not Found...")
        

        # Check ID Exists in Attendance table 
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_time = datetime.now()

        check_query = f"""
                SELECT * FROM attendance 
                WHERE labour_id = %s
                AND cast(start_time as date) = %s
            """
        
        result = curd.read_from_mysql(check_query, (id, current_date))
        logger.info(f"DATA FROM ATTENDANCE TABLE: {result}")

        if not result:
           insert_labour_query = """
                                    INSERT INTO attendance(labour_id, start_time)
                                    values (%s, %s)
                                """
           insert_ret = curd.insert_into_mysql(insert_labour_query, (id, current_time))
           logger.info(f"labour {id}, logged at {current_time}")
        else:
            id = result[0][0]
            update_labour_query = """
                            UPDATE attendance
                            SET end_time = now()
                            WHERE id = %s
                       """
            update_ret = curd.insert_into_mysql(update_labour_query, (id,))
            logger.info(f"UPDATED LABOUR {id} WITH {current_time} TIME")


class Mistry(labors):
    def __init__(self, first_name, last_name, wage, role, skill, crud, config):
        super().__init__(first_name, last_name, wage, role, crud, config)
        self.skill = skill
        self.__save_to_skill_table()
    
    def __save_to_skill_table(self):
        insert_query = """
                        INSERT INTO skills(labour_id, skill)
                        VALUES (%s, %s)
                """
        insert_ret = self.crud.insert_into_mysql(insert_query, (self.id, self.skill))
        print(f"INSERT RESULT SKILLS : {insert_ret}")