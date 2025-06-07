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
Instalar lidarslam_ros2:
Si estás en Ubuntu 24
```shell
sudo apt install libg2o-dev
```
y sigue la [documentación oficial](https://github.com/rsasaki0109/lidarslam_ros2)

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
```

## Uso:

### Mapear:
```shell
ros2 launch oak_d_camera multicam.launch.py
ros2 launch perception_system_v2 spawn_systems.launch.py
ros2 launch rslidar_sdk start.launch.py
ros2 launch computer_vision pcl_sync.launch.py
ros2 launch perception_system_v2 lidarslam_cam_and_lid.launch.py
ros2 bag record /computer_vision/pcl_sync /rslidar_points
```

### Reproducir rosbag para mapear:
```shell
ros2 launch oak_d_camera multicam.launch.py
ros2 launch perception_system_v2 spawn_systems.launch.py
ros2 launch perception_system_v2 lidarslam.launch.py
rviz2
ros2 bag play rosbag2_2025_03_07-12_01_20/
```

## Cambiar luego:

## Resultado de usar el sistema de percepción con lidar_slam
[![Resultado del Experimento](https://moresales.ca/wp-content/uploads/2022/06/Click-Me-2.png)](https://drive.google.com/file/d/1VGTcvLKiD8vrUgkvgi9_q75DOobXr2hW/view?usp=sharing)


## Componentes empleados:
Procesador:
- [Jetson AGX Xavier](https://www.nvidia.com/es-la/autonomous-machines/embedded-systems/jetson-agx-xavier/)
- [Intel® NUC NUC5i5RYK](https://www.intel.la/content/www/xl/es/products/sku/83254/intel-nuc-kit-nuc5i5ryk/specifications.html) (Recomendado)  

Sensores:
- [Intel realsense d435I](https://www.intelrealsense.com/depth-camera-d435i/)
- [Robosense Helios 32-beam](https://www.robosense.ai/en/rslidar/RS-Helios)

Batería portatil:
- [Krisdonia 50000mah Power Pack](https://www.amazon.es/Krisdonia-50000mah-Bater%C3%ADa-Cargador-Port%C3%A1til/dp/B077TR3H2R)

Chassis:
- [Modelo 3D](https://github.com/AdrianCobo/perception_system/tree/main/meshes)
  <div align="center">
  <img width=500px src="https://github.com/user-attachments/assets/6268514e-7398-4a32-aca1-fb947f5899ed" alt="explode"></a>
  </div>

Diagrama de conexiones:
  <div align="center">
  <img width=500px src="https://github.com/user-attachments/assets/81e16504-ab6a-4319-b346-66d632af213c" alt="explode"></a>
  </div>
  
## Rosbags y memoria del TFG
Puedes encontrar la memoria del TFG de este proyecto y los rosbags grabados durante los experimentos [aquí](https://urjc-my.sharepoint.com/personal/josemiguel_guerrero_urjc_es/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjosemiguel%5Fguerrero%5Furjc%5Fes%2FDocuments%2FRosbags%5FAdrian&ga=1)
