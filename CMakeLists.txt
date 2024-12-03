cmake_minimum_required(VERSION 3.10.2) 
project(perception_system_v2 VERSION 0.0.1 LANGUAGES CXX C)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)
add_compile_options(-g)

## is used, also find other catkin packages
if(POLICY CMP0057)
    cmake_policy(SET CMP0057 NEW)
endif()

find_package(ament_cmake REQUIRED)

install(DIRECTORY rviz DESTINATION share/${PROJECT_NAME})
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(DIRECTORY description DESTINATION share/${PROJECT_NAME})

ament_package()

