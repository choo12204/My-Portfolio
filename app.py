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
        "PCB Design & Manufacture",
        "Mechanical Design & Manufacture",
        "Signal & Communication Systems",
        "Computational Simulation",
        "Data Analysis & Visualization",
        "Linux & Development Environment",
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
        I'm a passionate and curious engineering student pursuing an MEng in Robotics Engineering at the University of Bath. My journey blends creativity with technical problem-solving, from building quadruped robots in my free time to designing high-performance PCBs and embedded systems for real-world applications.
        
        I thrive at the intersection of mechanical design, electronics, and software. Through hands-on projects in CAD, control systems, power electronics, and machine learning, I've developed a solid foundation in designing and simulating complex systems. I’ve also contributed to open-source game development communities and led teams in both sports and engineering competitions.
        
        Whether it’s crafting a functional Arduino case, fine-tuning a buck converter in LTspice, or soldering components on a multilayer PCB, I take pride in learning by doing. I enjoy sharing what I learn, through code, collaboration, or community engagement.
        
        I'm driven by a vision to turn ideas into impactful innovations and I’m just getting started.
        
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
    
 # Simulation Section
elif section == "PCB Design & Manufacture":
    st.header("PCB Design & Manufacture")
    st.subheader("🛠️ Design for Manufacturing")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Schematic & PCB Design (OrCAD): Created microphone amplifier schematics, assigned footprints, and routed PCBs using OrCAD tools. Netlisted schematics and completed board layout in PCB Editor.
        - Custom Footprint Creation: Designed component padstacks (e.g., carbon resistor) in Padstack Editor and constructed new symbols like a quad OpAmp using Capture CIS.
        - Footprint Editing & Replacement: Modified library footprints using Padstack Replace to meet specific design requirements.
        - DFM Guideline Application: Applied design-for-manufacturing principles by selecting optimal pad sizes, trace widths, and spacing to reduce soldering issues and improve assembly reliability.
        - Multilayer PCB Design: Extended two-layer amplifier to a four-layer PCB with dedicated GND and power planes for enhanced signal integrity, reduced noise, and improved routing.
        - Justification of Multilayer Use: Compared cost-performance tradeoffs and justified use of four-layer PCBs in amplifier circuits for superior noise performance and reliability.
        """)
    with col2:
        st.image("Capture (1).PNG.png", use_container_width=True)
        st.image("3D.PNG.png", use_container_width=True)
        st.image("Screenshot (9) (1).png.3.png", use_container_width=True)

    st.subheader("🔥 Thermal Design")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Applied thermal management strategies in PCB design, such as adding wider copper traces and thermal vias, to reduce heat buildup and ensure safe operating temperatures.
        - Calculated thermal resistance to evaluate heat dissipation effectiveness, using formulas based on material conductivity, thickness, and area.
        - Reduced hotspot formation by optimizing copper trace width and enhancing heat transfer pathways.
        - Reflected on improving component layout by grouping heat-intensive parts near heat sinks for enhanced cooling and long-term reliability.
        """)
    with col2:
        st.image("IMG_0877.jpeg", use_container_width=True)
        st.image("Capture (2).PNG.3.png", use_container_width=True)
        st.image("thermaldesignpcbeditor.PNG.png", use_container_width=True)

    st.subheader("📶 Design for Signal Integrity")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Ensured robust circuit performance by implementing solid ground and power planes to minimize electromagnetic interference and provide clean return paths.
        - Shortened and strategically routed critical signal traces to avoid noisy components and reduce crosstalk.
        - Added decoupling capacitors to filter high-frequency noise and improve signal stability.
        - Applied signal integrity guidelines to enhance system reliability, especially under high-speed and noisy operating conditions.
        """)
    with col2:
        st.image("WhatsApp Image 2025-04-30 at 18.44.20.jpeg", use_container_width=True)
        st.image("SignalIntegritySchematic.PNG.png", use_container_width=True)

    st.subheader("🔩 PCB Assembly")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Participated in through-hole component soldering during Project Week, collaborating with two teammates to assemble the PCB without formal instructions.
        - Ensured clean and reliable solder joints by using appropriate solder amounts and spacing to prevent bridging or overflow.
        - Performed continuity testing post-assembly to verify proper electrical connections and prevent short circuits.
        - Successfully populated the board with components like resistors, capacitors, and ICs, contributing to a fully functional PCB.
        """)
    with col2:
        st.image("20240108_170344.jpg.2.jpg", use_container_width=True)


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
        st.image("Screenshot 2025-05-06 114010.png", use_container_width=True)
        st.image("Screenshot 2025-05-06 114953.png", use_container_width=True)
        st.image("Screenshot 2025-05-06 114000.png", use_container_width=True)

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
        st.image("page_1.png", use_container_width=True)
        st.image("page_2.png", use_container_width=True)
        


    

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
        st.image("transmissionlinemismatch.PNG.png", use_container_width=True)
        st.image("transmissionline.PNG.png", use_container_width=True)
        st.image("transmissionlinefreqresponse.PNG.png", use_container_width=True)


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
        st.image("cmos3.3.PNG.png.1.png", use_container_width=True)
        st.image("0.25.PNG.png.1.png", use_container_width=True)
        st.image("1mf.PNG.png.1.png", use_container_width=True)
        st.image("condition5.PNG.png.1.png", use_container_width=True)

