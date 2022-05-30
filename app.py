import streamlit as st
import snowflake.connector

# Initialize connection
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(**st.secrets["snowflake"])

conn = init_connection()

# Perform query
# Uses st.experimental_memo to only rerun when the query changes or after 10 sec.
# @st.experimental_memo(ttl=10)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

if st.button('Refresh'):
    rows = run_query("SELECT * from mytable;")

with st.form("inserter"):
    st.write("`INSERT INTO MYTABLE VALUES ('{name}', '{animal}')`")
    name = st.text_input('Name')
    animal = st.text_input('Animal')
    if st.form_submit_button('Insert'):
        run_query(f"INSERT INTO MYTABLE VALUES ('{name}', '{animal}');")

with st.form("deleter"):
    st.write("`DELETE FROM MYTABLE WHERE name = '{name}'`")
    name = st.text_input('Name')
    if st.form_submit_button('Delete'):
        run_query(f"DELETE FROM MYTABLE WHERE name = '{name}';")