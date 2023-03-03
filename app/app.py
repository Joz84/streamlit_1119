import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
This is text""")


spell = st.secrets['spell']
key = st.secrets.some_magic_api.key

st.write(f"Ma super clé est maintenant visible pour tous : {key}")



df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)

head_df

@st.cache
def get_histo():

    df = pd.DataFrame(
            np.random.randn(200, 1),
            columns=['a']
        )

    return np.histogram(
        df.a, bins=25)[0]

hist_values = get_histo()

st.bar_chart(hist_values)



st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')