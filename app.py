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
        "Programming & Embedded Systems",
        "Circuits, Instrumentation and Power",
        "Mechanical Design & Manufacture",
        "Signal & Communication Systems",
        "Computational Simulation",
        "Data Analysis and Visualization",
        "Linux & Development Environment",
        "Team Projects & Competitions",
        "Sustainability and Engineering Impact",
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
I’m an aspiring **Robotics Engineer** currently pursuing a degree in **Robotics Engineering**, on track for a **2:1 or higher**. My passion lies in blending **embedded systems**, **mechanical design**, and **intelligent automation** to create real-world solutions.

Over the past few years, I’ve taken on a wide range of technical and hands-on engineering projects, including:

- Building a **self-balancing line-following robot** using Arduino and an MPU6050 sensor
- Developing a **mechatronic escape room puzzle** with touch sensors, LCDs, and custom enclosures
- Designing and manufacturing a **toy car** using milling, turning, and Styrofoam cutting machines
- Programming with **Python, C++, HTML, and JavaScript** for control systems, simulations, and web projects
- Setting up and managing **Linux development environments**, including Raspberry Pi projects
- Creating a **machine learning model** to predict PID gains for control systems
- Automating **Excel-based triathlon timing systems** using `openpyxl` and `matplotlib`
- Building a professional **Streamlit portfolio website** integrated with GitHub
- Designing and fabricating **custom PCBs** for embedded and power systems

As a committed team player, I’ve contributed to **Team Bath Roving** and **Team Bath Hydrobotics**, where I helped:
- Design and 3D-print **robotic components**, including a functional **gripper**
- Collaborate on multidisciplinary problems in simulation, electronics, and software
- Apply sustainable engineering practices in team competitions and events

Outside of engineering, I stay active in **sports**, enjoy **organising events**, and spend free time on technical hobbies like building **LEGO-based quadrupeds** and designing logic-driven **Minecraft data packs**.

