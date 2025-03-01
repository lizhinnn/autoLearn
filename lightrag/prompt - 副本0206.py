GRAPH_FIELD_SEP = "<SEP>"

PROMPTS = {}

PROMPTS["DEFAULT_TUPLE_DELIMITER"] = "<|>"
PROMPTS["DEFAULT_RECORD_DELIMITER"] = "##"
PROMPTS["DEFAULT_COMPLETION_DELIMITER"] = "<|COMPLETE|>"
PROMPTS["process_tickers"] = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

# 已修改
PROMPTS["DEFAULT_ENTITY_TYPES"] = [
    "ControlSystem",          # 控制系统（例如：PID控制器、状态反馈控制器）
    "MathematicalModel",      # 数学模型（例如：传递函数、状态空间模型）
    "Component",              # 组件（例如：传感器、执行器、滤波器）
    "Algorithm",              # 算法（例如：卡尔曼滤波、LQR控制）
    "Theorem",                # 定理（例如：奈奎斯特稳定性判据、劳斯-赫尔维茨准则）
    "Concept",                # 概念（例如：稳定裕度、相位裕度）
    "Equation",               # 方程（例如：微分方程、代数方程）
    "Experiment",             # 实验（例如：阶跃响应实验、频率响应实验）
    "Application",            # 应用（例如：无人机控制系统、自动驾驶汽车）
    "Parameter",              # 参数（例如：增益、时间常数）
    "PerformanceMetric",      # 性能指标（例如：上升时间、超调量）
    "Simulation",             # 仿真（例如：MATLAB/Simulink仿真）
    "Tool",                   # 工具（例如：MATLAB、Python控制库）
    "Person",                 # 人物（例如：课程教授、研究者）
    "Organization",           # 组织（例如：研究机构、大学）
    "Event",                  # 事件（例如：学术会议、研讨会）
    "Publication",            # 出版物（例如：论文、书籍）
]

