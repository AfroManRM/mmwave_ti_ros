from launch import LaunchDescription
from launch.actions import TimerAction ,DeclareLaunchArgument, GroupAction, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource, AnyLaunchDescriptionSource
from launch_ros.actions import PushRosNamespace
from ament_index_python.packages import get_package_share_directory
from pathlib import Path

def generate_launch_description():

    use_sim_time = LaunchConfiguration("use_sim_time")

    # Pfade zu den zu startenden Launchfiles
    Radar_M = Path(get_package_share_directory("ti_mmwave_rospkg")) / "launch" / "1843_Mid.launch.py"
    Radar_L = Path(get_package_share_directory("ti_mmwave_rospkg")) / "launch" / "1843_Left.launch.py"
    Radar_R = Path(get_package_share_directory("ti_mmwave_rospkg")) / "launch" / "1843_Right.launch.py" 



    # Optional: jedes Paket in einen Namespace packen
    group_a = GroupAction([
        #PushRosNamespace("ns_Radar_M"),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(str(Radar_M)),
                                 launch_arguments="")
    ])

    group_b = GroupAction([
        #PushRosNamespace("ns_Radar_L"),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(str(Radar_L)),
                                 launch_arguments="")
    ])

    group_c = GroupAction([
        #PushRosNamespace("ns_Radar_R"),
        IncludeLaunchDescription(AnyLaunchDescriptionSource(str(Radar_R)),
                                 launch_arguments="")
    ])

    return LaunchDescription([
        TimerAction(period=0.0, actions=[group_a]),
        TimerAction(period=15.0, actions=[group_b]),
        TimerAction(period=30.0, actions=[group_c]),
    ])
