# Chatbot-as-a-Service (ChaaS)

Este repositorio contiene el código y los datos utilizados en el trabajo de investigación:

**Chatbot-as-a-Service: una API para la generación automática de diálogos orientados a tareas**  
Autores: María Jesús Rodríguez-Sánchez, Zoraida Callejas, Ángel Ruiz-Zafra, Kawtar Benghazi  
Universidad de Granada

> (Cuando se publique el artículo, añade aquí el enlace o DOI)

## Descripción

ChaaS es una API REST que permite la generación automática de diálogos adaptativos a partir de especificaciones PPTalk.  
El sistema fue validado mediante un prototipo funcional desplegado en entorno cloud y evaluado con servicios de ejemplo.

Este repositorio incluye:

- Código fuente de la API.
- Servicios de ejemplo en formato JSON (`example_services/`) utilizados para las pruebas experimentales.

## Contenido de `example_services/`

La carpeta `example_services/` contiene tres archivos JSON independientes, cada uno representando un servicio de ejemplo.  
Estos servicios fueron definidos mediante especificaciones PPTalk y utilizados para la evaluación experimental presentada en el artículo.

Los archivos son:

- `restaurant_service_1.json`
- `restaurant_service_2.json`
- `restaurant_service_3.json`

## Cómo utilizar los servicios

Los servicios pueden ser importados directamente en MongoDB para reproducir los experimentos:

```bash
mongoimport --db chatbot --collection services --file restaurant_service_1.json
mongoimport --db chatbot --collection services --file restaurant_service_2.json
mongoimport --db chatbot --collection services --file restaurant_service_3.json
```

**Nota:** adapta el nombre de la base de datos y la colección si es necesario.

## Licencia

Este proyecto está publicado bajo licencia [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.html).
