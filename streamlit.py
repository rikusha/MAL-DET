import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame (replace with your actual data)
malData = pd.read_csv("MalwareData.csv",sep = "|" )
legit = malData[malData["legitimate"] == 1]
mal = malData[malData["legitimate"] == 0]

df = pd.DataFrame(malData)

# Calculate accuracy (replace with your actual accuracy)
accuracy = 99.45

# Create the dashboard
st.title("Malware Detection Dashboard")

# Display model accuracy
st.header("Model Accuracy")
st.progress(accuracy)

# Display infected files
st.header("Infected Files")
st.dataframe(df[df['label'] == 1])

# Display non-infected files
st.header("Non-Infected Files")
st.dataframe(df[df['label'] == 0])

# Create a pie chart
fig, ax = plt.subplots()
labels = ['Non-Infected', 'Infected']
sizes = [df['label'].value_counts()[0], df['label'].value_counts()[1]]
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)
