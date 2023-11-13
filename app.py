import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash_table import DataTable
import pandas as pd

# Load CSV data
df = pd.read_csv("output_with_status.csv")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    # Dropdown for selecting column to filter
    html.Label("Select Column to Filter:"),
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0]
    ),

    # Input for filtering the selected column
    html.Label("Filter Value:"),
    dcc.Input(id='filter-input', type='text', value=''),

    # DataTable for displaying the filtered data
    DataTable(
        id='data-table',
        columns=[
            {'name': col, 'id': col, 'selectable': True} for col in df.columns
        ],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        editable=True,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        row_selectable="single",
        row_deletable=True
    ),
])

# Define callback to update DataTable based on user input
@app.callback(
    Output('data-table', 'data'),
    [Input('column-dropdown', 'value'),
     Input('filter-input', 'value')]
)
def update_table(selected_column, filter_value):
    filtered_df = df[df[selected_column].astype(str).str.contains(filter_value, case=False)]
    return filtered_df.to_dict('records')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