My goal is to shape the future of **robotics**, **mechatronics**, or **aerospace systems** through innovative thinking and practical engineering excellence.
""")



# Embedded Project Section
elif section == "Programming & Embedded Systems":
    st.header("Programming & Embedded Systems")
    
    st.subheader("_Languages_")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 🐍 **Python**
        _Excel Automation for Triathlon Timing_
        - Automated ranking and result calculation for sports events using openpyxl and matplotlib.
        - Reduced manual processing time by over 80% and created visual reports using automated bar charts.
                    
        _PID Gain Prediction Using Machine Learning_
        - Built a multi-output regression model using scikit-learn to predict control system parameters.
        - Achieved MSE = 0.043 and visualized performance using matplotlib to validate predictions.
                    
        _Personal Portfolio Website (Streamlit)_
        - Designed and deployed a professional web app using Streamlit Cloud to showcase personal work
        - Integrated GitHub for live project updates
        - View project: streamlit portfolio
                    
        _Additional Learning_
        - Completed a 6-hour Python crash course by Mosh Hamedani to build a strong foundation in Python programming. 
        """)
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("1749381980605.jpg",caption="Excel Automation",use_container_width=True)
        st.image("1749381980670.jpg",caption="Machine Learning",use_container_width=True)
        st.image("Screenshot 2025-07-11 004530.png",caption="Portfolio",use_container_width=True)

    with col1:
        st.markdown("""
        ### **C++**  
        _Game Development_
        - Build a console-based Snake Game using C++.
                    
        _Additional Learning_
        - Complete The Cherno’s 16-hour C++ programming series on YouTube to strengthen understanding of C++ from the ground up.
        """)
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.video("C__Users_LENOVO_source_repos_Snake_x64_Debug_Snake.exe 2025-07-11 01-30-35.mp4")
    with col1:
        st.markdown("""
        ### **Javascript**  
        _Minecraft Datapack_
        - Inspired by *Heroes of Olympus*, I transformed myth into gameplay by designing 9 unique demigod characters using Minecraft Origins and custom JSON logic. 
        - Shared with 100+ players, the project combined creativity, reverse engineering, and community contribution.
        """)
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.image("1747066712134.jpg",caption="Character: Percy",use_container_width=True)


    with col1:
    
        st.markdown("""
        ### **HTML**  
        
        """)

    with col1:
        st.subheader("_Projects_")
        st.markdown("""
        ### **⚖️ Self Balancing Robot**  
        _What I Accomplished_
        - Build a two-wheeled self-balancing robot using an Arduino and an MPU6050 gyroscope sensor to detect tilt an angular motion.
        - Used Lego parts for the robot frame to allow quick prototyping and to adapt to limited resources (no access to a 3D printer).
        - Programmed the control system using the Arduino IDE, applying a PID controller to stabilize the robot by adjusting motor speeds based on tilt.
        - Designed and simulated the control system in Simulink to model system behaviour and validate PID tuning before applying it to hardware. 
                    
        _Additional Learning_
        - Watched a 1-hour video playlist explaining PID control theory to understand how proportional, integral, and derivative terms affect system response.
        """)
    with col2:
        st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
        st.video("selfbalancingrobot.mp4")
    
     
    with col1:
        st.markdown("""
        ### **🧩 Mechatronic Escapade**  
        _What I Accomplished_
        - Utilised creativity to design and build an engaging escape room puzzle, using touch pads, buttons and lcd screen to enhance user experience.  
        - Utilised CAD software and additive manufacturing techniques to produce the case and the lid.  
        - Programmed the embedded system and circuit using Arduino.  
        - Applied Gantt Chart, Design and Development and Risk Matrix to streamline project management, and risk mitigation.  
        - Created Presentation slides, Datasheet and Social Media posts to effectively communicate technical information. 
        """)
    with col2:
        st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
        st.image("Screenshot 2024-03-13 095855.png",caption="3D Model",use_container_width=True)
        st.image("WhatsApp Image 2024-03-10 at 7.16.36 PM.jpeg",caption="Circuit Prototype",use_container_width=True)

    with col1:
        st.markdown("<br><br><br><br><br><br><br>", unsafe_allow_html=True)
        st.markdown("""
        ### **🥧 Raspberry Pi**  
        _In Progress_
        - Set up Pi-hole to block ads and trackers across all devices using DNS filtering.
        - Install OpenMediaVault (OMV) to turn the Raspberry Pi into a personal NAS.
        - Configure Samba file sharing via OMV to allow secure access to shared folders from any device. 
        """) 
        

