# Import libraries
import streamlit as st
from utils.sidebar import add_sidebar
from utils.charts import get_radar_chart
from utils.data_model import add_predictions

def main():
  st.set_page_config(
    page_title="🎗️ Breast Cancer Predictor",
    layout="wide",
    initial_sidebar_state="auto"
  )
  
  st.logo("assets/rudra.png")
  
  # Show balloons only once per session
  if "balloons_shown" not in st.session_state:
        st.balloons()
        st.session_state.balloons_shown = True


  # Allow the streamlit to access the css files
  with open("assets/style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

  input_data = add_sidebar()
  
  with st.container():
    st.title("🎗️ Breast Cancer Predictor")
    st.write(
        "Connect this app to your cytology lab for fast and reliable breast cancer predictions. "
        "It analyzes tissue sample measurements to determine whether a breast mass is benign or malignant."
    )
    st.write(
        "To use the app, extract a cell sample from the breast, perform laboratory tests, and enter the measured values "
        "into the sidebar. The model will then provide a prediction based on the input."
    )
    st.markdown("---")

  col1, col2 = st.columns([4,1])
  
  with col1:
    # for the graph
    radar_chart = get_radar_chart(input_data)
    st.plotly_chart(radar_chart)
  with col2:
    # for the prediction value
    add_predictions(input_data)
    
if __name__ == '__main__':
  main()