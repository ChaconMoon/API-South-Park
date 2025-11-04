![Header](/blog/images/Index_Optimization_Part2_ES.webp){.header_image}
# Optimización del índice — Parte 2 {.blog_entry_title}

Esta entrada del blog es para hablar sobre la segunda parte de la optimización del índice.
{.blog_intro}

### Optimización del índice. {.blog_subtitle}

Al final he optado por hacer que los iframes que se cargan en la web principal sean estáticos, esto provoca que ahora la web del índice no refleje el estado real de la API, solo el que tenía al momento de hacer esta actualización, pero acelera enormemente la carga de la web, cargando bastante rápido a pesar de las limitaciones del servidor que lo aloja.

No obstante, la parte dinámica de la web no ha sido eliminada del código, solo ha sido comentada, por lo que en cuanto me pueda permitir un mejor hosting descomentar esa parte y el índice volverá a ser dinámico.

### Otras mejoras en la organización del proyecto. {.blog_subtitle}

Además de estos cambios, se han hecho otras mejoras en el código de la API, se han reestructurado los endpoints dentro del código. Hasta ahora todos los endpoints están categorizados, de forma que me es más fácil trabajar por categorías ya que tengo todo dentro de la misma carpeta. Además, la función ``main`` del proyecto ahora solo inicia la aplicación, esa es su única función; toda la API se estructura ahora mismo de forma independiente.

También se ha mejorado el modelo de datos dentro de todos los endpoints y ahora todos los objetos que devuelve la API heredan de un mismo objeto que los obliga a implementar los métodos necesarios, dejando toda la parte de dar formato a las respuestas al modelo de datos.

Además, ahora he implementado un pre-commit que me fuerza a comentar y me permitirá asegurarme que todo el código esté mejor formateado antes de hacer un cambio en GitHub, por lo que es probable que las actualizaciones tarden más en llegar, pero serán de mayor calidad.

### Mejoras del proyecto a futuro. {.blog_subtitle}

Además de las mejoras anteriormente mencionadas, a futuro se mejorará la conexión con la base de datos. Debido a las prisas de inicios del proyecto, las queries a la base de datos están "hardcodeadas", cosa que es incorrecta. Lo suyo sería usar un ORM; este cambio se hará a futuro, junto con la implementación de interfaces para las conexiones de la base de datos para tratar que la conexión con la base de datos esté lo más abstraída posible con la finalidad de tener un software lo más sólido posible.