# Simulation Section
elif section == "Circuits, Instrumentation and Power":
    st.header("Circuits, Instrumentation and Power")
    st.subheader("🌀 Induction Electrical Machine Simulation")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Simulated a three-phase induction machine using MATLAB/Simulink to analyze performance under varying load conditions.
        - Monitored key operational parameters:
            - Rotor Speed (rpm)
            - Electromagnetic Torque (N·m)
            - Line Voltage (V)
            - Phase Current (A)
        - Developed a realistic model incorporating a mechanical load and stop condition that halts the system when the motor speed reaches zero.
        - Connected a voltage source and used measurement blocks to dynamically visualize machine behavior.
        - Evaluated system efficiency and operational response using graphical outputs for torque-speed and voltage-current relationships.
        - Gained deeper insights into motor startup, load response, and steady-state dynamics.
        """)
    with col2:
        st.image("Screenshot 2025-03-17 124049.png.1.png", use_container_width=True)
        st.image("Screenshot 2025-03-17 124100.png.2.png", use_container_width=True)
        st.image("Screenshot 2025-03-17 124005.png", use_container_width=True)

    st.subheader("🛠 Motor Speed Control Circuit")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Designed and implemented a switch-mode motor drive circuit to control DC motor speed using PWM.
        - Used a MOSFET for power regulation and DIG OUT for digital PWM signal control.
        - Incorporated a diode for voltage spike protection and a capacitor to reduce electrical noise.
        - Set R2 = 100Ω to tune circuit response.
        - Built and tested the circuit on a breadboard using a waveform generator.
        - Measured duty cycle vs RPM, analyzing motor performance under variable control.
        - Identified limitations:
            - Low resolution at certain duty cycles; suggested increasing PWM frequency.
            - Load sensitivity causing unstable speed; proposed using a closed-loop feedback system with a speed sensor.
        """)
    with col2:
        st.image("graphdutyy (1).png", use_container_width=True)
        st.video("VID_20250312_145759.mp4")

    st.subheader("🤖 Dynamic System Simulation in Simulink")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Modeled and simulated a robotic mouse control system using MATLAB/Simulink.
    - Developed logic to calculate a sensor voltage ratio to determine steering direction:
    - Ratio = Right sensor voltage / Left sensor voltage
    - Implemented motor duty cycle control based on ratio:
        - If Ratio > 1 → Right = 1/Ratio, Left = 1
        - If Ratio < 1 → Left = Ratio, Right = 1
    - Used Max blocks to cap duty cycles at 1, ensuring safe operation.
    - Ensured interdependence between left and right motor speeds for accurate turning behavior.
    - Visualized and tested logic using separated logic blocks in Simulink for clarity and modularity.
        """)
    with col2:
        st.image("Simulink.png",caption="Simulink", use_container_width=True)
        st.image("Screenshot 2025-03-13 142832.png",caption="Left Output", use_container_width=True)
        st.image("Screenshot 2025-03-13 142839.png",caption="Right Output", use_container_width=True)

    st.subheader("⚡ Power Electronics Simulation and Design Evaluation")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Designed and simulated two independent buck converters using LTspice, stepping down an 8.4V input to a lower voltage output (Vout1 & Vout2).
        - Demonstrated accurate start-up and voltage settling behavior, confirming proper converter operation.
        - Used inductors, capacitors, diodes, and PWM-controlled switches to regulate power delivery and smooth output.
        - Highlighted real-world relevance in robotics, motor drivers, and battery-powered systems, where efficient voltage control is crucial.
        - Validated component selection and timing through simulation, preventing design flaws before hardware prototyping.
        - Developed simulation skills applicable to embedded systems, EV modules, and DC-DC power control circuits.
        """)
    with col2:
        st.image("circuit diagram (1).png",caption="Simulation", use_container_width=True)
        st.image("simulation (1).png",caption="Circuit Diagram", use_container_width=True)
    
        


