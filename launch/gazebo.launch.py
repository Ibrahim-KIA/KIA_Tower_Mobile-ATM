import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # Get package path
    pkg_path = os.path.join(get_package_share_directory('ATM_description'))
    xacro_file = os.path.join(pkg_path, 'urdf', 'atm.urdf.xacro')
    
    # Process the Xacro file
    robot_description_config = xacro.process_file(xacro_file)
    robot_description = {'robot_description': robot_description_config.toxml()}

    # Node to publish robot state
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )

    # Launch Gazebo empty world
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
    )

    # Spawn the robot in Gazebo
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'atm_robot',
                                   '-z', '0.5'], # Drop it from 0.5 meters high!
                        output='screen')

    return LaunchDescription([
        node_robot_state_publisher,
        gazebo,
        spawn_entity,
    ])