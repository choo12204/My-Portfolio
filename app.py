import streamlit as st
from PIL import Image, ImageDraw, ImageOps
import base64
import requests
from io import BytesIO

st.set_page_config(page_title="Shinn Gee Choo | Portfolio", page_icon=":wrench:", layout="wide")

# Sidebar Navigation
st.sidebar.title("Portfolio Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Welcome",
        "About Me",
        "Python",
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
    banner_url = "https://raw.githubusercontent.com/choo12204/my-portfolio/main/DSC01631.JPG"
    response = requests.get(banner_url)
    banner_img = Image.open(BytesIO(response.content)).convert("RGB")
    banner_b64 = image_to_base64(banner_img, format="JPEG")

    # Load and crop profile image circular
    profile_url = "https://raw.githubusercontent.com/choo12204/my-portfolio/main/IMG_4185.JPG"
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
elif section == "Python Programming":
    st.header("🐍 Python Programming")
    
    st.subheader("Fundamentals")
    st.markdown("""
    - 🧠 **Key Learning Outcomes**  
    This 6-hour course from Mosh Hamedani on YouTube provided a complete beginner-to-intermediate understanding of Python programming, covering everything from fundamentals to building web apps and doing machine learning.
    """)

    st.subheader("📘 What I Learned")

    st.markdown("### 1. Core Python Concepts")
    st.markdown("""
    - Variables, data types (str, int, float, bool)
    - Arithmetic and logical operators
    - Control flow (`if`, `for`, `while`)
    - Functions with `*args` and `**kwargs`
    - Error handling with `try`, `except`, `finally`, `with`
    """)

    st.markdown("### 2. Data Structures")
    st.markdown("""
    - Lists, tuples, sets, and dictionaries
    - List comprehensions, `map()`, `filter()`, `zip()`
    - Stacks, queues, and custom containers
    """)

    st.markdown("### 3. Object-Oriented Programming (OOP)")
    st.markdown("""
    - Classes, objects, constructors
    - Instance vs class attributes
    - Inheritance, polymorphism, encapsulation
    - Special methods (`__str__`, `__repr__`)
    - Data classes and reusable modular components
    """)

    st.markdown("### 4. Modules and the Standard Library")
    st.markdown("""
    - Creating/importing modules and packages
    - File handling, date/time, JSON, CSV, SQLite
    - Automation using ZIP, email, PDF, and web scraping tools
    """)

    st.markdown("### 5. Working with External Packages")
    st.markdown("""
    - Installing packages via `pip` and `pipenv`
    - Using virtual environments
    - Accessing and securing APIs (e.g., Yelp, Twilio)
    """)

    st.markdown("### 6. Web Development with Django")
    st.markdown("""
    - Creating projects, apps, views, templates, and admin interfaces
    - Using Django ORM for database operations
    - Structuring URLs and handling HTTP requests/responses
    """)
    
    st.markdown("### 7. Introduction to Machine Learning")
    st.markdown("""
    - Understanding supervised learning and model training
    - Using `scikit-learn` for building, testing, and saving models
    - Data cleaning and visualization
    """)

    st.subheader("🔧 Tools & Practices")
    st.markdown("""
    - VS Code tips, debugging, extensions
    - Jupyter Notebooks for data analysis
    - Writing docstrings and maintaining clean, readable code
    """)

    st.subheader("📌 Takeaway")
    st.markdown("""
    This course gave me a strong foundation in Python, with practical skills in web development, automation, and machine learning.  
    It also emphasized best practices, clean code, and a clear understanding of the Python ecosystem.
    """)
  

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


