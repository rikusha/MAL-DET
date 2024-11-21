import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(layout="wide")

# Sample DataFrame (replace with your actual data)
malData = pd.read_csv("MalwareData.csv",sep = "," )
legit = malData[malData["legitimate"] == 1]
mal = malData[malData["legitimate"] == 0]

df = pd.DataFrame(malData)

#to check incase error in reading data
print(malData.head())

# Calculate accuracy (replace with your actual accuracy)
accuracy = 0.99

# Create the dashboard
st.title("Malware Detection Dashboard")

# Display model accuracy
st.header("Model Accuracy")
st.progress(accuracy)

# Create two columns
col1, col2 = st.columns(2)

# Display infected files in the first column
with col1:
    st.header("Infected Files")
    st.dataframe(df[df['legitimate'] == 1])

# Display non-infected files in the second column
with col2:
    st.header("Non-Infected Files")
    st.dataframe(df[df['legitimate'] == 0])

col1, col2 = st.columns([2,1])

with col1:
    plt.figure(figsize=(1, 1), dpi=300)  #figure size and dpi
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    labels = ['Non-Infected', 'Infected']
    colors = ['#85586F', '#B7D3DF']
    font = {'family': 'serif',
            'color':  'white',
             'size': 3}
    
    sizes = [df['legitimate'].value_counts()[0], df['legitimate'].value_counts()[1]]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, textprops=font)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

with col2: 
    print("    ")
