import streamlit as st
import pandas as pd
import numpy as np
import pickle

def get_clean_data():
    """
    Loads and cleans the breast cancer dataset.

    This function reads the dataset from a CSV file, drops unnecessary columns,
    and maps the diagnosis labels ('M' for malignant, 'B' for benign) to binary values (1 and 0).

    Returns:
        pandas.DataFrame: A cleaned DataFrame ready for analysis or modeling.
    """

    # Read the dataset
    data = pd.read_csv("data/data.csv")
    
    # Drop unnecessary columns
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    
    # Map diagnosis labels to numerical values
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
    
    return data


def add_predictions(input_data):
    """
    Loads a trained model and scaler, makes a prediction based on user input, and displays the result.

    The input is collected from the sidebar, scaled using a pre-fitted scaler,
    and passed to the trained model to predict whether the tumor is benign or malignant.
    The function also displays the prediction probabilities using styled HTML elements.

    Args:
        input_data (dict): A dictionary containing 30 numerical features entered by the user.

    Returns:
        None
    """

    # Load model and scaler
    model = pickle.load(open("model/model.pkl", "rb"))
    scaler = pickle.load(open("model/scaler.pkl", "rb"))
    
    # Convert input data to array and scale it
    input_array = np.array(list(input_data.values())).reshape(1, -1)
    input_array_scaled = scaler.transform(input_array)
    
    # Make a prediction
    prediction = model.predict(input_array_scaled)
    
    # Display the result
    st.subheader("Cell Cluster Prediction")
    st.write("The cell cluster is:")
    
    if prediction[0] == 0:
        st.write("<span class='diagnosis benign'>Benign</span>", unsafe_allow_html=True)
    else:
        st.write("<span class='diagnosis malicious'>Malicious</span>", unsafe_allow_html=True)
    
    # Get probabilities and convert to percentages
    benign_prob = model.predict_proba(input_array_scaled)[0][0] * 100  # Convert to percentage
    malignant_prob = model.predict_proba(input_array_scaled)[0][1] * 100  # Convert to percentage
    
    # Highlight probabilities
    benign_highlight = f"<span style='color: #4CAF50; font-size: 18px; font-weight: bold; background-color: #DFF7DC;'> {benign_prob:.2f}% </span>"
    malignant_highlight = f"<span style='color: #F44336; font-size: 18px; font-weight: bold; background-color: #F8D7DA;'> {malignant_prob:.2f}% </span>"
    
    st.markdown(f"**Probability of being benign:** {benign_highlight}", unsafe_allow_html=True)
    st.markdown(f"**Probability of being malignant:** {malignant_highlight}", unsafe_allow_html=True)
    
    # Warning Sign
    st.markdown("---")
    st.warning(
    "⚠️ This application is intended for educational purposes only and should not be used for real-life medical decisions. "
    "While the model has an accuracy of approximately **98.25%** , it is not a substitute for professional medical advice or diagnosis."
    )
    st.success(
        "🧑‍💻 Rudra Prasad Bhuyan  [Linkedin](https://www.linkedin.com/in/rudra-prasad-bhuyan-44a388235/)" 
    )