import streamlit as st
import pandas as pd

def generate_output(PT, WT, PPT):
    return pd.DataFrame([(a, b, c) for a in PT for b in WT for c in PPT], columns=["PT", "WT", "PPT"])

st.title("Streamlit Web App")

# Input sets
PT = st.text_input("Enter Precursor Temperature values (comma-separated):", "45,50,60")
WT = st.text_input("Enter Wafer Temperature values (comma-separated):", "30,50,75")
PPT = st.text_input("Enter Precursor Pulse Time values (comma-separated):", "0.5,1.0,2.0")

# Convert input strings to lists
PT = [float(val.strip()) for val in PT.split(',')]
WT = [float(val.strip()) for val in WT.split(',')]
PPT = [float(val.strip()) for val in PPT.split(',')]

# Generate output
output_df = generate_output(PT, WT, PPT)

# Display formatted output
st.write("Generated Output List:")
st.dataframe(output_df)
