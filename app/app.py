# https://365datascience.com/tutorials/machine-learning-tutorials/how-to-deploy-machine-learning-models-with-python-and-streamlit/#5

import streamlit as st
import numpy as np
from prediction import predict
from encoder import encode

st.title('Predicting Non-Recycled Waste')
st.markdown('This app predicts the amount of non-recycled waste in a given Australian state by waste type.')

st.header('Waste features')

col1, col2 = st.columns(2)

selected_year = st.slider('Year', 2020, 2030)

with col1:
    st.text('Waste characteristics')

    jurisdiction = ['ACT', 'NSW', 'NT', 'Qld', 'SA', 'Tas', 'Vic', 'WA']
    selected_jurisdiction = st.selectbox("Select a state", jurisdiction)

    waste_category = ['Biosolids', 'Building and demolition materials', 'Glass',
                      'Hazardous wastes', 'Metals', 'Mining', 'Organics', 'Paper & cardboard',
                      'Plastics', 'Textiles, leather & rubber (excl. tyres)', 'Total',
                      'Unclassified materials', 'Mineral processing',
                      'Organic primary production', 'Organic processing', 'Ash']
    selected_category = st.selectbox("Select a waste category", waste_category)

    waste_type = ['Biosolids', 'Soil, sand and rock not contaminated above any threshold requiring classification as contaminated soils (N120)',
                  'Acids (B)', 'Alkalis (C)', 'Asbestos (N220)', 'Clinical and pharmaceutical (R)',
                  'Contaminated soils (N120)', 'Food-derived hazardous wastes (K100, K110)', 'Inorganic chemicals (D)',
                  'Oils (J)', 'Organic chemicals (M)', 'Organic solvents (G)', 'Other',
                  'Other hazardous organic wastes (K140, K190)', 'Other miscellaneous (other T)',
                  'Other soil/sludges (other N)', 'Paints, resins, inks, organic sludges (F)', 'Pesticides (H)',
                  'Plating and heat treatment (A)', 'Reactive chemicals (E)', 'Tyres (T140)', 'Food organics',
                  'Garden organics', 'Other organics', 'Timber', 'CSG brines', 'Red mud', 'Bauxite mining',
                  'Coal mining',
                  'Copper ore mining', 'Gold ore mining', 'Iron ore mining', 'Mineral sand mining', 'Nickel ore mining',
                  'Oil and gas extraction', 'Other construction material mining', 'Other metal ore mining',
                  'Other non-metallic mineral mining and quarrying', 'Silver-lead-zinc ore mining',
                  'Primary production animal waste', 'Primary production green waste',
                  'Primary production other organics',
                  'Primary production product loss', 'Primary production sludges', 'Broadacre crops food processing',
                  'Cotton gin trash', 'Fisheries food processing', 'Horticulture food processing',
                  'Livestock food processing',
                  'Sugarcane bagasse (available)', 'Sugarcane mill mud', 'Ash', 'Iron and steel',
                  'High density polyethylene (HDPE) (2)', 'Unclassified materials', 'Asphalt',
                  'Bricks, concrete and pavers', 'Plasterboard & cement sheeting', 'Aluminium', 'Rubble',
                  'Low density polyethylene (LDPE) (4)', 'Other plastics (7)', 'Polyethylene terephthalate (PET) (1)',
                  'Polypropylene (PP) (5)', 'Polystyrene (PS) (6)', 'Polyvinyl chloride (PVC) (3)',
                  'Leather & rubber (excl. tyres)', 'Textiles']
    selected_type = st.selectbox("Select a waste type", waste_type)

with col2:
    st.text("Waste management options")

    waste_fate = ['Disposal', 'Waste reuse', 'Energy recovery', 'Unknown', 'Long-term storage']
    selected_fate = st.selectbox("Select a fate option", waste_fate)

    waste_management = ['Other disposal', 'Waste reuse', 'Landfill', 'Energy from waste facility', 'Treatment', 'Unknown']
    selected_management = st.selectbox("Select a management option", waste_management)

    substream_options = ['C&I core', 'Total', 'C&D', 'MSW', 'C&I (mining)', 'C&I (mineral processing)', 'C&I (organic primary production)', 'C&I (organic processing)', 'C&I (electricity generation)']
    selected_substream = st.selectbox("Select a waste sub-stream", substream_options)


if st.button('Predict waste amount'):
    model_input = encode(np.array([selected_jurisdiction,
                                   selected_category,
                                   selected_type,
                                   selected_management,
                                   selected_fate,
                                   selected_substream,
                                   selected_year], dtype=object))
    result = predict(model_input)

    # Sample result
    result = [result[0]]

    # Convert the result to a float (in case it's not already)
    result_float = float(result[0])

    # Round the number to a specific number of decimal places (e.g., 2)
    rounded_result = round(result_float, 3)

    # Increase the font size and display the rounded number with text
    st.write(f"<span style='font-size: 36px;'>{rounded_result} tonnes of waste</span>", unsafe_allow_html=True)

