import streamlit as st
from PIL import Image
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
def runway(poster_prompt):
    model_id = "runwayml/stable-diffusion-v1-5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)

    pipe = pipe.to("cuda")

    

    # Prompt input for poster design
    



    # Generate image using Stable Diffusion
    with autocast("cuda"):
        output = pipe(poster_prompt, height=512, width=512)
        image = output["images"][0]  # Assuming "images" is the correct key
        image.save("poster_design_1.png")

        st.image(image)

    # Save the generated image
    print("Poster design generated and saved as 'poster_design_1.png'")
st.title("Runway 🏃‍♂️")
with st.form("my_form"):
   st.write("Inside the form")
   title_theme = st.text_input("Title/Theme: ")
   color_vibe = st.text_input("Color Scheme/Vibe: ")
   aim_objective = st.text_input("Aim/Objective of the Poster: ")
   key_text = st.text_input("Key Text Elements (separated by commas): ")
   design_pref = st.text_input("Design Preference or Design Vibe: ")
   additional_notes = st.text_input("Additional Notes/Preferences: ")
   

   # Every form must have a submit button.
   submitted = st.form_submit_button("Generate Poster")
   if submitted:
    poster_prompt = f"A {color_vibe} poster with a {design_pref} design style for {aim_objective}. "
    poster_prompt += f"The title or theme is '{title_theme}'. "
    poster_prompt += f"The key text elements are: {', '.join(key_text.split(','))}. "
    poster_prompt += additional_notes
    st.write("Poster Design Prompt:")
    st.markdown(poster_prompt)
    runway(poster_prompt)
       





# Formatting the prompt


# print("\nPoster Design Prompt:")
# print(poster_prompt)
