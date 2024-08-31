import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Sample data
data = pd.DataFrame({
    'x': np.arange(0, 100),
    'y': np.random.rand(100)
})

# Title of the dashboard
st.title('Simple Dashboard Example')

# Displaying a line chart
st.line_chart(data)

# Creating an interactive chart with Altair
chart = alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    tooltip=['x', 'y']
).interactive()

st.altair_chart(chart, use_container_width=True)