import streamlit as st

st.set_page_config(page_title="My Engineering Portfolio",page_icon=":wrench:", layout="wide")

# Sidebar Navigation
st.sidebar.title("Portfolio Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Welcome",
        "About Me",
        "Real-Time Embedded Project",
        "Simulation & Modelling",
        "Linux & PPMAC Work",
        "Skills",
        "Why AB Dynamics?",
        "Contact"
    ]
)

# Welcome Section
if section == "Welcome":
    st.image("https://via.placeholder.com/1200x250.png?text=Welcome+to+My+Engineering+Portfolio",
             use_container_width=True)
    st.title("Engineering Portfolio")
    st.markdown("Use the menu on the left to explore my work and experiences.")

# About Me Section
elif section == "About Me":
    st.header("👋 About Me")
    st.markdown("""
    I’m an engineering student on track for a **2:1 or higher** in **Robotics Engineering**. I’m passionate about **real-time embedded systems**, **simulation**, and **automotive innovation**.

    My technical strengths and projects align well with AB Dynamics’ focus on safety, efficiency, and environmental impact in vehicle development.
    """)

# Embedded Project Section
elif section == "Real-Time Embedded Project":
    st.header("⚙️ Real-Time Embedded Software")
    st.subheader("PID Motor Control on STM32 (C/C++)")
    st.markdown("""
    - Developed a real-time PID motor control system using **C on STM32**
    - Implemented a **FreeRTOS** task scheduler
    - Designed to maintain speed control under dynamic load conditions
    """)
    st.code("""
    float computePID(float setpoint, float measured, float Kp, float Ki, float Kd) {
        static float integral = 0, last_error = 0;
        float error = setpoint - measured;
        integral += error;
        float derivative = error - last_error;
        last_error = error;
        return Kp * error + Ki * integral + Kd * derivative;
    }
    """, language="c")

# Simulation Section
elif section == "Simulation & Modelling":
    st.header("🧠 Simulation & Modelling")
    st.subheader("Autonomous Path Following with Simulink & Python")
    st.markdown("""
    - Created a **multi-level PID vehicle controller**
    - Built path tracking logic in **MATLAB/Simulink** and validated in Python
    - Simulated different terrains and sensor noise scenarios
    """)
    st.image("https://via.placeholder.com/800x300.png?text=Path+Following+Simulation", use_container_width=True)

# Linux/PPMAC Section
elif section == "Linux & PPMAC Work":
    st.header("🐧 Embedded Linux & PPMAC")
    st.markdown("""
    - Developed and deployed embedded C++ algorithms on **PPMAC** (Linux-based)
    - Integrated GPIO, PWM, and sensor control logic
    - Used **GDB** and shell scripts for remote debugging
    """)

# Skills Section
elif section == "Skills":
    st.header("🛠 Technical Skills")
    st.markdown("""
    - **Languages**: C, C++, Python, MATLAB
    - **Tools**: Simulink, FreeRTOS, STM32, PPMAC, Git, Linux
    - **Concepts**: PID control, real-time systems, kinematics, motor control
    - **Soft Skills**: Communication, time management, team collaboration
    """)

# Why AB Dynamics Section
elif section == "Why AB Dynamics?":
    st.header("🎯 Why AB Dynamics?")
    st.markdown("""
    AB Dynamics is an inspiring company pushing the boundaries of vehicle technology.

    Your mission to make vehicles **safer, more efficient**, and **environmentally conscious** aligns perfectly with my goals.

    I am excited about the opportunity to:
    - Apply real-time embedded skills
    - Contribute to automated testing platforms
    - Grow through multi-disciplinary collaboration
    """)

# Contact Section
elif section == "Contact":
    st.header("📫 Get in Touch")
    st.markdown("""
    - **Name**: [Your Name]  
    - **Email**: [your.email@example.com]  
    - **LinkedIn**: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)  
    - **GitHub**: [github.com/yourusername](https://github.com/yourusername)
    """)

