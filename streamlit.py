import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

with open('RandomForest.pkl', 'rb') as f:
    model = pickle.load(f)
    
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
accuracy = 0.9861

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

col1, col2, col3 = st.columns(3)

with col1:
    def main():
        St.title("Virus Detector")
        uploaded_file = st.file_uploader("Choose a file")

        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)

            # Convert the DataFrame to CSV
            csv_data = df.to_csv(index=False)
    
            # Display the converted CSV data
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name="converted_file.csv",
                mime='text/csv'
            )
    
            with open('RandomForest.pkl', 'rb') as f:
                model = pickle.load(f)
    
            # Make predictions
            predictions = model.predict(df)
    
            # Display the predictions
            st.write("Predictions:")
            st.write(predictions)
    
            if __name__ == '__main__':
                main()

with col2:
    fig, ax = plt.subplots(figsize=(5, 5))  # Adjust figure size
    labels = ['Non-Infected', 'Infected']
    fig.patch.set_facecolor('black')
    labels = ['Non-Infected', 'Infected']
    colors = ['#85586F', '#B7D3DF']
    font = {'family': 'serif',
                'color':  'white',
                 'size': 7}
        
    sizes = [df['legitimate'].value_counts()[0], df['legitimate'].value_counts()[1]]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, textprops=font)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)

with col3: 
    print("   ")
