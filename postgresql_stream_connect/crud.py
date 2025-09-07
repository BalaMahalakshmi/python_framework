 # streamlit_postgres_crud.py
import streamlit as st
import psycopg2

# --- Database Connection ---
def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="mahabi",
        user="postgres",
        password="08102004",
        port="5432"
    )

# --- Initialize Table (run once) ---
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            age INT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

init_db()

# --- Streamlit UI ---
st.title("Streamlit + PostgreSQL CRUD")

# CREATE
st.subheader("Add User")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120, step=1)

if st.button("Add User"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cur.close()
    conn.close()
    st.success(f"User {name} added!")

# READ
st.subheader(" Users in Database")
conn = get_connection()
cur = conn.cursor()
cur.execute("SELECT id, name, age FROM users ORDER BY id")
rows = cur.fetchall()
cur.close()
conn.close()

for r in rows:
    st.write(f"ID {r[0]} | 👤 {r[1]} - {r[2]} years old")

# UPDATE
st.subheader("Update User Age")
user_id = st.number_input("Enter user ID to update", min_value=1, step=1)
new_age = st.number_input("New Age", min_value=1, max_value=120, step=1)

if st.button("Update Age"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET age=%s WHERE id=%s", (new_age, user_id))
    conn.commit()
    cur.close()
    conn.close()
    st.success(f"User {user_id}'s age updated!")

# DELETE
st.subheader(" Delete User")
delete_id = st.number_input("Enter user ID to delete", min_value=1, step=1, key="delete")

if st.button("Delete User"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (delete_id,))
    conn.commit()
    cur.close()
    conn.close()
    st.success(f"User {delete_id} deleted!")
