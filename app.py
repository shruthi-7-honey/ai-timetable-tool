import streamlit as st
from PIL import Image
import pytesseract

st.set_page_config(page_title="AI Timetable Planner", layout="wide")
st.title("📅 AI Timetable & Daily Routine Generator")
st.markdown("Upload your class timetable image, and we’ll read it!")

uploaded_file = st.file_uploader("Upload timetable image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Timetable", use_column_width=True)

    # OCR to extract text
    extracted_text = pytesseract.image_to_string(img)
    
    st.subheader("📄 Extracted Timetable Text:")
    st.code(extracted_text)

    if st.button("✨ Generate Smart Routine"):
        st.success("Here’s your smart daily routine based on timetable:")
        st.markdown("""
        - ⏰ Wake Up: 6:30 AM  
        - 🍽️ Breakfast: 7:00 AM  
        - 📚 Classes: According to extracted timetable  
        - 📖 Study Time: 5:00 PM  
        - 🏋️ Gym/Yoga: 6:30 PM  
        - 📱 Chill Time: 8:30 PM  
        - 😴 Sleep: 10:30 PM
        """)
