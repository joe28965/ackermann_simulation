################################################################################
# Set minimum required version of cmake, project name and compile options
################################################################################
cmake_minimum_required(VERSION 3.5)
project(ackermann_simulation)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

################################################################################
# Find ament packages and libraries for ament and system dependencies
################################################################################
find_package(ament_cmake REQUIRED)
find_package(urdf REQUIRED)

################################################################################
# Install
################################################################################
install(
  DIRECTORY urdf launch models
  DESTINATION share/${PROJECT_NAME}
)

ament_environment_hooks("${CMAKE_CURRENT_SOURCE_DIR}/env-hooks/ackermann_simulation.dsv.in")

################################################################################
# Macro for ament package
################################################################################
ament_package()
