# 7. xxargs
def save_user(**user):
    print(user["id"], user["name"], user["profession"])


save_user(id = 1, name="Python", age =22, profession= "Programming language")
save_user(id = 2, name="Java", age =25, profession= "Programming language")

print("End of function 1 ")
print(" ")
print(" ")
# another calling
def user_data(**users):
    print(users["Id"], users["name"], users["department"],users["scope"])

user_data(Id=1, name="Hammad ibrahim ", department="DevOps,", scope="infrastructure")
user_data(Id=2, name="Mustafa Sabah", department="Php Developer,", scope="Full-Stack ")
user_data(Id=3, name="Alaa Elrayq ", department="Laravel Developer,", scope="Back End ")
user_data(Id=4, name="Ali Hussein ", department="Mobile app developer, ", scope="Mobile development ")
user_data(Id=5, name="Muhammed Ali ", department="Scrum master,", scope="Team Coaching ")