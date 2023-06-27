# RedBlue_LAB_XL_JA
# Diseño y desarrollo de un laboratorio de ciberseguridad de tipo Red y Blue Team
## Introducción
 Se ha diseñado un laboratorio para la ejecución y detección de adversarios empleando CALDERA para la parte de red team y CASCADE para la parte blue. Además, se dispondrá de los pasos a seguir para la instalación de este laboratorio.
## Arquitectura
![image](https://github.com/UPM-RSTI/RedBlue_LAB_XL_JA/assets/117222099/601191ef-a32a-4a49-9d42-8bfa7f066aa2)
## Instalación
## Red-Blue
### MongoDB
```
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add - apt-key list
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update
sudo apt install mongodb-org
sudo systemctl start mongod.service
```
Para observar que se ha instalado correctamente:
```
sudo systemctl status mongod
```
### ELASTICSEARCH
Para instalar Elasticsearch se necesita tener instalado Java en el sistema operativo, para ello:
```
sudo apt update
sudo apt install openjdk-11-jdk
java –version
```
Después de instalar Java, se instala Elasticsearch:
```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.13.4-amd64.deb  
sudo dpkg -i elasticsearch-7.13.4-amd64.deb 
```
Cuando ya está instalado en el sistema, se inicia su servicio:
```
sudo systemctl start elasticsearch
```
Si el usuario quiere corrobar que la instalación ha sido correcta:
```
curl -X GET “http:localhost:9200/”
```
Cabe destacar que en este repositorio Logstash envía a la dirección IP de la máquina en la que está ejecutándose Elasticsearch. Para ello, se deberá cambiar el archivo .yml de Elasticsearch:
### CALDERA
La instalación de CALDERA se puede encontrar en su repositorio: https://github.com/mitre/caldera 
### CASCADE
La instalación de CASCADE también se encuentra en su repositorio: https://github.com/mitre/cascade-server 
#### 