# Simulation Section
elif section == "Computational Simulation":
    st.header("Computational Simulation")
    st.subheader("🧮 Computational Modelling & Analysis – 1D Heat Transfer Simulation")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        - Simulated 1D heat diffusion along a rod using the heat equation:∂T/∂t = α ∂²T/∂x² where T = temperature, α = thermal diffusivity.
        - Implemented both explicit and implicit numerical methods in MATLAB to analyze transient thermal behavior.
        - Applied two boundary condition types:
            - Dirichlet (fixed ends): Heat dissipated outward.
            - Neumann (insulated ends): Heat redistributed internally.
        - Initiated the system with a sinusoidal temperature profile to simulate realistic thermal gradients.
        - Analyzed stability:
            - Explicit method intuitive but unstable at large time steps.
            - Implicit method remained stable and accurate.
        - Insights applied to thermal system design, insulation engineering, and heat management in embedded systems.
        """)
    with col2:
        st.image("Screenshot 2025-03-20 141325.png", use_container_width=True)
        st.image("Screenshot 2025-03-20 141313.png", use_container_width=True)
        st.image("Screenshot 2025-05-01 120921.png", use_container_width=True)

    st.subheader("🧲 Finite Element Analysis – Wireless Power Transfer (WPT) System using Ansys HFSS")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        What I Did:
        - Modeled a wireless power transfer system using inductively coupled coils.
        - Applied Maxwell’s equations (Faraday’s Law & Magnetostatic curl) using the finite element method (FEM) in Ansys HFSS.
        - Defined the following model components:
            - Geometry: Two parallel circular copper coils
            - Material: Copper in a vacuum enclosure
            - Boundary: Radiation boundary to minimize wave reflection
            - Excitations: Lumped ports to simulate AC current input
            - Meshing: Adaptive refinement in high-field regions for accuracy
            - Solver: Frequency-domain sweep
        What I Analyzed:
        - Magnetic field distribution around coils to study energy transfer efficiency
        - Impedance vs. frequency to identify optimal resonance and minimize losses
        """)
    with col2:
        st.image("FEAoutput.PNG.png", use_container_width=True)
        st.image("fea.PNG.png", use_container_width=True)
        st.image("fea2.PNG.1.png", use_container_width=True)




# Simulation Section
elif section == "Data Analysis & Visualization":
    st.header("Data Analysis & Visualization – Sea Ice Concentration using MATLAB")
    st.subheader("📊 Data Analysis")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        What I Did:
        - Analyzed European Space Agency (ESA) sea ice data in MATLAB.
        - Imported and visualized the data using pseudocolor plots with latitude and longitude axes.
        - Created comparative visualizations for different seasons to study environmental patterns.
                    
        What I Discovered:
        - Darker shades indicate higher sea ice concentration; lighter shades show melt or water regions.
        - Observed seasonal variation: higher ice concentration in January (winter) and lower in August (summer).
        - Identified regional differences and melting trends, highlighting potential climate change impact.
        """)
    with col2:
        st.image("Screenshot 2024-04-25 000254.png", use_container_width=True)
        st.image("Screenshot 2024-04-24 231155.png", use_container_width=True)



    st.subheader("📈 Data Visualization")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        Purpose:
        - To transform complex geospatial data into clear, interpretable visuals for environmental insight and decision-making.
                    
        What I Did:
        - Used pseudocolor plots in MATLAB to map sea ice concentration over latitude and longitude.
        - Added axis labels and a colorbar to communicate geographic context and concentration levels clearly.
                    
        Why It Works:
        - Color mapping makes patterns in ice distribution easy to interpret.
        - Enables comparison across time and geography, supporting climate trend analysis and scientific communication.
        """)
    with col2:
        st.image("Screenshot 2024-04-24 235505.png", use_container_width=True)

    
# Simulation Section
elif section == "Linux & Development Environment":
    st.header("🐧 Linux & Development Environment")
    st.markdown("""
    - Dual-booted Arch Linux with Windows 11 to explore low-level system control and development workflows.
    - Gained hands-on experience configuring bootloaders, window managers, and resolving system issues independently.
    - Relied heavily on the Arch Wiki and open-source community to troubleshoot and understand the Linux ecosystem.
    - Developed greater confidence and problem-solving skills through real-world debugging and system customization.
    - Continued using Windows for daily tasks while leveraging Linux for experimentation and growth in open-source development.
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

