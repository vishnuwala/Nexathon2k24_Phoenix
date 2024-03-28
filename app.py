import streamlit as st
from PIL import Image
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline


st.set_page_config(
    page_title="Text_2_Poster",
    page_icon="🖖",
)

st.title("Main Page 😊")
st.sidebar.success("Select a page above.")

st.write("Unleash the artist within! Our Text-to-Poster Generation project empowers you to transform your wildest ideas into captivating posters. With the magic of AI, simply describe your vision, and watch it blossom into a stunning visual masterpiece. Let words become worlds, and ignite your creative spark with a click.")

st.write("Say goodbye to design limitations! Our Text-to-Poster Generation project puts the power of customization in your hands. Craft a detailed description of your dream poster, and our intelligent system will translate your vision into a unique, personalized piece. Whether it's capturing a specific mood, theme, or style, your vision is our priority. Step into a world where words translate seamlessly into captivating visuals.")

st.write("These are just a few examples, feel free to mix and match or create your own based on your project's specific focus. You can also add details about the types of posters your project generates (abstract, minimalist, etc.) or the features it offers (customization options, style selection, etc.).")