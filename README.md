# 🧠 perception_system_v2

[![ROS 2 Humble](https://img.shields.io/badge/ROS2-Humble-blue)](https://docs.ros.org/en/humble/)
![distro](https://img.shields.io/badge/ROS2-Jazzy-blue)

Repositorio principal del sistema de percepción 3D desarrollado para SLAM pasivo basado en visión estéreo y comparación con un sistema LiDAR. Contiene los archivos de configuración, descripciones del sistema, lanzadores y modelos necesarios para ejecutar y evaluar ambos sistemas con el paquete lidarslam_ros2.

---

## 🛠️ Instalación

Asegúrate de estar trabajando dentro de un workspace de ROS 2 (por ejemplo, `~/ros2_ws/src`):

```bash
cd ~/ros2_ws/src
git clone https://github.com/AdrianCobo/perception_system_v2.git
cd ..
colcon build --packages-select perception_system_v2
```

Una vez finalice la compilación, no olvides fuentear el entorno:
```bash
source install/setup.bash
```
---

## 🗂️ Estructura relevante del repositorio

```bash
perception_system_v2/
├── config                             # Archivos de configuración para lidarslam_ros2
│
├── description/                       # Archivos .xacro del sistema completo
│
├── launch/
│   ├── spawn_systems.launch.py        # Lanza el sistema y publica los TFs
│   ├── lidarslam*.launch.py           # Lanza lidarslam_ros2 con la configuración deseada
│
├── meshes/
│   ├── *.dae                          # Modelos 3D del soporte
