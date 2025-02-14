import streamlit as st
import pandas as pd

# Set page title and icon
st.set_page_config(page_title="Student Management System", page_icon="📚", layout="wide")

# Initialize session state for student records
if "students" not in st.session_state:
    st.session_state.students = {}  # Dictionary to store student data

# Sidebar menu
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/201/201818.png", use_container_width=True)  # Fixed parameter
menu = st.sidebar.radio("📌 Select an Option", 
                        ["🏠 Home", "➕ Add Student", "📋 View All Students", "🔍 Search Student", 
                         "✏️ Update Student", "❌ Delete Student", "📂 Export to CSV"])

st.title("📚 Student Management System")

# Home Section
if menu == "🏠 Home":
    st.subheader("🎓 Welcome to the Student Management System")
    st.write("This system allows you to **add, view, search, update, and delete** student records.")
    #st.image("https://www.kindpng.com/picc/m/234-2344302_student-management-system-hd-png-download.png", use_container_width=True)

# Add Student
elif menu == "➕ Add Student":
    st.subheader("➕ Add Student Record")
    student_id = st.text_input("🔢 Enter Student ID")
    name = st.text_input("👤 Enter Name")
    age = st.number_input("🎂 Enter Age", min_value=1, step=1)
    grade = st.text_input("🏆 Enter Grade")
    
    if st.button("✅ Add Student", type="primary"):
        if student_id and name and age and grade:
            if student_id in st.session_state.students:
                st.error("⚠️ Student ID already exists!")
            else:
                st.session_state.students[student_id] = {'name': name, 'age': age, 'grade': grade}
                st.success(f"✅ Student {name} added successfully!")
        else:
            st.warning("⚠️ Please fill all fields.")

# View All Students
elif menu == "📋 View All Students":
    st.subheader("📋 All Student Records")
    if not st.session_state.students:
        st.warning("⚠️ No students found.")
    else:
        df = pd.DataFrame.from_dict(st.session_state.students, orient="index").reset_index()
        df.columns = ["Student ID", "Name", "Age", "Grade"]
        st.data_editor(df, num_rows="dynamic")  # Editable Table

        # Button to Clear All Records
        if st.button("🗑 Clear All Students", type="primary"):
            st.session_state.students = {}  # Reset all records
            st.success("✅ All student records have been cleared.")

# Search Student
elif menu == "🔍 Search Student":
    st.subheader("🔍 Search Student")
    student_id = st.text_input("🔎 Enter Student ID to Search")
    
    if st.button("🔍 Search"):
        if student_id in st.session_state.students:
            student = st.session_state.students[student_id]
            st.success(f"**ID:** {student_id} | **Name:** {student['name']} | **Age:** {student['age']} | **Grade:** {student['grade']}")
        else:
            st.error("⚠️ Student not found.")

# Update Student
elif menu == "✏️ Update Student":
    st.subheader("✏️ Update Student Information")
    student_id = st.text_input("✏️ Enter Student ID to Update")

    if student_id in st.session_state.students:
        name = st.text_input("👤 New Name", value=st.session_state.students[student_id]['name'])
        age = st.number_input("🎂 New Age", min_value=1, step=1, value=st.session_state.students[student_id]['age'])
        grade = st.text_input("🏆 New Grade", value=st.session_state.students[student_id]['grade'])
        
        if st.button("✅ Update Student", type="primary"):
            st.session_state.students[student_id] = {'name': name, 'age': age, 'grade': grade}
            st.success(f"✅ Student {name} updated successfully!")
    elif student_id:
        st.error("⚠️ Student not found.")

# Delete Student
elif menu == "❌ Delete Student":
    st.subheader("❌ Delete Student Record")
    student_id = st.text_input("🗑 Enter Student ID to Delete")
    
    if st.button("❌ Delete", type="primary"):
        if student_id in st.session_state.students:
            del st.session_state.students[student_id]
            st.success("✅ Student deleted successfully!")
        else:
            st.error("⚠️ Student not found.")

# Export to CSV
elif menu == "📂 Export to CSV":
    st.subheader("📂 Export Student Records to CSV")
    
    if not st.session_state.students:
        st.warning("⚠️ No students found to export.")
    else:
        df = pd.DataFrame.from_dict(st.session_state.students, orient="index").reset_index()
        df.columns = ["Student ID", "Name", "Age", "Grade"]
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(label="📥 Download CSV", data=csv, file_name="student_records.csv", mime="text/csv")
        st.success("✅ Student records exported successfully!")