# Mechanical Design & Manufacture Section
elif section == "Mechanical Design & Manufacture":
    st.header("Mechanical Design & Manufacture")

    st.subheader("🧩 3D CAD Design: Arduino Case using Autodesk Inventor")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Designed a functional Arduino case using Autodesk Inventor, incorporating precise cutouts and ventilation.
        - Used **“Extrude”** to create the main structural box from two rectangles with varied dimensions.
        - Applied the **“Pattern”** tool to mirror ventilation slits and cable holes across symmetrical planes for consistent airflow design.
        - Engraved a username tag using the **“Emboss”** feature with a 0.5mm depth for personalization and professional finish.
        """)
    with col2:
        st.image("Screenshot 2024-03-13 095855.png", caption="3D Case", use_container_width=True)

    st.subheader("📐 2D CAD Drawing: Technical Documentation of Arduino Case")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Placed base view with top, right, and isometric projections using the **“Base”** tool.
        - Measured dimensions and applied tolerances using the **“Dimensions”** tool.
        - Customized the **“Title Block”** to include username and drawing details for professional documentation.
        """)
    with col2:
        import base64
        with open("PW3caseA.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        st.markdown(f'''
            <iframe src="data:application/pdf;base64,{base64_pdf}"height="200" type="application/pdf"></iframe>
        ''', unsafe_allow_html=True)

    st.subheader("🧩 Additive Manufacturing")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Prepared and exported STL files for 3D printing using Autodesk Inventor.
        - Designed a print-ready Arduino case that required no support structures due to stable geometry and optimal orientation.
        - Oriented the model to lay flat on the print bed, minimizing print errors and ensuring dimensional accuracy.
        - Evaluated and improved the design by proposing threaded corners for a screw-on lid (not printed due to time constraints).
        - Developed an understanding of rapid prototyping workflow, including slicing setup and design-for-manufacture considerations.
        """)
    with col2:
        st.image("image (1).png", caption="Sliced Part", use_container_width=True)

    

    
# Simulation Section
elif section == "Signal & Communication Systems":
    st.header("Signal & Communication Systems")
    st.subheader("🎧 Spectrogram Generation and Analysis (Class AB Amplifier – MATLAB)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Designed and simulated a Class AB amplifier to amplify a 1 kHz sinusoidal signal using MATLAB.
        - Ensured correct transistor biasing to minimize crossover distortion and maintain active region operation.
        - Used a push-pull transistor configuration with a quiescent current to enable smooth signal transition.
        - Calculated output voltage based on transistor behavior (collector/emitter current, load resistance).
        - Analyzed input and output signals for waveform fidelity and amplification accuracy.
        - Added simulated noise to model non-linearities and environmental interference, emulating real-world conditions.
        - Characterized the amplified signal through spectrogram and time-series analysis to evaluate system performance.
        """)
    with col2:
        st.image("C:/Users/LENOVO/Pictures/Screenshot 2025-05-06 114010.png", use_container_width=True)
        st.image("C:/Users/LENOVO/Pictures/Screenshot 2025-05-06 114953.png", use_container_width=True)
        st.image("C:/Users/LENOVO/Pictures/Screenshot 2025-05-06 114000.png", use_container_width=True)

    st.subheader("🎛️ FIR Filter Design (MATLAB)")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Developed a Finite Impulse Response (FIR) bandpass filter to isolate a narrow frequency range from noisy input data.
        - Applied Hamming window technique to shape the filter response, achieving minimal passband ripple and high stopband attenuation.
        - Calculated and defined precise cut-off and passband edge frequencies for accurate signal selection.
        - Simulated and analyzed pre- and post-filter signals in both time and frequency domains to verify filter performance.
        - Gained practical experience in noise suppression, signal isolation, and filter tuning — key concepts in real-world signal processing applications.
        """)
    with col2:
        st.image("C:/Users/LENOVO/Downloads/page_1.png", use_container_width=True)
        st.image("C:/Users/LENOVO/Downloads/page_2.png", use_container_width=True)
        


    

    st.subheader("📡 Characterisation of a Transmission Line")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Analyzed waveforms for open-circuit, short-circuit, mismatched, and matched transmission lines using simulation tools.
        - Demonstrated the effect of impedance mismatch (e.g., 50Ω source with 100Ω load), leading to signal reflections and standing waves.
        - Identified in-phase and phase-inverted reflections in open and short-circuited scenarios, respectively.
        - Validated that proper impedance matching minimizes reflections and maximizes power transfer.
        - Interpreted frequency response plots to show how mismatches introduce resonance and degrade signal fidelity.
        - Investigated data rate limitations due to attenuation, dispersion, and inter-symbol interference (ISI).
        - Highlighted the impact of high-frequency losses (skin effect, dielectric absorption) on transmission quality.
        - Discussed bandwidth vs. data rate trade-offs and suggested techniques like equalization and impedance matching to mitigate degradation.
        """)
    with col2:
        st.image("C:/Users/LENOVO/Downloads/transmissionlinemismatch.PNG.png", use_container_width=True)
        st.image("C:/Users/LENOVO/Downloads/transmissionline.PNG.png", use_container_width=True)
        st.image("C:/Users/LENOVO/Downloads/transmissionlinefreqresponse.PNG.png", use_container_width=True)


    st.subheader("🔗 Characterisation of Coupled Transmission Lines")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Simulated coupled transmission lines to evaluate crosstalk behavior under varying coupling capacitance (C₀) and impedance conditions.
        - Verified that impedance matching (R = 200Ω) reduces reflections and maintains clean signal transitions across Vin(t), Vout(t), Vnear(t), and Vfar(t).
        - Demonstrated how increasing C₀ from 0.25nF to 1nF intensifies crosstalk, shown by waveform distortions at Vnear and Vfar.
        - Compared 3.3V CMOS input levels with matched vs mismatched loads; higher voltage increased signal swing but preserved shape when properly matched.
        - Analyzed the effect of a 2000Ω high impedance mismatch, which caused repeated signal reflections, waveform distortion, and extreme crosstalk.
        - Highlighted that reflections and crosstalk degrade signal quality and limit maximum data rates in high-speed transmission lines.
        - Reinforced the importance of impedance matching and capacitive isolation to maintain signal integrity in PCB and communication line design.
        """)
    with col2:
        st.image("C:/Users/LENOVO/Downloads/cmos3.3.PNG.png.1.png", use_container_width=True)
        st.image("C:/Users/LENOVO/Downloads/0.25.PNG.png.1.png", use_container_width=True)
        st.image("C:/Users/LENOVO/Downloads/1mf.PNG.png.1.png", use_container_width=True)
        st.image("C:/Users/LENOVO/Downloads/condition5.PNG.png.1.png", use_container_width=True)





# Simulation Section
elif section == "Computational Simulation":
    st.header("Computational Simulation")
    st.subheader("Autonomous Path Following with Simulink & Python")
    st.markdown("""
    - Created a **multi-level PID vehicle controller**
    - Built path tracking logic in **MATLAB/Simulink** and validated in Python
    - Simulated different terrains and sensor noise scenarios
    """)
    st.image("https://via.placeholder.com/800x300.png?text=Path+Following+Simulation", use_container_width=True)

# Simulation Section
elif section == "Data Analysis & Visualization":
    st.header("Data Analysis & Visualization")
    st.subheader("Autonomous Path Following with Simulink & Python")
    st.markdown("""
    - Created a **multi-level PID vehicle controller**
    - Built path tracking logic in **MATLAB/Simulink** and validated in Python
    - Simulated different terrains and sensor noise scenarios
    """)
    st.image("https://via.placeholder.com/800x300.png?text=Path+Following+Simulation", use_container_width=True)

# Simulation Section
elif section == "Linux & Development Environment":
    st.header("Linux & Development Environment")
    st.subheader("Autonomous Path Following with Simulink & Python")
    st.markdown("""
    - Created a **multi-level PID vehicle controller**
    - Built path tracking logic in **MATLAB/Simulink** and validated in Python
    - Simulated different terrains and sensor noise scenarios
    """)
    st.image("https://via.placeholder.com/800x300.png?text=Path+Following+Simulation", use_container_width=True)

# Simulation Section
elif section == "Team Projects & Competitions":
    st.header("Team Projects & Competitions")
    st.subheader("Autonomous Path Following with Simulink & Python")
    st.markdown("""
    - Created a **multi-level PID vehicle controller**
    - Built path tracking logic in **MATLAB/Simulink** and validated in Python
    - Simulated different terrains and sensor noise scenarios
    """)
    st.image("https://via.placeholder.com/800x300.png?text=Path+Following+Simulation", use_container_width=True)

# Simulation Section
elif section == "Sustainability & Engineering Impact":
    st.header("Sustainability & Engineering Impact")
    st.subheader("Autonomous Path Following with Simulink & Python")
    st.markdown("""
    - Created a **multi-level PID vehicle controller**
    - Built path tracking logic in **MATLAB/Simulink** and validated in Python
    - Simulated different terrains and sensor noise scenarios
    """)
    st.image("https://via.placeholder.com/800x300.png?text=Path+Following+Simulation", use_container_width=True)
    
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

