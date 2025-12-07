# Data Model: Module 1 - The Robotic Nervous System (ROS 2)

## Entities and Conceptual Models

This section outlines the key conceptual entities relevant to the content of Module 1. As this module focuses on educational content about robotics middleware and modeling, the "data model" here refers to the structure and relationships of concepts presented to the learner, rather than a database schema for an application.

### 1. ROS 2 Node

*   **Description**: An executable process that performs computation (e.g., sensor data processing, motor control, AI algorithm execution) within the ROS 2 graph. It's the fundamental unit of computation in ROS 2.
*   **Key Attributes (Conceptual)**:
    *   `name`: Unique identifier for the node within the ROS 2 graph.
    *   `purpose`: High-level function of the node (e.g., "lidar_driver", "path_planner", "ai_decision_maker").
    *   `language`: Programming language used for implementation (e.g., Python).
    *   `communication_interfaces`: List of topics, services, actions it uses.
*   **Relationships**:
    *   Publishes to/Subscribes from ROS 2 Topics.
    *   Provides/Uses ROS 2 Services.

### 2. ROS 2 Topic

*   **Description**: A named bus over which nodes exchange messages in a publish-subscribe communication model. It's used for streaming data (e.g., sensor readings, joint states).
*   **Key Attributes (Conceptual)**:
    *   `name`: Unique identifier for the topic (e.g., "/scan", "/cmd_vel").
    *   `message_type`: Data structure of the messages exchanged (e.g., `sensor_msgs/msg/LaserScan`, `geometry_msgs/msg/Twist`).
    *   `qos_profile`: Quality of Service settings (e.g., reliability, durability, history).
*   **Relationships**:
    *   Published by one or more ROS 2 Nodes.
    *   Subscribed by one or more ROS 2 Nodes.

### 3. ROS 2 Service

*   **Description**: A request/reply communication mechanism that allows nodes to send a request to a service server and receive a single response. Used for synchronous, one-shot interactions (e.g., "get_map", "set_pose").
*   **Key Attributes (Conceptual)**:
    *   `name`: Unique identifier for the service (e.g., "/navigate", "/calculate_ik").
    *   `request_type`: Data structure for the request message.
    *   `response_type`: Data structure for the response message.
*   **Relationships**:
    *   Provided by a single ROS 2 Node (server).
    *   Used by one or more ROS 2 Nodes (clients).

### 4. Python AI Agent

*   **Description**: A conceptual representation of an artificial intelligence component implemented in Python, interacting with the ROS 2 ecosystem. This entity encapsulates the AI logic (e.g., path planning, object recognition, natural language understanding).
*   **Key Attributes (Conceptual)**:
    *   `algorithm`: The AI algorithm or model employed (e.g., "reinforcement_learner", "neural_network_vision").
    *   `ros2_interface`: How it connects to ROS 2 (e.g., `rclpy`).
    *   `data_inputs`: ROS 2 topics/services it consumes.
    *   `command_outputs`: ROS 2 topics/services it produces.
*   **Relationships**:
    *   Implements logic for a ROS 2 Node.
    *   Communicates via ROS 2 Topics and Services.

### 5. URDF/Xacro Robot Model

*   **Description**: A hierarchical description of a robot's physical and kinematic properties, including its links (rigid bodies) and joints (connections between links). Xacro extends URDF for modularity and parameterization.
*   **Key Attributes (Conceptual)**:
    *   `links`: Rigid bodies of the robot (e.g., "base_link", "upper_arm", "gripper").
        *   `geometry`: Shape and size.
        *   `mass`: Mass property.
        *   `inertia`: Inertia tensor.
        *   `visual`: Visual representation (e.g., CAD model).
        *   `collision`: Collision properties.
    *   `joints`: Connections between links (e.g., "revolute", "prismatic", "fixed").
        *   `type`: Type of joint.
        *   `parent_link`: The link it's attached to.
        *   `child_link`: The link it moves.
        *   `axis`: Axis of rotation/translation.
        *   `limits`: Joint limits (position, velocity, effort).
    *   `sensors`: (Optional) Description of sensors attached to the robot.
*   **Relationships**:
    *   Defines the physical structure for a Humanoid Robot.
    *   Used by ROS 2 for inverse kinematics, simulation, and visualization.
