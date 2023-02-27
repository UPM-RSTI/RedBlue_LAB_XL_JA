#!/usr/bin/python

import requests
import sys
from subprocess import call
import uuid
import subprocess
import os

headers = {
            "KEY": "ADMIN123",
            "accept": "application/json",
            "Content-Type": "application/json" 
}
if str(sys.argv[1]) == "server":
  #os.chdir('caldera')
  subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', 'python3 server.py --insecure; exec $SHELL'])

#Ejecute 'python3 red-team.py server' para iniciar el servidor
#Ejecute 'python3 red-team.py agente crear' para crear un agente
#Ejecute 'python3 red-team.py agente editar' para editar un agente
#Ejecute 'python3 red-team.py agente eliminar' para eliminar un agente
#Ejecute 'python3 red-team.py operacion crear' para crear una operacion con su respectivo adversario
#Ejecute 'python3 red-team.py operacion editar' para editar una operacion
#Ejecute 'python3 red-team.py operacion eliminar' para eliminar una operacion
# =======================================================================================================================================
#   AGENTE
# =======================================================================================================================================
elif str(sys.argv[1]) == "agente":
    #json del agente
    data = {
      "privilege": "string",
      "server": "string",
      "host_ip_addrs": [
      ],
      "sleep_min": 30,
      "executors": [
        "string"
      ],
      "exe_name": "splunkd",
      "platform": "linux",
      "proxy_chain": [
        [
          "string"
        ]
      ],
      "ppid": 0,
      "deadman_enabled": True,
      "group": "red",
      "upstream_dest": "string",
      "trusted": True,
      "pending_contact": "HTTP",
      "watchdog": 0,
      "host": "red-team",
      "paw": "string",
      "architecture": "amd64",
      "pid": 0,
      "username": "red-team",
      "proxy_receivers": {
      },
      "origin_link_id": "",
      "location": "/home",
      "contact": "HTTP",
      "sleep_max": 60,
      "available_contacts": [
        "HTTP"
      ]
    }

    if str(sys.argv[2]) == "crear":
      #datos proporcionados por el usuario

      url = input("Escriba la IP del dispositivo a ejecutar: ")
      data["host_ip_addrs"] = [str(url)]
      data["upstream_dest"] = "http://"+str(url)+":8888"
      data["paw"] = input("Escriba el paw (identificador único del agente): ")
      data["ppid"] = int(input("Escriba el ppid(número entero): "))
      data["pid"] = data["ppid"]
      data["server"] = "http://"+url+":8888"       

      data["platform"] = input("Escriba la platforma (windows o linux): ")
      data["contact"] = input("Escriba el contact (HTTP para Sandcat, TCP para Manx o HTML para Ragdoll): ")
      data["available_contacts"] = [data["contact"]]
      data["pending_contact"] = data["contact"]
     # data["username"] = input("Enter username: ")
     # data["deadman_enabled"] = bool(input("Enter deadman_enabled (True o False): ")) 
      data["exe_name"] = input("Escriba el exe_name: ")
      data["privilege"] = input("Escriba los privilegios (User o Elevated): ")
    # data["location"] = input("Enter location: ")
    #  data["executors"] = [input("Enter executors: ")]
    #  data["host"] = input("Enter host: ")      
      print("Para editar el agente ejecute: 'python3 red-team.py editar'")

      #peticion POST a la 
      try:
        response = requests.post("http://"+url+":8888/api/v2/agents", headers = headers, json = data)
        response.raise_for_status()
      except requests.exceptions.HTTPError as e:
        print("Error: " + str(e))
        print(response.text)
      else:
        print('Agente creado correctamente.')

  
    elif str(sys.argv[2]) == "editar":
      url = input("Escriba la IP del dispositivo a ejecutar: ")
      response = requests.get("http://"+url+":8888/api/v2/agents", headers = headers)
      data = response.json()

      print("Agentes disponibles a editar:")

      for i, agent in enumerate(data):
          print(f"{i + 1}->{agent['paw']}")
      
      var = input("Escriba el paw del agente que desea editar: ") 
      data = {
          "watchdog": 0,
          "sleep_min": 30,
          "sleep_max": 60,
          "group": "string",
          "pending_contact": "string",
          "trusted": True
      }
      data["watchdog"] = input("Escriba el watchdog: ")
      data["sleep_min"] = input("Escriba el sleep_min: ")
      data["sleep_max"] = input("Escriba el sleep_max: ")
      data["group"] = input("Escriba el group: ")
      data["pending_contact"] = input("Escriba el pending_contact: ")
      data["trusted"] = input("Escriba el trusted (True o False): ")

      try:
        response = requests.patch("http://"+url+":8888/api/v2/agents/"+var, headers = headers, json = data)
        response.raise_for_status()
      except requests.exceptions.HTTPError as e:
        print("Error: " + str(e))
        print(response.text)
      else:
        print('Agente editado correctamente.')

    elif str(sys.argv[2]) == "eliminar":
      url = input("Escriba la IP del dispositivo a ejecutar: ")
      response = requests.get("http://"+url+":8888/api/v2/agents", headers = headers)
      data = response.json()

      print("Agentes disponibles a editar:")

      for i, agent in enumerate(data):
          print(f"{i + 1}->{agent['paw']}")
      
      var = input("Escriba el paw del agente que desea eliminar: ") 
      
      try:
         response = requests.delete("http://"+url+":8888/api/v2/agents/"+var, headers = headers)
         response.raise_for_status()
      except requests.exceptions.HTTPError as e:
         print("Error: " + str(e))
      else:
         print('Agente eliminado correctamente')
      
    else: 
      print("Comando incorrecto: python3 red-team.py agente"+str(sys.argv[2]))
      print("Para obtener la información para crear un agente: 'python3 red-team.py agente info'")

