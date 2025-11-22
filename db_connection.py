import psycopg2

def connection():
    try:
        #External database host from cloud to cloud 
        """ conn = psycopg2.connect(user="test_2ax2_user",
                                password="CdYjtWXw0dW9gmwjA2YYslv4sSBlB5qD",
                                host="dpg-d4ethoc9c44c73cjdni0-a",
                                port="5432",
                                database="test_2ax2") """
        # Internal database connection from local to local
        conn = psycopg2.connect(user="postgres",
                                    password="postgres",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="testdb2")
        
        return conn 
          
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into mobile table", error)
        return None


            
