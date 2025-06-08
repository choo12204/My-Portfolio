import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import base64
import request
from io import BytesIO

st.set_page_config(page_title="Shinn Gee Choo | Portfolio", page_icon=":wrench:", layout="wide")

# Sidebar Navigation
st.sidebar.title("Portfolio Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Welcome",
        "About Me",
        "Real-Time Embedded Project",
        "Simulation & Modelling",
        "Linux Work",
        "Skills",
        "Contact"
    ]
)

def image_to_base64(img: Image.Image, format="PNG"):
    buffered = BytesIO()
    img.save(buffered, format=format)
    return base64.b64encode(buffered.getvalue()).decode()

# === Welcome Section ===
if section == "Welcome":
    # Load banner
    banner_url = "https://raw.githubusercontent.com/choo12204/My-Portfolio/main/images/DSC01631.JPG"
    response = requests.get(banner_url)
    banner_img = Image.open(BytesIO(response.content)).convert("RGB")
    banner_b64 = image_to_base64(banner_img, format="JPEG")

    # Load and crop profile image circular
    profile_url = "https://raw.githubusercontent.com/choo12204/My-Portfolio/main/images/IMG_4185.JPG"
    response = requests.get(profile_url)
    profile_img = Image.open(BytesIO(response.content)).convert("RGBA")


    size = min(profile_img.size)
    left = (profile_img.width - size) // 2
    top = (profile_img.height - size) // 2
    cropped = profile_img.crop((left, top, left + size, top + size))

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    circular = ImageOps.fit(cropped, (size, size))
    circular.putalpha(mask)
    circular_b64 = image_to_base64(circular)


    # HTML layout with overlap
    html = f"""
    <div style="position: relative; text-align: left;">
        <img src="data:image/jpeg;base64,{banner_b64}" style="width: 100%; border-radius: 10px;">
        <img src="data:image/png;base64,{circular_b64}"
             style="position: absolute; bottom: -60px; left: 40px;
                    width: 150px; height: 150px; border-radius: 50%; border: 5px solid white;">
    </div>
    <br><br>
    """

    st.markdown(html, unsafe_allow_html=True)





    # Profile Header
    st.markdown("## Shinn Gee Choo  \n**Meng Robotics Engineering Student at the University of Bath** \n**University of Bath**  \n📍 Bath, England, United Kingdom")

    # Open to Work
    st.markdown("### ✅ Open to Work")
    st.write("Mechanical Engineer, Electrical Engineer and Software Engineer Internship")

    # Final note
    st.markdown("---")
    st.markdown("👈 Use the sidebar to navigate through my portfolio and explore my engineering projects.")


elif section == "About Me":
    st.header("👋 About Me")
    st.markdown("""
I’m an aspiring **Robotics Engineer** currently pursuing a degree in **Robotics Engineering**, on track for a **2:1 or higher**. My passion lies in the intersection of **real-time embedded systems**, **mechanical design**, and **automotive innovation**.

Over the past few years, I’ve immersed myself in a variety of technical projects—ranging from building **mechatronic puzzle** and **self-balancing line-following robot**, to designing **control systems** and working on **CAD-based mechanical assemblies**. I enjoy pushing the limits of what's possible, especially when combining hardware and software to solve real-world problems.

My academic and extracurricular involvement with teams like **Team Bath Roving** and **Team Bath Hydrobotics** has honed my skills in:
- **Mechatronic integration**
- **Team-based design and development**
- **Rapid prototyping using 3D printing**

Outside of engineering, I’m active in sports, event organising, and creative technical hobbies like building **LEGO-based robots** and designing **Minecraft data packs** to experiment with logic and automation.

My goal is to become a forward-thinking engineer who blends creativity with robust technical foundations—whether it’s in **autonomous robotics**, **intelligent machines**, or **cutting-edge aerospace systems**.
    """)

# Embedded Project Section
elif section == "Real-Time Embedded Project":
    st.header("⚙️ Real-Time Embedded Software")
    st.subheader("PID Motor Control")
    st.markdown("""
    - Developed a real-time PID motor control system
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

# Linux Section
elif section == "Linux Work":
    st.header("🐧 Embedded Linux")
    st.markdown("""
    - Daily user of **Linux systems**, particularly **Arch Linux**, with a personalized development setup  
    - Experience running and maintaining projects on **Raspberry Pi**, including building an **ad-blocking server (Pi-hole)**  
    - Comfortable with **terminal-based workflows**, **shell scripting**, and system configuration  
    """)

elif section == "Skills":
    st.header("🛠 Technical Skills")
    st.markdown("""
    ### 💻 Programming & Coding
    - Proficient in: **Python**, **MATLAB**, **JavaScript**, **HTML**
    - Experience with **embedded systems** using Arduino

    ### 🧰 Tools & Software
    - **Microsoft Office**: Word, Publisher, PowerPoint (for technical reports & presentations)
    - **Adobe Dreamweaver**: Website and data pack creation using HTML/JavaScript
    - **3D CAD Software**: Design and additive manufacturing using CAD tools
    - **Circuit & PCB Design**: OrCAD Capture (schematic), PCB Designer (layout), PSpice (simulation)
    - **Simulation & Modeling**: MATLAB, Simulink
    - Version Control: Experienced in using GitHub to manage code changes and collaboration.
    - **Operating Systems**: Linux (Arch Linux with custom environment)

    ### 🤖 Robotics & Mechatronics
    - Experience building robotic systems (e.g. **quadruped**, **self-balancing line-following robot**)
    - Integration of mechanical, electrical, and software systems
    - Applying principles of **PID control** and **feedback loops** for precise movement
    - Familiarity with sensors such as **IMUs** and **infrared line sensors**
    - Prototyping and testing robotic hardware and software

    ### 📊 Data Analysis & Testing
    - Analyzing and visualizing data with **Excel** and **MATLAB**
    - Skilled in using **oscilloscopes**, **multimeters**, and **signal generators**

    ### 🤖 Machine Learning
    - Understanding of **supervised learning**, **regression**, and **classification**
    - Exposure to **scikit-learn**, **NumPy**, and **pandas**

    ### 🧪 Hardware & Soldering
    - Hands-on experience with **soldering**, prototyping, and electronics repair
    - Confident in **circuit testing**, **troubleshooting**, and iterative design

    ### 🧠 Engineering Concepts
    - Strong grasp of **kinematics**, **motor control**, and **real-time systems**

    ### 📋 Project Management
    - Experienced in project planning with **Gantt Charts**, **Agile workflows**, and tools like **Notion**

    ### 🤝 Soft Skills
    - Effective **communication**, **time management**, **problem-solving**, and **team collaboration**

    ### 🌐 Languages
    - Fluent in **English** & **Chinese**
    """)




# Contact Section
elif section == "Contact":
    st.header("📫 Get in Touch")
    st.markdown("""
    - **Name**: Choo Shinn Gee  
    - **Email**: chooshinngee@gmail.com
    - **LinkedIn**: [linkedin.com/in/choosg](https://linkedin.com/in/choosg)  
    - **GitHub**: [github.com/choo12204](https://github.com/choo12204)
    """)


