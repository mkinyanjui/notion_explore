import streamlit as st
import pandas as pd

# streamlit_app.py

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM pTest;', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name}  lives in :{row.city}:")