# 已修改
PROMPTS["entity_extraction"] = """-Goal-
Given a text document that is potentially relevant to modern control principles and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities. The focus should be on concepts, algorithms, models, components, and applications in the field of control systems.

-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, use same language as input text. If English, capitalized the name.
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes, properties, and significance in the context of control systems
Format each entity as ("entity"{tuple_delimiter}<entity_name>{tuple_delimiter}<entity_type>{tuple_delimiter}<entity_description>

2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
- relationship_keywords: one or more high-level key words that summarize the overarching nature of the relationship, focusing on concepts or themes rather than specific details
Format each relationship as ("relationship"{tuple_delimiter}<source_entity>{tuple_delimiter}<target_entity>{tuple_delimiter}<relationship_description>{tuple_delimiter}<relationship_keywords>{tuple_delimiter}<relationship_strength>)

3. Identify high-level key words that summarize the main concepts, themes, or topics of the entire text. These should capture the overarching ideas present in the document, particularly those related to control theory and applications.
Format the content-level key words as ("content_keywords"{tuple_delimiter}<high_level_keywords>)

4. Return output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.

5. When finished, output {completion_delimiter}

######################
-Examples-
######################
Example 1:

Entity_types: [control_system, component, algorithm, model, application, principle, concept, parameter, equation, theorem]
Text:
In the design of an automatic temperature control system, engineers apply the PID (Proportional-Integral-Derivative) controller to maintain a stable temperature within a predefined range. The PID controller adjusts its output based on the error between the setpoint and the measured process variable. A common mathematical model used for this purpose is the first-order plus dead time (FOPDT) model. This model captures the dynamics of the system with a simple yet effective approach. Engineers also consider the Nyquist stability criterion to ensure the closed-loop system remains stable under various operating conditions.
################
Output:
("entity"{tuple_delimiter}"Automatic Temperature Control System"{tuple_delimiter}"control_system"{tuple_delimiter}"A system designed to automatically maintain a stable temperature within a specified range using feedback control."){record_delimiter}
("entity"{tuple_delimiter}"PID Controller"{tuple_delimiter}"component"{tuple_delimiter}"A type of control loop feedback mechanism widely used in industrial control systems, consisting of proportional, integral, and derivative terms."){record_delimiter}
("entity"{tuple_delimiter}"First-Order Plus Dead Time (FOPDT) Model"{tuple_delimiter}"model"{tuple_delimiter}"A simplified mathematical model used to describe the dynamic behavior of a control system, characterized by a first-order response and a time delay."){record_delimiter}
("entity"{tuple_delimiter}"Nyquist Stability Criterion"{tuple_delimiter}"theorem"{tuple_delimiter}"A method used in control theory to determine the stability of a closed-loop system by analyzing the frequency response of the open-loop transfer function."){record_delimiter}
("relationship"{tuple_delimiter}"PID Controller"{tuple_delimiter}"Automatic Temperature Control System"{tuple_delimiter}"The PID Controller is used within the Automatic Temperature Control System to adjust the output based on the temperature error."{tuple_delimiter}"feedback control, error correction"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"First-Order Plus Dead Time (FOPDT) Model"{tuple_delimiter}"Automatic Temperature Control System"{tuple_delimiter}"The FOPDT Model is used to mathematically represent the dynamics of the Automatic Temperature Control System."{tuple_delimiter}"system modeling, dynamic behavior"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Nyquist Stability Criterion"{tuple_delimiter}"Automatic Temperature Control System"{tuple_delimiter}"The Nyquist Stability Criterion is applied to ensure the stability of the Automatic Temperature Control System."{tuple_delimiter}"stability analysis, frequency response"{tuple_delimiter}7){record_delimiter}
("content_keywords"{tuple_delimiter}"temperature control, PID controller, FOPDT model, stability criterion, feedback control"){completion_delimiter}
#############################
Example 2:

Entity_types: [control_system, component, algorithm, model, application, principle, concept, parameter, equation, theorem]
Text:
Feedback linearization is a nonlinear control technique that transforms a nonlinear system into a linear one, simplifying the design of controllers. It is particularly useful when dealing with systems that have complex nonlinear dynamics. In the context of robotic manipulators, feedback linearization can be used to achieve precise motion control, ensuring that the end-effector follows a desired trajectory accurately. The backstepping control method is often combined with feedback linearization to further enhance the performance of the control system. Both techniques rely on Lyapunov stability theory to guarantee the stability of the controlled system.
#############
Output:
("entity"{tuple_delimiter}"Feedback Linearization"{tuple_delimiter}"algorithm"{tuple_delimiter}"A nonlinear control technique that transforms a nonlinear system into a linear one, making it easier to design controllers."){record_delimiter}
("entity"{tuple_delimiter}"Robotic Manipulator"{tuple_delimiter}"application"{tuple_delimiter}"An application of control systems where precise motion control is required to ensure accurate end-effector movement."){record_delimiter}
("entity"{tuple_delimiter}"Backstepping Control Method"{tuple_delimiter}"algorithm"{tuple_delimiter}"A control strategy that incrementally designs a controller for a system, often used in conjunction with feedback linearization to improve performance."){record_delimiter}
("entity"{tuple_delimiter}"Lyapunov Stability Theory"{tuple_delimiter}"theorem"{tuple_delimiter}"A theoretical framework used to prove the stability of nonlinear systems, providing a basis for designing stable control systems."){record_delimiter}
("relationship"{tuple_delimiter}"Feedback Linearization"{tuple_delimiter}"Robotic Manipulator"{tuple_delimiter}"Feedback Linearization is applied to robotic manipulators to achieve precise motion control."{tuple_delimiter}"nonlinear control, motion accuracy"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Backstepping Control Method"{tuple_delimiter}"Feedback Linearization"{tuple_delimiter}"The Backstepping Control Method is often combined with Feedback Linearization to enhance the performance of the control system."{tuple_delimiter}"performance enhancement, control design"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Lyapunov Stability Theory"{tuple_delimiter}"Feedback Linearization"{tuple_delimiter}"Lyapunov Stability Theory provides the theoretical foundation for proving the stability of systems controlled by Feedback Linearization."{tuple_delimiter}"stability proof, theoretical basis"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"Lyapunov Stability Theory"{tuple_delimiter}"Backstepping Control Method"{tuple_delimiter}"Lyapunov Stability Theory also underpins the stability analysis of systems controlled using the Backstepping Control Method."{tuple_delimiter}"stability analysis, theoretical support"{tuple_delimiter}6){record_delimiter}
("content_keywords"{tuple_delimiter}"feedback linearization, nonlinear control, robotic manipulator, precise motion control, backstepping control, lyapunov stability, system stability, performance enhancement, control design"){completion_delimiter}
#############################
Example 3:

Entity_types: [control_system, component, algorithm, model, application, principle, concept, parameter, equation, theorem]
Text:
In the development of an Unmanned Aerial Vehicle (UAV) flight control system, engineers utilize advanced control techniques to ensure stable and precise flight. The UAV's flight dynamics are modeled using a nonlinear state-space representation, which captures the complex interactions between the vehicle's attitude, velocity, and position. To stabilize the UAV during flight, a Model Predictive Control (MPC) algorithm is employed. This algorithm predicts future states of the UAV based on current inputs and adjusts the control inputs in real-time to minimize tracking errors.

The MPC controller also takes into account constraints such as maximum thrust and angle limits to ensure safe operation. Additionally, the Kalman filter is used for state estimation, providing accurate estimates of the UAV's position and velocity even in the presence of sensor noise. The integration of these advanced control algorithms allows the UAV to perform complex maneuvers, such as autonomous landing and obstacle avoidance, with high precision and reliability.

To validate the performance of the flight control system, engineers conduct simulations and field tests. Simulations help identify potential issues before actual flights, while field tests provide real-world data to refine the control algorithms. Throughout this process, the Bode plot and root locus analysis are used to analyze the frequency response and stability margins of the control system.
#############
Output:
("entity"{tuple_delimiter}"Unmanned Aerial Vehicle (UAV) Flight Control System"{tuple_delimiter}"control_system"{tuple_delimiter}"A system designed to control the flight dynamics of a UAV, ensuring stable and precise flight."){record_delimiter}
("entity"{tuple_delimiter}"Nonlinear State-Space Representation"{tuple_delimiter}"model"{tuple_delimiter}"A mathematical model that describes the UAV's flight dynamics using nonlinear equations, capturing the complex interactions between attitude, velocity, and position."){record_delimiter}
("entity"{tuple_delimiter}"Model Predictive Control (MPC) Algorithm"{tuple_delimiter}"algorithm"{tuple_delimiter}"An advanced control technique that predicts future states of the UAV and adjusts control inputs in real-time to minimize tracking errors, while considering operational constraints."){record_delimiter}
("entity"{tuple_delimiter}"Kalman Filter"{tuple_delimiter}"algorithm"{tuple_delimiter}"A statistical estimation algorithm used to provide accurate estimates of the UAV's position and velocity, even in the presence of sensor noise."){record_delimiter}
("entity"{tuple_delimiter}"Autonomous Landing"{tuple_delimiter}"application"{tuple_delimiter}"An application where the UAV performs a landing without human intervention, relying on the flight control system for precision and safety."){record_delimiter}
("entity"{tuple_delimiter}"Obstacle Avoidance"{tuple_delimiter}"application"{tuple_delimiter}"An application where the UAV detects and avoids obstacles in its flight path, ensuring safe navigation."){record_delimiter}
("entity"{tuple_delimiter}"Bode Plot"{tuple_delimiter}"concept"{tuple_delimiter}"A graphical tool used to analyze the frequency response of the control system, helping to understand its behavior at different frequencies."){record_delimiter}
("entity"{tuple_delimiter}"Root Locus Analysis"{tuple_delimiter}"concept"{tuple_delimiter}"A method used to analyze the stability margins of the control system by plotting the roots of the characteristic equation as system parameters vary."){record_delimiter}
("relationship"{tuple_delimiter}"Model Predictive Control (MPC) Algorithm"{tuple_delimiter}"Unmanned Aerial Vehicle (UAV) Flight Control System"{tuple_delimiter}"The MPC Algorithm is used within the UAV Flight Control System to predict future states and adjust control inputs in real-time, ensuring stable and precise flight."{tuple_delimiter}"real-time control, error minimization, constraint handling"{tuple_delimiter}9){record_delimiter}
("relationship"{tuple_delimiter}"Nonlinear State-Space Representation"{tuple_delimiter}"Unmanned Aerial Vehicle (UAV) Flight Control System"{tuple_delimiter}"The Nonlinear State-Space Representation models the UAV's flight dynamics, providing a basis for designing the control algorithms."{tuple_delimiter}"system modeling, dynamic behavior"{tuple_delimiter}8){record_delimiter}
("relationship"{tuple_delimiter}"Kalman Filter"{tuple_delimiter}"Unmanned Aerial Vehicle (UAV) Flight Control System"{tuple_delimiter}"The Kalman Filter is integrated into the UAV Flight Control System to estimate the UAV's position and velocity accurately, even in noisy conditions."{tuple_delimiter}"state estimation, sensor fusion"{tuple_delimiter}7){record_delimiter}
("relationship"{tuple_delimiter}"Autonomous Landing"{tuple_delimiter}"Unmanned Aerial Vehicle (UAV) Flight Control System"{tuple_delimiter}"The Autonomous Landing application relies on the UAV Flight Control System to perform a precise and safe landing without human intervention."{tuple_delimiter}"autonomous operation, precision control"{tuple_delimiter}6){record_delimiter}
("relationship"{tuple_delimiter}"Obstacle Avoidance"{tuple_delimiter}"Unmanned Aerial Vehicle (UAV) Flight Control System"{tuple_delimiter}"The Obstacle Avoidance application uses the UAV Flight Control System to detect and avoid obstacles, ensuring safe navigation."{tuple_delimiter}"safety, obstacle detection"{tuple_delimiter}5){record_delimiter}
("relationship"{tuple_delimiter}"Bode Plot"{tuple_delimiter}"Unmanned Aerial Vehicle (UAV) Flight Control System"{tuple_delimiter}"The Bode Plot is used to analyze the frequency response of the UAV Flight Control System, helping to understand its behavior at different frequencies."{tuple_delimiter}"frequency response, system analysis"{tuple_delimiter}4){record_delimiter}
("relationship"{tuple_delimiter}"Root Locus Analysis"{tuple_delimiter}"Unmanned Aerial Vehicle (UAV) Flight Control System"{tuple_delimiter}"The Root Locus Analysis is used to analyze the stability margins of the UAV Flight Control System, ensuring robust performance under varying conditions."{tuple_delimiter}"stability analysis, margin evaluation"{tuple_delimiter}3){record_delimiter}
("content_keywords"{tuple_delimiter}"UAV flight control, nonlinear state-space, MPC algorithm, Kalman filter, autonomous landing, obstacle avoidance, Bode plot, root locus analysis"){completion_delimiter}
#############################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:
"""

