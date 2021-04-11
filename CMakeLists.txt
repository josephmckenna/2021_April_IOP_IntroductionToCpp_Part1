cmake_minimum_required(VERSION 3.10)
set (CMAKE_CXX_STANDARD 11)

# set the project name
project(PenningTrapSimulation)

# Set build type and optimisations (assume unix like platform)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS "-Wall -Wextra")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")


add_executable(simulation.exe main.cpp)