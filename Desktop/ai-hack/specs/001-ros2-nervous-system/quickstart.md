# Quickstart Guide: Module 1 - The Robotic Nervous System (ROS 2)

This quickstart guide provides a high-level overview of setting up your development environment and getting started with the examples in Module 1.

## 1. System Requirements

*   **Operating System**: Ubuntu 22.04 LTS (Jammy Jellyfish) or later (recommended).
*   **ROS 2 Distribution**: Humble Hawksbill (recommended) or Iron Irwini.
*   **Python**: Python 3.8+ (comes pre-installed with Ubuntu 22.04).

## 2. ROS 2 Installation

Follow the official ROS 2 documentation for your chosen distribution.

*   **For Ubuntu Desktop**:
    ```bash
    # Set locale
    sudo apt update && sudo apt install locales
    sudo locale-gen en_US en_US.UTF-8
    sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
    export LANG=en_US.UTF-8

    # Setup sources
    sudo apt install software-properties-common -y
    sudo add-apt-repository universe -y
    sudo apt update && sudo apt install curl -y
    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

    # Install ROS 2 Humble Desktop
    sudo apt update
    sudo apt upgrade -y
    sudo apt install ros-humble-desktop -y

    # Environment setup
    echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    ```
    *(Adjust for Iron Irwini by replacing `humble` with `iron` in commands.)*

## 3. Python Environment Setup

It is recommended to use a virtual environment for Python development.

```bash
# Install pip and virtualenv if not already installed
sudo apt update
sudo apt install python3-pip python3-venv -y

# Create and activate a virtual environment
mkdir -p ~/ros2_ws/src # Create a workspace if you don't have one
cd ~/ros2_ws
python3 -m venv .venv
source .venv/bin/activate

# Install rclpy and other necessary Python packages
pip install -U pip
pip install rclpy # This will be specific based on ROS 2 version
pip install colcon-common-extensions # For building ROS 2 packages
```

## 4. Building Your Workspace

After placing your ROS 2 Python packages (containing AI agents, etc.) in the `~/ros2_ws/src` directory:

```bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

## 5. Running Examples

Each chapter will provide specific instructions for running its examples. Generally, it will involve:

```bash
# In one terminal, run a ROS 2 node
ros2 run <package_name> <node_executable>

# In another terminal, run your Python AI agent
ros2 run <python_package_name> <python_script_name>

# To visualize URDF models in Rviz
ros2 launch urdf_tutorial display.launch.py model:=src/<your_robot_package>/urdf/<your_robot>.urdf.xacro
```

## 6. Simulation with Gazebo

Instructions for launching Gazebo and loading robot models will be provided in relevant chapters.

```bash
ros2 launch gazebo_ros gazebo.launch.py
ros2 launch <your_robot_package> gazebo.launch.py
```
