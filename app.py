import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Timetable Planner", layout="wide")

st.title("📅 AI Timetable & Daily Routine Generator")
st.markdown("Upload your class timetable as **text** or **image**, and get a smart daily routine!")

upload_type = st.radio("Choose input type:", ["📝 Text", "🖼️ Image"])

if upload_type == "📝 Text":
    timetable_text = st.text_area("Paste your class timetable here:")
else:
    timetable_image = st.file_uploader("Upload your class timetable (Image)", type=["png", "jpg", "jpeg"])
    if timetable_image:
        img = Image.open(timetable_image)
        st.image(img, caption="Your Uploaded Timetable", use_column_width=True)

if st.button("✨ Generate Daily Routine"):
    st.success("Here’s your smart routine:")
    st.markdown("""
    - ⏰ Wake Up: 6:30 AM  
    - 🍽️ Breakfast: 7:00 AM  
    - 📚 Classes: As per your timetable  
    - 📖 Study Time: 5:00 PM  
    - 🏋️ Gym/Yoga: 6:30 PM  
    - 📱 Social Break: 8:30 PM  
    - 😴 Sleep: 10:30 PM
    """)
