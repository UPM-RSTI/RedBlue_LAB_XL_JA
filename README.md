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
Cabe destacar que en este repositorio Logstash envía a la dirección IP de la máquina en la que está ejecutándose Elasticsearch. Para ello, se deberá cambiar el archivo .yml de Elasticsearch.
### KIBANA
```
sudo apt install kibana
sudo systemctl enable kibana
sudo systemctl start kibana
```
### VIRTUAL ENVIRONMENT
Se van a crear 2 entornos, uno llamado red-team para la parte CALDERA y otro llamado blue-team para la ejecución de CASCADE.
```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt install virtualenvwrapper
```
Después de esto, es necesario agregar varias línear al final del archivo ~/.bashrc:
```
export WORKON_HOME=/opt/virtualenvs
export VIRTUALENVWRAPPER_HOOK_DIR=$WORKON_HOME/hooks
```
Se procede con la creación de los entornos virtuales:
```
mkvirtualenv red-team
mkvirtualenv blue-team
```
Para trabajar con ese entorno:
```
workon nombre_entorno
```
Además, dentro del entorno blue-team se va a necesitar la versión de python 2.7.13, para ello:
```
workon blue-team
sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
curl https://pyenv.run | bash
```
Después de esto hay que añadir los siguientes comandos al fichero ~/.bashrc:
```
# pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```
Finalizando la instalación de pyenv:
```
exec $SHELL
pyenv --version
pyenv install 2.7.13
pyenv versions
pyenv global 2.7.13
```
### CALDERA
La instalación de CALDERA se puede encontrar en su repositorio: https://github.com/mitre/caldera 
### CASCADE
La instalación de CASCADE también se encuentra en su repositorio: https://github.com/mitre/cascade-server
## Windows10-atacada
### Sysmon
1.	Descargar el ZIP de la página oficial de sysinternals: https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon 
2.	Extraer el ZIP en una ubicación segura
3.	Se abre una powershell con permisos de administración
4.	Nos ponemos en el directorio donde está instalado sysmon
```
5.	sysmon.exe -i accepteula
6.	sysmon.exe -s
```
### Winglogbeat
1.	Descargar el ZIP de la página oficial de Elastic: https://www.elastic.co/downloads/beats/winlogbeat 
2.	Extraer el ZIP en una ubicación segura
3.	Descargamos el archivo winglogbeat.yml del repositorio
4.	Navegamos hasta el directorio donde se encuentra winlogbeat
```
5.	.\winlogbeat.exe -e -c winlogbeat.yml
```
### Logstash
1.	Navegar hasta la página: https://www.elastic.co/downloads/logstash 
2.	Descargar el ZIP
3.	Navegamos hacia la carpeta donde se encuentra el ZIP instalado
4.	Debemos configurar el archivo .conf, se usa el archivo logstash.conf de este repositorio
```
5.	.bin/logstash -f /sysmon.conf
```
## Linux-atacada
### SysmonForLinux
```
wget -q https://packages.microsoft.com/config/ubuntu/$(lsb_release   -rs)/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install sysmonforlinux
```
### Logstash
```
sudo apt install logstash
```
Para ejecutar este agente es necesario tener un archivo de configuración para enviar los eventos en Elasticsearch, en nuestro caso usamos el archivo logstash.conf de este 
repositorio
```
sudo /usr/share/logstash/bin/logstash --path.settings /etc/logstash -f /etc/logstash/conf.d/logstash.conf
```
