from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        # Declare the launch argument for the robot description file
        DeclareLaunchArgument(
            name='use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'
        ),
        
        # Declare the launch argument for the robot description file
        DeclareLaunchArgument(
            name='robot_description_file',
            default_value='my_robot.urdf.xacro',
            description='URDF/Xacro file with the robot description'
        ),
        
        # Node to publish the robot state
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time'),
                'robot_description': Command([
                    'xacro ',
                    LaunchConfiguration('robot_description_file')
                ])
            }]
        )
    ])

if __name__ == '__main__':
    generate_launch_description()