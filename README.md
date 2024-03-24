

***Text-to-Poster Generator***

This project allows users to generate unique and creative posters based on text prompts. 

**Features:**

* **User-friendly interface:** Interact with the model through a user-friendly Streamlit web app.
* **Text-to-image generation:** Input a text description, and the model creates a corresponding poster image.
* **Customization options:** Specify details like color scheme, design style, and key text elements to personalize your posters.
* **Colab support:** Run the Streamlit app directly within Google Colab for easy access and potential hardware acceleration (TPUs/GPUs).

**Requirements:**

* Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* Streamlit ([https://docs.streamlit.io/](https://docs.streamlit.io/))
* Text-to-image generation library (e.g., Stable Diffusion: [https://huggingface.co/spaces/stabilityai/stable-diffusion](https://huggingface.co/spaces/stabilityai/stable-diffusion)) - Might require additional dependencies.
* (Optional) Libraries for hardware acceleration like accelerate (consult specific library documentation)

**Quick Start (Google Colab):**

1. **Upload the project files to your Colab notebook.**
2. **Install required libraries:**

   ```bash
   !pip install streamlit <text-to-image_library_dependencies>
   ```

3. **Run the Streamlit app:**

   ```bash
   !streamlit run app.py &>/dev/null &
   ```

4. **Create a public URL with Ngrok (optional):**

   ```bash
   !ngrok authtoken YOUR_AUTHTOKEN  # Replace with your Ngrok authtoken
   !ngrok http 8501
   ```

   - Ngrok will provide a forwarding URL to access the app in your Colab browser.

**Usage:**

1. Open the Streamlit app in your Colab browser (or locally if running on your machine).
2. Enter details like title, color scheme, aim, key text elements, and design preference.
3. Click the "Generate Poster" button.
4. The app will generate a unique poster image based on your provided information.

**You can also create your own dataset and apply transfer learning for it checkout - https://huggingface.co/docs/diffusers/en/training/create_dataset**






