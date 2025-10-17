![Header](/blog/images/Hello_South_Park.webp){.header_image}
# Hola, South Park {.blog_entry_tittle}

Esta es la primera entrada del blog de desarrollo de la API.
{.blog_intro}

Finalmente he decidido tratar esta API como un proyecto vivo: mientras la aplicación esté en beta, la API permanecerá en funcionamiento durante su desarrollo. Creo que esto tiene ventajas e inconvenientes, tanto para mí como para los usuarios.

- Podré trabajar y probar la API en vivo y recibir feedback.
- Una mayor implicación por mi parte al saber que va evolucionando.
- Tener un proyecto más serio, con un historial de actualizaciones y un changelog con los cambios.
- Posibilidad de hacer un proyecto más sólido y mejor organizado.

El problema es que no voy a poder garantizar que la API siempre sea compatible con los cambios que vayan surgiendo hasta llegar a la versión 1; después de eso versionaré la API.

## Cambios en esta actualización {.blog_title}

### Blog de desarrollo {.blog_subtitle}
El principal cambio en esta web es este mismo blog de desarrollo. Al ser un proyecto que se va a mantener vivo, veo necesario tener un blog contando las actualizaciones. Este blog está creado gracias a un sistema de paginado dinámico que he creado usando el backend de la web. Esta estructura es capaz de interpretar ficheros en Markdown como el que estoy escribiendo ahora mismo. Estos ficheros tienen un formato específico que es convertido a un HTML con clases a las que posteriormente le doy formato por CSS y posee un listado de todos los artículos que quiero que se muestren, de forma que puedo estar trabajando en un artículo que esté en el código pero sin publicarlo.

![Markdown Document](/blog/images/Markdown_Dev_Blog.webp){.body_image}

De momento estoy muy contento con este resultado, aunque lo iré cambiando y modificando según las necesidades del momento. Aún no soy muy consciente de las limitaciones que tiene al ser algo totalmente casero. Lo iré mejorando.

Aunque como de momento, a fecha de escribir esto, solo tiene 2 artículos no se ve, pero tiene un sistema de paginación que según el número de artículos va generando páginas. En este ejemplo he generado 16 artículos, copiando y pegando el mismo (tampoco voy a escribir tanto), y crea 2 páginas de 6 artículos y una adicional de 4, es decir, 16 artículos en 3 páginas.

![Blog Index](/blog/images/Blog_index.webp){.body_image}

### 404 NOT FOUND {.blog_subtitle}

Durante el desarrollo de la página de blog surgió la necesidad de asegurarse que el usuario no acaba en webs vacías y sitios raros, por ello he tenido que crear una página de ruta no encontrada, es la siguiente.

![404 Page](/blog/images/Page_404.webp){.body_image}

Esta página tiene a mi avatar de South Park con un cartel. Iba a hacerlo con Stan, Kyle, Kenny y Cartman pero de momento no he encontrado cómo hacerlo y que quede bien.

Esta página tiene 4 diseños: 3 diseños que tienen un 33% de probabilidades de aparecer y uno secreto que tiene un 1% de probabilidades de aparecer.

![404 Avatars](/blog/images/404_Avatars.webp){.body_image}

Como me gusta dar algo de intriga lo podéis ver aquí o si no podéis esperar a que salga, jeje: [Avatar Secreto](/img/website/Cartel_NOT_FOUND_Charlie_Brown.webp)

Además, podéis volver a la web o al blog directamente desde aquí.

### Mensaje del desarrollador {.blog_subtitle}

Reconozco que estoy logrando un proyecto bastante más sólido de lo que pensaba; me está gustando muchísimo cómo se ve y las posibilidades que le veo. Aunque soy consciente de que muchas partes pueden y deberían automatizarse, lo estoy disfrutando o al menos trato de disfrutarlo.

El problema de que el index tarda mucho en cargar es grave y estoy barajando múltiples opciones para arreglarlo, tomaré la que considere mejor o incluso combinar varias de ellas.

Quiero ver mis proyectos como si fuesen mis hijos y tratar a cada uno con la delicadeza que merecen. Podría dedicarme a hacer proyectos pequeños, pero me gusta ver cómo algo así va evolucionando con el tiempo.

Quiero poder sentirme orgulloso de lo que hago y ver que todo el esfuerzo puesto en un proyecto así merece la pena a medio-largo plazo.

La próxima actualización saldrá el 17-18 de octubre de 2025 añadiendo a la API el primer capítulo de la temporada 28. Será algo muy pequeño pero creo que haré un pequeño artículo hablando del tema.