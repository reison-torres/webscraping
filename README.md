---
Materia: 'Tipología y ciclo de vida de los datos'
Actividad: 'PRA1: Web Scraping'
Autor: "Reison Arturo Torres Urina"
Fecha: "Octubre 2019"
---

******
# Introducción

El objetivo de esta actividad será la creación de un dataset a partir de los datos contenidos en una web, aplicando las tecnicas de Web Scraping.

## Contexto

Con el fin de llevar a cabo esta actividad de Web Scraping, se seleccionó el sitio web de [CORABASTOS](https://www.corabastos.com.co/aNuevo/index.php/about-joomla/nuestra-historia). Esta  es una Sociedad del orden nacional, vinculada al Ministerio de Agricultura y Desarrollo Rural. Su papel en la economía del país Colombia, es la de fijar los precios de los principales productos agroalimentario, estos precios son dirigidos al consumidor. Este listado de precios son publicados en la web [AppCoraPrecios](https://www.corabastos.com.co/sitio/historicoApp2/reportes/prueba.php)

## Descripción del conjunto de datos

__Título DataSet__: Productos y precios de comercialización, dirigidos al consumidor.

__Descripción__: Este conjunto de datos contiene el listado de productos y precios que se comercializan diariamente en los puntos de venta de las diferentes Bodegas de la corporación CORABASTOS y dichos precios están dirigido al consumidor.

## Imagen identificativa

![Productos y precios de comercialización, dirigidos al consumidor.](./img/foodprice.png)

## Contenido

La base datos de productos y precios que se comercializan a diario al consumidor, publicados por la entidad CORABASTOS, está constituido por variables numéricas y de textos. A continuación daremos una pequeña descripción, acerca de lo que representa, cada una de las variables, que se encuentra en este conjunto de datos.

1. **Grupo**: Nombre del grupo al que pertenece un producto (HORTALIZAS, FRUTAS, TUBERCULOS, PLATANOS, GRANOS Y PROCESADOS, LACTEOS, CARNICOS y HUEVOS)  . (Texto). 
2. **Nombre**: Nombre o descripción del producto. (Texto). 
3. **Presentación**: Presentaciones de venta en la que viene el producto. (Texto). 
4. **Cantidad**: Número de unidades que vienen por presentación. (Numérico).  
5. **Unidad**: Unidad de medida en la que se vende el producto. (Texto).  
6. **Cal_Extra**: Precio máximo de venta. (Numérico).  
7. **Cal_Primera**: Precio mínimo de venta. (Numérico).  
8. **Valor**: Precio de venta. (Numérico).  
9. **Fecha_publicacion**: Fecha de publicacion del precio del producto. (Fecha).  

Estos datos son publicados diariamente solo en los días hábiles de L-V.

## Agradecimientos

Los datos han sido recolectados desde la base de datos online [AppCoraPrecios](https://www.corabastos.com.co/sitio/historicoApp2/reportes/prueba.php). Para ello, se ha hecho uso del lenguaje de programación Python y de técnicas de *Web Scraping* para extraer la información alojada en las páginas HTML.

## Inspiración

El presente conjunto de datos podría utilizarse en el ámbito comercial, donde se podría elaborar modelos predictivos, que nos ayuden a predecir el precio del producto en el futuro, y con esto poder preparar estrategias de markiting.

También podría ser de gran utilidad en el campo de la *Agricultura*, para informar al pequeño productor de las temporadas de mayor de manda de sus productos en el mercado nacional, para que puedan preparar sus cosechas para suplir esta demanda.

## Licencia

Para la publicacion de este conjunto de datos se selecciono la licencia **CC BY-SA 4.0 License**. Los motivos por los cual se selecciono esta licencia son:

* _Los trabajos derivadas del conjunto de datos generado, su distribución se debe hacer con una licencia igual a la que regula el trabajo original_. Con esto garantizamos que los trabajos derivados del trabajo original, seguiran distribuyendose bajo los mismo terminos que el autor original planteo.

* _Se debe dar crédito de manera adecuada al creador del conjunto de datos generado, e indicar si se han realizado cambios_. De esta manera damos credito del trabajo del autor original, y mantenemos una transparencia en la medida que se indican las aportaciones/cambios realizados al trabajo original.

* _Explotación de los datos generados, incluyendo una finalidad comercial_. Con esto garantizamos que la utilizacion de los datos generados, no seran de uso privativo, dando la posibilidad que otras empresas utilicen los datos generados y realicen trabajos de calidad que mantenga su competitividad en el mercado.

## Código fuente y dataset

## Recursos





