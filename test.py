import streamlit as st
import pandas as pd
import numpy as np



from PIL import Image

image = Image.open('blinkXLogoDark.jpg')
st.write("DB username:", st.secrets["api_key"])
st.image(image, caption='Sunrise by the mountains')
st.title('BlinkX ')