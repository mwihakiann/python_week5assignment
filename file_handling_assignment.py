#create a new text file named my_file.txt in write ('W')mode
with open('my_file.txt', 'w') as file:
    
    #write some content to the file
    file.write("Name: Mary Ann, Age: 25, Score: 85.\n")
    file.write("Name: Jane, Age: 20, Score: 75.\n")
    file.write("Name: George, Age: 23, Score: 78.\n")           
                   
#Read from the file and display its contents
with open('my_file.txt', 'r') as file:
    
    #Read all lines from the contents
    content = file.read()
    #Display the contents on the console
    print("File Contents:\n")
    print(content)  
    
#Append to the file
with open('my_file.txt', 'a') as file:
    
    #Append three additional lines of text to the existing content
    file.write("Name: Elias, Age: 26, Score:86.\n")
    file.write("Name: Abel, Age: 21, Score:79.\n")
    file.write("Name: Cally, Age: 24, Score: 72.\n")
    
#Read from the updated file
with open('my_file.txt', 'r') as file:
    content = file.read()
    print("Updated File Contents\n")
    print(content) 
    
 # Attempt to create and write to the file
try:
    with open('my_file.txt', 'w') as file:
        file.write("Name: Mary Ann, Age: 25, Score: 85.\n")
        file.write("Name: Jane, Age: 20, Score: 75.\n")
        file.write("Name: George, Age: 23, Score: 78.\n")
    print("File created and initial content added.")
except Exception as e:
    print(f"Something went wrong while writing to the file: {e}")
finally:
    print("Finished writing operation.\n")

# Attempt to read the file content
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("Here are the current contents of the file:")
        print(content)
except Exception as e:
    print(f"Error occurred during reading: {e}")
finally:
    print("File read operation completed.\n")

# Attempt to append new data to the file
try:
    with open('my_file.txt', 'a') as file:
        file.write("Name: Elias, Age: 26, Score:86.\n")
        file.write("Name: Abel, Age: 21, Score:79.\n")
        file.write("Name: Cally, Age: 24, Score: 72.\n")
    print("New data has been added to the file.")
except Exception as e:
    print(f"Could not append to the file: {e}")
finally:
    print("Finished appending data.\n")

# Attempt to read the updated file content
try:
    with open('my_file.txt', 'r') as file:
        updated_content = file.read()
        print("Updated file contents:")
        print(updated_content)
except Exception as e:
    print(f"Error occurred while reading the updated file: {e}")
finally:
    print("Finished reading the updated file.\n")
                          