# 已修改
PROMPTS["summarize_entity_descriptions"] = """
You are an assistant designed to aid in teaching modern control principles. Your task is to generate a comprehensive and coherent summary of the provided data, which includes one or more entities related to control systems, along with a list of descriptions for each entity.

Your summary should:
- Combine all given descriptions into a single, detailed explanation.
- Resolve any contradictions between the descriptions to provide a unified and accurate account.
- Write the summary in third person, ensuring clarity and completeness.
- Include the entity names in the context to provide full understanding.
- Highlight key concepts, applications, and relationships relevant to control engineering.
- Use language that is accessible to students learning about control systems.

#######
-Data-
Entities: {entity_name}
Description List: {description_list}
#######
Output:
"""
# 已修改
# 指示模型或系统继续从文本中提取之前可能遗漏的实体
# PROMPTS["entiti_continue_extraction"] = """
# Several important concepts were missed in the last extraction. Please add them below using the same format to ensure a more comprehensive understanding and mastery of modern control principles:

# Format Example:
# ("entity"{tuple_delimiter}"Entity Name"{tuple_delimiter}"Entity Type"{tuple_delimiter}"Brief description of the entity"){record_delimiter}

# Please maintain a consistent format, ensuring each entity has a clear name, type, and concise description. This will help build a complete and structured knowledge base, enhancing both learning and teaching effectiveness.

