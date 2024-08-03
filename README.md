# MyApp

# Proyecto de Aplicación con SSR en Angular

Este proyecto es una aplicación con Server-Side Rendering (SSR) desarrollada con Angular y desplegada en un servidor EC2 en AWS usando Amazon Linux y Apache.

## Descripción

La aplicación se comunica con un backend ubicado en otra instancia EC2 a través de una red privada. El backend es una API desarrollada con Flask que se conecta a una base de datos MySQL alojada en
Amazon RDS.

## Arquitectura del Proyecto

1. **Frontend**: 
   - Desarrollado con Angular y habilitado para SSR.
   - Desplegado en una instancia EC2 con Amazon Linux y servidor Apache.

2. **Backend**:
   - API desarrollada con Flask.
   - Alojada en una instancia EC2 diferente, comunicándose con el frontend mediante una red privada.

3. **Base de Datos**:
   - Base de datos MySQL alojada en Amazon RDS.

## Funcionamiento

1. La aplicación Angular envía solicitudes a la API de Flask.
2. La API de Flask se comunica con la base de datos MySQL para recuperar y enviar los datos solicitados.
3. El servidor Angular renderiza los datos y los muestra en el frontend.


## Instalación y Despliegue

1. **Frontend**:
   - Desplegar en modo produccion la aplicación Angular con SSR en una instancia EC2.
   - Configurar Apache para servir la aplicación Angular.

2. **Backend**:
   - Desplegar la API Flask en una instancia EC2 diferente.
   - Configurar la API para que se comunique con la base de datos MySQL en RDS.
   - 
## Clonación del Repositorio

Para clonar este repositorio, utiliza el siguiente comando:

```bash
git clone https://github.com/FelipeBustos22/rest-API-midu.git
