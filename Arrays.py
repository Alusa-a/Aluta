courses = ["MIT", "Cyber Security", "Data Science"]
print(courses)
print(courses)

#Accessing an element
print(courses[2])

#Looping through an array
for x in courses:
    print("Course is",x)



#Adding a new element into an array
courses.append("Laravel")
print(courses)

#Removing an element from an array
courses.remove("Cyber Security")
print(courses)