# For instance, if the important concept "Lyapunov Function" was overlooked in the discussion of feedback linearization, you can add it as follows:
# ("entity"{tuple_delimiter}"Lyapunov Function"{tuple_delimiter}"concept"{tuple_delimiter}"A function used in Lyapunov stability theory to prove the stability of a system, providing a scalar measure of the system's energy or distance from equilibrium."){record_delimiter}

# Please continue adding other important entities that may have been missed.
# """
PROMPTS[
    "entiti_continue_extraction"
] = """MANY entities were missed in the last extraction.  Add them below using the same format:
"""

PROMPTS[
    "entiti_if_loop_extraction"
] = """It appears some entities may have still been missed.  Answer YES | NO if there are still entities that need to be added.
"""

PROMPTS["fail_response"] = "Sorry, I'm not able to provide an answer to that question."

PROMPTS["rag_response"] = """---Role---

You are a helpful assistant responding to questions about data in the tables provided.


---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.
If you don't know the answer, just say so. Do not make anything up.
Do not include information where the supporting evidence for it is not provided.

---Target response length and format---

{response_type}

---Data tables---

{context_data}

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.
"""

# 已修改
PROMPTS["keywords_extraction"] = """---Role---

You are an intelligent assistant designed to aid in the teaching and learning of modern control principles. Your task is to identify both high-level and low-level keywords from queries related to control systems, algorithms, models, applications, and theoretical concepts.

---Goal---

Given a query about control systems or related topics, list both high-level and low-level keywords. High-level keywords should focus on overarching concepts or themes within control theory, while low-level keywords should focus on specific entities, details, or concrete terms relevant to the field.

---Instructions---

- Output the keywords in JSON format.
- The JSON should have two keys:
  - "high_level_keywords" for overarching concepts or themes.
  - "low_level_keywords" for specific entities or details.

- Ensure that the identified keywords cover a broad spectrum of control theory, including but not limited to:
  - Control system types (e.g., PID, state-space)
  - Control algorithms (e.g., MPC, LQR)
  - Mathematical models (e.g., transfer functions, state equations)
  - Applications (e.g., robotics, aerospace, process control)
  - Theoretical foundations (e.g., stability theory, frequency response analysis)

######################
-Examples-
######################
Example 1:

Query: "How does feedback linearization improve the performance of robotic manipulators?"
################
Output:
{{
  "high_level_keywords": ["Feedback Linearization", "Performance Improvement", "Robotic Manipulators"],
  "low_level_keywords": ["Nonlinear control", "End-effector motion", "Trajectory tracking", "Backstepping control", "Lyapunov stability"]
}}
#############################
Example 2:

Query: "What are the key components of a Model Predictive Control (MPC) system?"
################
Output:
{{
  "high_level_keywords": ["Model Predictive Control", "Control System Components", "Advanced Control Techniques"],
  "low_level_keywords": ["Prediction horizon", "Optimization problem", "State estimation", "Constraint handling", "Real-time control"]
}}
#############################
Example 3:

Query: "Explain the role of the Kalman filter in state estimation for autonomous vehicles."
################
Output:
{{
  "high_level_keywords": ["Kalman Filter", "State Estimation", "Autonomous Vehicles"],
  "low_level_keywords": ["Sensor fusion", "Position estimation", "Velocity estimation", "Noise reduction", "Predictive modeling"]
}}
#############################
-Real Data-
######################
Query: {query}
######################
Output:

"""

PROMPTS["naive_rag_response"] = """---Role---

You are a helpful assistant responding to questions about documents provided.


---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.
If you don't know the answer, just say so. Do not make anything up.
Do not include information where the supporting evidence for it is not provided.

---Target response length and format---

{response_type}

---Documents---

{content_data}

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.
"""
