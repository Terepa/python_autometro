import os
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash_table import DataTable
import pandas as pd
import glob

# Find the latest file that starts with "checked_SKU_"
files = glob.glob("/app/output/checked_SKU_*.csv")

if files:
    latest_file = max(files, key=os.path.getctime)
    # Rest of your code...
else:
    print("No files matching the pattern found.")

# Load CSV data
df = pd.read_csv(latest_file)

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'])

# Define app layout
app.layout = html.Div([
    html.Div([
        html.H1("Checked SKU Data", className="display-4"),
        html.P("Explore and filter SKU data with Dash DataTable", className="lead"),
    ], className="jumbotron"),

    html.Div([


        # Input for filtering the selected column
        dcc.Input(id='filter-input', type='text', value='', className="form-control"),

        # Dropdown for selecting column to filter
        dcc.Dropdown(
            id='column-dropdown',
            options=[{'label': col, 'value': col} for col in df.columns if col not in ['instock']],
            value=df.columns[0],
            className="form-control",
            style={'width': '100%'}  # Set the width to 100%
        ),

        # Dropdown for selecting sort order for 'originaltransdate'
        dcc.Dropdown(
            id='date-sort-dropdown',
            options=[
                {'label': 'Ascending', 'value': 'asc'},
                {'label': 'Descending', 'value': 'desc'}
            ],
            value='asc',
            className="form-control",
            style={'width': '100%'}  # Set the width to 100%
        ),

    ], className="form-row my-3"),

    # DataTable for displaying the filtered data
    DataTable(
        id='data-table',
        columns=[

            {'name': col, 'id': col, 'selectable': True} for col in df.columns if col not in ['instock']
        ],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={'maxWidth': '300px', 'overflow': 'hidden', 'textOverflow': 'ellipsis'},
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="single",
        row_deletable=True
    ),
], className="container-fluid")

# Define callback to update DataTable based on user input
@app.callback(
    Output('data-table', 'data'),
    [Input('column-dropdown', 'value'),
     Input('filter-input', 'value'),
     Input('date-sort-dropdown', 'value')]
)
def update_table(selected_column, filter_value, date_sort_order):
    filtered_df = df[df[selected_column].astype(str).str.contains(filter_value, case=False)]

    # Additional filter rule
    if selected_column == 'itemname':
        filtered_df = filtered_df[
            (filtered_df['simple_product'] == 'not found') |
            (filtered_df['master_product'] == 'not found') |
            (filtered_df['carlist_product'] == 'not found')
            ]

    # Sort 'originaltransdate'
    if date_sort_order == 'asc':
        filtered_df = filtered_df.sort_values(by='originaltransdate', ascending=True)
    else:
        filtered_df = filtered_df.sort_values(by='originaltransdate', ascending=False)

    return filtered_df.to_dict('records')

# Run the app (LOCAL)
# if __name__ == '__main__':
#     app.run_server(debug=True)

# Run the app (PROD)
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
