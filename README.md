# 🚗 KIA Tower Mobile (ATM) - ROS 2 Gazebo Simulation

Welcome to the official simulation hub for the **Aurora Tower Mobile (ATM)**! 

This repository contains a from-scratch ROS 2 package (`ATM_description`) that brings the ATM robot to life in Gazebo. We’ve moved past boring cylinders and boxes—this model features **high-fidelity 3D CAD meshes**, perfectly balanced differential drive physics, and custom-tuned solver constraints so it drives smooth as butter. No gridlock here! 🧈

Whether you are here to test autonomous navigation algorithms or just want to drive a cool virtual robot around, you are in the right place.

---

## 🛠️ Prerequisites
Before we get the wheels spinning, make sure your machine (or cloud server!) has the following installed:
* **ROS 2** (Built and tested on Humble)
* **Gazebo** (Classic)
* The `teleop_twist_keyboard` package (for the fun part)

---

## 🚀 Quick Start Guide

### 1. Clone & Build
Pop open your terminal, navigate to your ROS 2 workspace, and pull down the code:

```bash
cd ~/ros2_ws/src
git clone [https://github.com/Ibrahim-KIA/KIA_Tower_Mobile-ATM.git](https://github.com/Ibrahim-KIA/KIA_Tower_Mobile-ATM.git) ATM_description
Now, head back to the root of your workspace and build the package:

Bash
cd ~/ros2_ws
colcon build --packages-select ATM_description
source install/setup.bash
2. Spawn the Robot
Let's drop the ATM into the Gazebo matrix. Run the launch file:

Bash
ros2 launch ATM_description gazebo.launch.py
Wait a few seconds for Gazebo to spin up. You should see the fully rendered ATM robot drop perfectly onto the grid!

🎮 The Fun Part: Let's Drive!
What is a robot if you can't drive it? The ATM is equipped with a diff_drive Gazebo plugin, meaning it is ready to receive your commands.

Leave Gazebo running, open a brand new terminal window, and run the teleop node:

Bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
⌨️ Controls
Make sure your terminal window is selected (clicked on), and use these keys to drive the robot like a classic arcade game:

i : Move Forward

k : STOP (Hit the brakes!)

, : Move Backward

j : Spin Left

l : Spin Right

Pro-tip: You can press q / z to increase or decrease your max speed if you want to see how fast the ATM can really go before it drifts!

🧠 Behind the Scenes (For the Nerds)
If you peek under the hood at the atm_gazebo.xacro file, you'll see some serious physics engineering:

Collision Spheres: We wrapped the complex wheel STLs in simple invisible spheres to keep the simulation running lightning-fast without melting your CPU.

Balanced Dynamics: Friction (mu1/mu2) and contact stiffness (kp) are mathematically balanced to prevent Gazebo's ODE solver from locking up (goodbye, numerical gridlock).

Frictionless Casters: The front and rear casters are tuned to glide perfectly so they don't drag against the differential drive motors.

Happy simulating! 🤖✨
