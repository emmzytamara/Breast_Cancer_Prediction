import streamlit as st
from utils.data_model import get_clean_data


def add_sidebar() -> dict:
    """
    Creates a sidebar in the Streamlit app with sliders for cell nuclei measurements.

    Each of the 30 features (e.g., radius_mean, texture_se, etc.) is represented by a slider
    allowing the user to input values, which can be used for predictions or visualizations.

    Returns:
        dict: A dictionary where keys are feature names and values are user-selected inputs
              from the sliders.
    """
    
    st.sidebar.header("Cell Nuclei Measurements")

    # Get the clean data
    data = get_clean_data()

    # create an label for the column
    slider_labels = [
          ("Radius (mean)", "radius_mean"),
          ("Texture (mean)", "texture_mean"),
          ("Perimeter (mean)", "perimeter_mean"),
          ("Area (mean)", "area_mean"),
          ("Smoothness (mean)", "smoothness_mean"),
          ("Compactness (mean)", "compactness_mean"),
          ("Concavity (mean)", "concavity_mean"),
          ("Concave points (mean)", "concave points_mean"),
          ("Symmetry (mean)", "symmetry_mean"),
          ("Fractal dimension (mean)", "fractal_dimension_mean"),
          ("Radius (se)", "radius_se"),
          ("Texture (se)", "texture_se"),
          ("Perimeter (se)", "perimeter_se"),
          ("Area (se)", "area_se"),
          ("Smoothness (se)", "smoothness_se"),
          ("Compactness (se)", "compactness_se"),
          ("Concavity (se)", "concavity_se"),
          ("Concave points (se)", "concave points_se"),
          ("Symmetry (se)", "symmetry_se"),
          ("Fractal dimension (se)", "fractal_dimension_se"),
          ("Radius (worst)", "radius_worst"),
          ("Texture (worst)", "texture_worst"),
          ("Perimeter (worst)", "perimeter_worst"),
          ("Area (worst)", "area_worst"),
          ("Smoothness (worst)", "smoothness_worst"),
          ("Compactness (worst)", "compactness_worst"),
          ("Concavity (worst)", "concavity_worst"),
          ("Concave points (worst)", "concave points_worst"),
          ("Symmetry (worst)", "symmetry_worst"),
          ("Fractal dimension (worst)", "fractal_dimension_worst"),
      ]

    input_dict = {}

    # Pairing 
    for label, key in slider_labels:
      input_dict[key] = st.sidebar.slider(
        label,
        min_value=float(0),
        max_value=float(data[key].max()),
        value=float(data[key].mean())
      )
      
    return input_dict