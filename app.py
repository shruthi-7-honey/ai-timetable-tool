       # OCR to extract text
    extracted_text = pytesseract.image_to_string(img)
    
    st.subheader("📄 Raw Extracted Timetable:")
    st.code(extracted_text)

    # 🧼 Clean the messy text
    def clean_text(text):
        lines = text.splitlines()
        useful_lines = []

        for line in lines:
            line = line.strip()
            if line == "" or line.lower() in ["sec", "vac"]:
                continue
            if any(char.isdigit() for char in line) and len(line) > 4:
                useful_lines.append(line)
        
        return useful_lines

    cleaned_lines = clean_text(extracted_text)

    st.subheader("🧹 Cleaned Timetable Lines:")
    for line in cleaned_lines:
        st.markdown(f"- {line}")

    # 🧠 Dummy Routine based on cleaned lines
    if st.button("✨ Generate Smart Routine"):
        st.success("Here’s your AI-based day plan 📅:")
        for i, line in enumerate(cleaned_lines):
            st.markdown(f"**Class {i+1}:** {line}")
        
        st.markdown("""
        - 🧘 Gym/Yoga: 6:30 AM  
        - 🍽️ Breakfast: 8:00 AM  
        - 📚 Classes: As above  
        - 📖 Study Time: 6:00 PM  
        - 📱 Chill Time: 8:00 PM  
        - 😴 Sleep: 10:30 PM
        """)

