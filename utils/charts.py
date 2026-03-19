import streamlit as st
import plotly.graph_objects as go
from utils.data_model import get_clean_data

def get_scaled_values(input_dict) -> dict:
    """
    Scales user input values to a `0–1` range based on the dataset's feature distribution.

    This function excludes the target column ('diagnosis') and performs min-max normalization 
    on each feature based on the original dataset.

    Args:
        input_dict (dict): A dictionary of user-provided input values from the sidebar.

    Returns:
        dict: A dictionary with scaled values for each input feature.
    """
    
    data = get_clean_data()
    
    X = data.drop(['diagnosis'], axis=1)
    
    scaled_dict = {}
    
    for key, value in input_dict.items():
        max_val = X[key].max()
        min_val = X[key].min()
        scaled_value = (value - min_val) / (max_val - min_val)
        scaled_dict[key] = scaled_value
    
    return scaled_dict

def get_radar_chart(input_data):
    """
    Creates a radar chart using Plotly to visualize 10 key features across three measurement types.

    The radar chart includes:
    - Mean values
    - Standard error (SE)
    - Worst-case values

    These are plotted across 10 features such as Radius, Texture, Perimeter, etc.

    Args:
        input_data (dict): A dictionary of user inputs to be scaled and plotted.

    Returns:
        plotly.graph_objects.Figure: A Plotly radar chart figure for visualization.
    """
  
    input_data = get_scaled_values(input_data)
    
    categories = ['Radius', 'Texture', 'Perimeter', 'Area', 
                  'Smoothness', 'Compactness', 
                  'Concavity', 'Concave Points',
                  'Symmetry', 'Fractal Dimension']

    fig = go.Figure()

    # Add traces for Mean Value, Standard Error, and Worst Value
    fig.add_trace(go.Scatterpolar(
        r=[input_data['radius_mean'], input_data['texture_mean'], input_data['perimeter_mean'],
           input_data['area_mean'], input_data['smoothness_mean'], input_data['compactness_mean'],
           input_data['concavity_mean'], input_data['concave points_mean'], input_data['symmetry_mean'],
           input_data['fractal_dimension_mean']],
        theta=categories,
        fill='toself',
        name='Mean Value'
    ))

    fig.add_trace(go.Scatterpolar(
        r=[input_data['radius_se'], input_data['texture_se'], input_data['perimeter_se'], input_data['area_se'],
           input_data['smoothness_se'], input_data['compactness_se'], input_data['concavity_se'],
           input_data['concave points_se'], input_data['symmetry_se'], input_data['fractal_dimension_se']],
        theta=categories,
        fill='toself',
        name='Standard Error'
    ))

    fig.add_trace(go.Scatterpolar(
        r=[input_data['radius_worst'], input_data['texture_worst'], input_data['perimeter_worst'],
           input_data['area_worst'], input_data['smoothness_worst'], input_data['compactness_worst'],
           input_data['concavity_worst'], input_data['concave points_worst'], input_data['symmetry_worst'],
           input_data['fractal_dimension_worst']],
        theta=categories,
        fill='toself',
        name='Worst Value'
    ))

    # Update the layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]  # Ensuring values are scaled between 0 and 1
            )
        ),
        showlegend=True,
        legend=dict(
            orientation='h',  # Horizontal layout for the legend
            yanchor='bottom',  # Position legend below the chart
            y=-0.2,  # Adjust position of legend (move it further down)
            xanchor='center',  # Align legend horizontally in the center
            x=0.5  # Center the legend
        ),
        width=800,  # Increase width
        height=800,  # Increase height
        title='Feature Comparison for Cell Characteristics'
    )
    
    return fig
