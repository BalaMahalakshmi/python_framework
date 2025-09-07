import streamlit as st
from pymongo import MongoClient

# Replace with your connection string
client = MongoClient("mongodb://localhost:27017")
db = client["baladb"]   # Database
collection = db["list"]    # Collection (like a table)

st.title("Streamlit + MongoDB CRUD App")

# CREATE
st.subheader("Add a User")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120)
if st.button("Add User"):
    collection.insert_one({"name": name, "age": age})
    st.success(f"User {name} added!")

# READ
st.subheader("Users in Database")
users = list(collection.find())
if users:
    for user in users:
        # st.write(user)
        st.write(f"👤 {user['name']} - {user['age']} years old")


# UPDATE
st.subheader("Update User Age")
user_to_update = st.text_input("Enter name to update")
new_age = st.number_input("New Age", min_value=1, max_value=120, key="update_age")
if st.button("Update Age"):
    result = collection.update_one({"name": user_to_update}, {"$set": {"age": new_age}})
    if result.modified_count:
        st.success("Age updated successfully!")
    else:
        st.warning("User not found.")

# DELETE
st.subheader("Delete User")
user_to_delete = st.text_input("Enter name to delete")
if st.button("Delete User"):
    result = collection.delete_one({"name": user_to_delete})
    if result.deleted_count:
        st.success("User deleted successfully!")
    else:
        st.warning("User not found.")