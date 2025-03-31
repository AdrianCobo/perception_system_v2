import os

import launch
import launch_ros.actions

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    main_param_dir_cam = launch.substitutions.LaunchConfiguration(
        'main_param_dir_cam',
        default=os.path.join(
            get_package_share_directory('perception_system_v2'),
            'config',
            'lidarslam_cam.yaml'))

    rviz_param_dir = launch.substitutions.LaunchConfiguration(
        'rviz_param_dir',
        default=os.path.join(
            get_package_share_directory('perception_system_v2'),
            'rviz',
            'mapping.rviz'))

    mapping_cam = launch_ros.actions.Node(
        package='scanmatcher',
        executable='scanmatcher_node',
        parameters=[main_param_dir_cam],
        remappings=[('/input_cloud', '/computer_vision/pcl_sync'),
                    ('/current_pose', '/current_pose_cam'),
                    ('/map', '/map_cam'),
                    ('/path', '/path_cam'),
                    ('/map_array', '/map_array_cam')],
        output='screen'
        )

    graphbasedslam_cam = launch_ros.actions.Node(
        package='graph_based_slam',
        executable='graph_based_slam_node',
        parameters=[main_param_dir_cam],
        remappings=[('/map_array', '/map_array_cam'),
                    ('/modified_path', '/modified_path_cam'),
                    ('/modified_map', '/modified_map_cam')],
        output='screen'
        )


    main_param_dir_lid = launch.substitutions.LaunchConfiguration(
        'main_param_dir_lid',
        default=os.path.join(
            get_package_share_directory('perception_system_v2'),
            'config',
            'lidarslam_lid.yaml'))

    mapping_lid = launch_ros.actions.Node(
        package='scanmatcher',
        executable='scanmatcher_node',
        parameters=[main_param_dir_lid],
        remappings=[('/input_cloud', '/rslidar_points'),
                    ('/current_pose', '/current_pose_lid'),
                    ('/map', '/map_lid'),
                    ('/path', '/path_lid'),
                    ('/map_array', '/map_array_lid')],
        output='screen'
        )

    graphbasedslam_lid = launch_ros.actions.Node(
        package='graph_based_slam',
        executable='graph_based_slam_node',
        parameters=[main_param_dir_lid],
        remappings=[('/map_array', '/map_array_lid'),
                    ('/modified_path', '/modified_path_lid'),
                    ('/modified_map', '/modified_map_lid'),
                    ('/map_save', '/map_save_lid')],
        output='screen'
        )

    rviz = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', rviz_param_dir]
        )


    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
            'main_param_dir_cam',
            default_value=main_param_dir_cam,
            description='Full path to main parameter file to load'),
        launch.actions.DeclareLaunchArgument(
            'main_param_dir_lid',
            default_value=main_param_dir_lid,
            description='Full path to main parameter file to load'),
        mapping_cam,
        graphbasedslam_cam,
        mapping_lid,
        graphbasedslam_lid,
        rviz
            ])
