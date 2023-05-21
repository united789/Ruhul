import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="banks_portal",
                 user='root',
                 password='wuwu16qexo'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)


    def getAllAccounts(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor()
            query = "select * from accounts"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            return records

    def getAllTransactions(self):
        ''' Complete the method to execute
                query to get all transactions'''
        pass
       
    def deposit(self, accountId, amount):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor()
            print("Connection Successful")
            self.cursor.callproc('deposit', (accountId, amount))
        pass
   

    def withdraw(self, accountId, amount):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor()
            print("Connection Successful")
            self.cursor.callproc('withdraw', (accountId, amount))
        pass
        
    def addAccount(self, ownerName, owner_ssn, balance, status):
        print("Function Start")
        if self.connection.is_connected():
            print("Connection Established")
            self.cursor= self.connection.cursor()
            query = f"INSERT INTO accounts (ownerName, owner_ssn, balance, account_status) VALUES (\'{ownerName}\', {owner_ssn}, {balance}, \'{status}\')"
            print(query)
            print("Before Query Execution")
            self.cursor.execute(query)
            print("After Query Execution")
            self.connection.commit() 
            print("After Commit")
            print("Account added successfully!")
        else:
            print('Function Bypassed')
        
  
    def accountTransactions(self, accountID):
        ''' Complete the method to call
                    procedure accountTransaction return results'''
        pass
  
    def deleteAccount(self, AccountID):
        ''' Complete the method to delete account
                and all transactions related to account'''
        pass
        
        
        
    
    
