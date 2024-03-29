import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata
from sklearn.preprocessing import LabelEncoder

definitions_list = [
    "B60L7/10", "B60T1/10", "D21F5/20", "F01K17/02", "F01K17/06", "F01K27/02", "F02C7/10",
    "F02G5/00", "F15B21/14", "F16D61/00", "F17C9/04", "F22B1/16", "F22B1/18", "F22D1/40",
    "F22G1/02", "F22G1/12", "F22G5/06", "F23G5/46", "F24F3/147", "F24F12/00", "F24H8/00",
    "F27D17/00", "F28C1/08"
]

place_list = [
    ['F16D61/00', 'B60L7/10', 'F22B1/16', 'F23G5/46', 'F01K17/02'],
    ['F24F12/00', 'F22G1/02', 'F27D17/00', 'F02G5/00'],
    ['F15B21/14', 'F22D1/40', 'D21F5/20', 'F22G5/06', 'F28C1/08'],
    ['F01K17/06', 'F02C7/10', 'F17C9/04', 'F24H8/00', 'F22G1/12'],
    ['F01K27/02', 'F24F3/147', 'F22B1/18', 'B60T1/10']
]

cited_by = [80232, 63011, 749, 7333, 5182, 9054, 10206, 8631, 41461, 29970, 18330, 4448, 12867, 279, 1717, 304, 40, 22090, 10543, 5528, 13971, 3842, 280]

# Creating a DataFrame
result_dict = {'Table': definitions_list, 'x': [1,5,3,1,4,5,4,2,3,1,4,1,5,3,2,4,3,1,5,2,4,2,3], 'y': [2,4,3,5,1,1,2,4,1,1,3,3,3,2,2,5,4,4,2,1,4,3,5], 'cited_by': cited_by}
df = pd.DataFrame(result_dict)

# Use LabelEncoder to convert string labels to numerical values
label_encoder = LabelEncoder()
df['Table'] = label_encoder.fit_transform(df['Table'])

# Creating a 3D surface plot
fig = go.Figure()

# Scatter plot for points
scatter = fig.add_trace(go.Scatter3d(x=df['x'], y=df['y'], z=df['cited_by'], mode='markers',
                                    marker=dict(size=8, color=df['cited_by'], colorscale='Viridis', opacity=0.7),
                                    text=label_encoder.inverse_transform(df['Table'])))

# Interpolate to create a smooth surface
x_vals = np.linspace(df['x'].min(), df['x'].max(), 100)
y_vals = np.linspace(df['y'].min(), df['y'].max(), 100)
X, Y = np.meshgrid(x_vals, y_vals)

Z = griddata((df['x'], df['y']), df['cited_by'], (X, Y), method='cubic')

# Adding the smooth surface
fig.add_trace(go.Surface(x=x_vals, y=y_vals, z=Z, colorscale='Viridis', opacity=0.5, text=label_encoder.inverse_transform(df['Table'])))

# Updating layout to hide tick labels on x-axis and y-axis
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Cited By',
                             xaxis=dict(tickvals=[], ticktext=[]),  # hide x-axis ticks and labels
                             yaxis=dict(tickvals=[], ticktext=[]),  # hide y-axis ticks and labels
                             ),
                  scene_camera=dict(eye=dict(x=-1.2, y=-1.2, z=0.6)))

# Display the plot
fig.show()
