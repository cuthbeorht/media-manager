cmake_minimum_required(VERSION 3.16)
project(QtM1MacProject VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Force CMake to look into Homebrew's M1 directory for Qt
list(APPEND CMAKE_PREFIX_PATH "/opt/homebrew/opt/qt")

find_package(Qt6 REQUIRED COMPONENTS Widgets)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

add_executable(QtM1MacProject main.cpp)
target_link_libraries(QtM1MacProject PRIVATE Qt6::Widgets)
