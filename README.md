# Chatbot-as-a-Service (ChaaS)

Este repositorio contiene el código y los datos utilizados en el trabajo de investigación:

**Chatbot-as-a-Service: una API para la generación automática de diálogos orientados a tareas**  
Autores: María Jesús Rodríguez-Sánchez, Zoraida Callejas, Ángel Ruiz-Zafra, Kawtar Benghazi  
Universidad de Granada

## Descripción

ChaaS es una API REST que permite la generación automática de diálogos adaptativos a partir de especificaciones PPTalk.  
El sistema fue validado mediante un prototipo funcional desplegado en entorno cloud y evaluado con servicios de ejemplo.

Este repositorio incluye:

- Código fuente de la API.
- Servicios de ejemplo en formato JSON (`services/`) utilizados para las pruebas experimentales.

## Contenido de `services/`

La carpeta `services/` contiene tres archivos JSON independientes, cada uno representando un servicio de ejemplo.  
Estos servicios fueron definidos mediante especificaciones PPTalk y utilizados para la evaluación experimental presentada en el artículo.

Los archivos son:

- `service1.json`
- `service2.json`
- `service3.json`

## Cómo utilizar los servicios

Los servicios pueden ser importados directamente en MongoDB en la base de datos `restaurants` colección `services` para reproducir los experimentos:

```bash
mongoimport --db chatbot --collection services --file restaurant_service_1.json
mongoimport --db chatbot --collection services --file restaurant_service_2.json
mongoimport --db chatbot --collection services --file restaurant_service_3.json
```

## Licencia

Este proyecto está publicado bajo licencia [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html).
