import mysql.connector

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)
print("---==Welcome to the Duck's Dictionary==---")
word = input("Enter a word to search: ").lower()
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary where Expression  = '%s'" %word)
results = cursor.fetchall()
i=0
if results:
    print(word,":")
    for result in results:
        i = i+1    
        print(i,".",result[1] , "\n ------------")
else : 
    print("No word found!")        