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
git clone -b calib https://github.com/AdrianCobo/computer_vision.git
git clone -b multicam https://github.com/AdrianCobo/oak_d_camera.git
cd ..
colcon build
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
## Resultado de usar el sistema de percepción con lidarslam_ros2 (en rojo nuestro sistema y en escala de colores el del LiDAR)
[![Resultado del Experimento](https://moresales.ca/wp-content/uploads/2022/06/Click-Me-2.png)](https://urjc-my.sharepoint.com/:v:/r/personal/josemiguel_guerrero_urjc_es/Documents/Rosbags_Adrian/tfm_data/lidar_vs_camara_lab.mp4?csf=1&web=1&e=CH88Wh&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)


## Componentes empleados:
Procesador:
- [Jetson AGX Xavier](https://www.nvidia.com/es-la/autonomous-machines/embedded-systems/jetson-agx-xavier/)
- [Intel® NUC](https://www.pccomponentes.com/msi-cubi-5-12m-210bes-intel-core-i7-1255u?utm_campaign=pedido-confirmado&utm_source=connectif&utm_medium=email&utm_content=MSI+Cubi+5+12M-210BES+Intel+Core+i7-1255U) (Recomendado)  

Sensores:
- [OAK-D-Lite](https://shop.luxonis.com/products/oak-d-lite-1?variant=42583102456031)
- [Robosense Helios 32-beam](https://www.robosense.ai/en/rslidar/RS-Helios)

Batería portatil:
- [Krisdonia 50000mah Power Pack](https://www.amazon.es/Krisdonia-50000mah-Bater%C3%ADa-Cargador-Port%C3%A1til/dp/B077TR3H2R)

Chassis:
- [Modelo 3D](https://github.com/AdrianCobo/perception_system_v2)
  <div align="center">
  <img width=500px src="https://github.com/user-attachments/assets/0f978722-dc84-49ed-8cf5-4613f4afd448" alt="explode"></a>
  </div>

Diagrama de conexiones:
  <div align="center">
  <img width=500px src="https://github.com/user-attachments/assets/3889d39c-d107-4275-be20-a40275c22097" alt="explode"></a>
  </div>

  
## Rosbags y memoria del TFM
Puedes encontrar la memoria del TFM de este proyecto y los rosbags grabados durante los experimentos [aquí](https://urjc-my.sharepoint.com/personal/josemiguel_guerrero_urjc_es/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjosemiguel%5Fguerrero%5Furjc%5Fes%2FDocuments%2FRosbags%5FAdrian&ga=1)
