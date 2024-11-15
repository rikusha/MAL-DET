import streamlit as st
import requests
import matplotlib.pyplot as plt
import zipfile
import pandas as pd

github_url = "https://github.com/rikusha/MAL-DET/archive/refs/heads/main.zip"

def download_and_extract_data(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open("temp.zip", "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile("temp.zip", 'r') as zip_ref:
            try:
                zip_ref.extract(filename)
                return True
            except KeyError:
                st.error(f"File '{filename}' not found in the ZIP archive.")
                return False
    else:
        st.error(f"Failed to download data. Error code: {response.status_code}")
        return False

if download_and_extract_data(github_url, "MalwareData.csv"):
    malData = pd.read_csv('MalwareData.csv', sep='|')
    # ... rest of your code using malData ...
else:
    st.error("Data extraction failed. Please check the ZIP file and try again.")

# Read the CSV file
malData = pd.read_csv('MalwareData.csv', sep='|')

# Split data into legitimate and malware DataFrames
legitimate = malData[malData['label'] == 0].drop(["legitimate"], axis=1)
malware = malData[malData['label'] == 1].drop(["legitimate"], axis=1)

# Calculate accuracy (replace with your actual accuracy)
accuracy = 99.45

# Create the dashboard
st.title("Malware Detection Dashboard")

# Display model accuracy
st.header("Model Accuracy")
st.progress(accuracy)

# Display infected files
st.header("Infected Files")
st.dataframe(malware)

# Display non-infected files
st.header("Non-Infected Files")
st.dataframe(legitimate)

# Create a pie chart
fig, ax = plt.subplots()
labels = ['Non-Infected', 'Infected']
sizes = [malData['label'].value_counts()[0], malData['label'].value_counts()[1]]
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)
