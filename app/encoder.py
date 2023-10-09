import numpy as np
import joblib
import pandas as pd


def encode(array):
    # Load the pre-trained LabelEncoder objects
    jurisdiction_encoder = joblib.load('Jurisdiction_label_encoder.pkl')
    substream_encoder = joblib.load('Sub_stream_name_label_encoder.pkl')
    category_encoder = joblib.load('Category_label_encoder.pkl')
    type_encoder = joblib.load('Type_label_encoder.pkl')
    management_encoder = joblib.load('Management_label_encoder.pkl')
    fate_encoder = joblib.load('Fate_label_encoder.pkl')

    # Sample values to encode
    selected_jurisdiction = array[0]
    selected_category = array[1]
    selected_type = array[2]
    selected_management = array[3]
    selected_fate = array[4]
    selected_substream = array[5]

    # Encode each value using the corresponding LabelEncoder
    encoded_jurisdiction = jurisdiction_encoder.transform([selected_jurisdiction])
    encoded_substream = substream_encoder.transform([selected_substream])
    encoded_category = category_encoder.transform([selected_category])
    encoded_type = type_encoder.transform([selected_type])
    encoded_management = management_encoder.transform([selected_management])
    encoded_fate = fate_encoder.transform([selected_fate])


    # In order to recieved client inputs appended these inputs (created above) into dictionary as we mentioned before. And We returned into dataframe.
    data_dict = {
        "Jurisdiction": encoded_jurisdiction[0],
        "Category": encoded_category[0],
        "Type": encoded_type[0],
        "Management": encoded_management[0],
        "Fate": encoded_fate[0],
        "Sub_stream_name": encoded_substream[0],
        "Year": array[0]
    }

    df = pd.DataFrame.from_dict([data_dict])

    columns = ['Jurisdiction', 'Category', 'Type', 'Management', 'Fate', 'Sub_stream_name', 'Year']
    # And appended column names into column list. We need columns to use with reindex method as we mentioned before.

    df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)

    return df
