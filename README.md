sistema de manejo de informes en gabinete

# Desarrollo:

## Crear entorno:

´´´

virtualenv venv -p python3

venv/Scripts/activate.bat

_para usar autenticacion ldap_

pip install python_ldap-3.2.0-cp37-cp37m-win32.whl

pip install -r requirements.txt


´´´



## Generar instalador

Usar installer.bat

## Copiar o actualizar en servidor

Usar deploy.bat