# =======================================================================================================================================
#  OPERACION
# =======================================================================================================================================  
elif str(sys.argv[1]) == "operacion":
  
  
  if str(sys.argv[2]) == "crear":
    
    url = input("Escriba la IP del dispositivo a ejecutar: ")
    
    response = requests.get("http://"+url+":8888/api/v2/adversaries", headers = headers)
    data = response.json()

    print("Adversarios disponibles a ejecutar:")

    for i, adver in enumerate(data):
        print(f"{i + 1}->{adver['name']}")

    num_adv = int(input("Ingrese el número del adversario que desea crear: "))
    
    

    adversario = data[num_adv - 1]
    
    try:
        response = requests.get("http://"+url+":8888/api/v2/adversaries", headers = headers, json = adversario)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error: " + str(e))
    else:
        print(f"Adversario {num_adv} obtenido correctamente")

    data = 	{
  "planner": {
    "description": "string",
    "stopping_conditions": [
    ],
    "params": {},
    "id": "string",
    "plugin": None,
    "module": "string",
    "name": "string",
    "allow_repeatable_abilities": True,
    "ignore_enforcement_modules": [
      "string"
    ]
  },
  "source": {
    "adjustments": [
    ],
    "plugin": None,
    "facts": [
      {
        "score": 0,
        "source": "string",
        "limit_count": 0,
        "collected_by": [
          "string"
        ],
        "technique_id": "string",
        "value": "string",
        "origin_type": "string",
        "relationships": [
          "string"
        ],
        "trait": "string",
        "links": [
          "string"
        ]
      }
    ],
    "name": "string",
    "relationships": [
      {
        "score": 0,
        "edge": "string",
        "source": {
          "score": 0,
          "source": "string",
          "limit_count": 0,
          "collected_by": [
            "string"
          ],
          "technique_id": "string",
          "value": "string",
          "origin_type": "string",
          "relationships": [
            "string"
          ],
          "trait": "string",
          "links": [
            "string"
          ]
        },
        "target": {
          "score": 0,
          "source": "string",
          "limit_count": 0,
          "collected_by": [
            "string"
          ],
          "technique_id": "string",
          "value": "string",
          "origin_type": "string",
          "relationships": [
            "string"
          ],
          "trait": "string",
          "links": [
            "string"
          ]
        },
        "origin": "string"
      }
    ],
    "rules": [
    ],
    "id": "string"
  },
  "obfuscator": "plain-text",
  "visibility": 0,
  "objective": {
    "description": "string",
    "goals": [
      {
        "count": 0,
        "target": "string",
        "operator": "string",
        "value": "string"
      }
    ],
    "name": "string",
    "id": "string"
  },
  "adversary": {
    "description": "string",
    "plugin": None,
    "tags": [
      "string"
    ],
    "atomic_ordering": [
      "string"
    ],
    "name": "string",
    "adversary_id": "string",
    "objective": "string"
  },
  "jitter": "2/8",
  "name": "string",
  "group": "",
  "autonomous": 1,
  "auto_close": False,
  "id": "string",
  "state": "running",
  "use_learning_parsers": True
}

    
    data["name"] = input("Escriba el nombre de la operación: ")
    

    data["adversary"]["adversary_id"] = adversario['adversary_id']
    data["adversary"]["description"] = adversario["description"]
    data["adversary"]["name"] = adversario["name"]
    data["adversary"]["atomic_ordering"] = adversario["atomic_ordering"]
    data["id"] = str(uuid.uuid4())
    print(data)

    try:
          response = requests.post("http://"+url+":8888/api/v2/operations", headers = headers, json = data)
          response.raise_for_status()
    except requests.exceptions.HTTPError as e:
          print("Error: " + str(e))
    else:
          print(f"Operacion creada correctamente")

  elif str(sys.argv[2]) == "editar":
     
    url = input("Escriba la IP del dispositivo a ejecutar: ")
    response = requests.get("http://"+url+":8888/api/v2/operations", headers = headers)
    data = response.json()

    print("Operaciones(Nombre:ID):")

    for i, oper in enumerate(data):
        print(f"{i + 1}->{oper['name']}:{oper['id']}")

    var = input("Escriba el ID de la operación a editar:")

    data = {
    "obfuscator": "base64",
    "autonomous": 1,
    "state": "running"
    }

    data["obfuscator"] = input("Escriba el obfuscator: (base64, base64jumble, base64NoPadding, caesar cipher, plain-text, steganography): ")
    data["autonomous"] = input("Escriba un 0 para modo manual o 1 para modo autónomo: ")
    data["state"] = input("Escriba running, run_one_link, paused, out_of_time, finished o cleanup para cambiar el estado de la operacion: ")

    try:
          response = requests.patch("http://"+url+":8888/api/v2/operations/"+var, headers = headers, json = data)
          response.raise_for_status()
    except requests.exceptions.HTTPError as e:
          print("Error: " + str(e))
    else:
          print(f"Operacion editada correctamente")

  elif str(sys.argv[2]) == "eliminar":
    url = input("Escriba la IP del dispositivo a ejecutar: ")
    response = requests.get("http://"+url+":8888/api/v2/operations", headers = headers)
    data = response.json()

    print("Operaciones(Nombre:ID):")

    for i, oper in enumerate(data):
        print(f"{i + 1}->{oper['name']}:{oper['id']}")

    var = input("Escriba el ID de la operación a eliminar:")

    try:
          response = requests.delete("http://"+url+":8888/api/v2/operations/"+var, headers = headers, json = data)
          response.raise_for_status()
    except requests.exceptions.HTTPError as e:
          print("Error: " + str(e))
    else:
          print(f"Operacion eliminada correctamente")

elif str(sys.argv[1]) == "comandos":
    print("Ejecute 'python3 red-team.py agente crear' para crear un agente")
    print("Ejecute 'python3 red-team.py agente editar' para editar un agente")
    print("Ejecute 'python3 red-team.py agente eliminar' para eliminar un agente")
    print("Ejecute 'python3 red-team.py operacion crear' para crear una operacion con su respectivo adversario")
    print("Ejecute 'python3 red-team.py operacion editar' para editar una operacion")
    print("Ejecute 'python3 red-team.py operacion eliminar' para eliminar una operacion")

else:
    print("Comando incorrecto\n Ejecute 'python3 red-team.py comandos' para más información sobre los diferentes comandos")

    







