![Header](/blog/images/Index_Optimization_Part1_ES.webp){.header_image}
# Optimización del índice — Parte 1 {.blog_entry_title}

Esta entrada del blog de desarrollo trata sobre una actualización que he hecho del índice de la web. Desde la creación ya sabía que cargaba muy lento; esto se debe a que la página cargaba entera desde el principio y, además, es dinámica con la API: todas las fichas de personajes se generan al momento. El problema era que hacía unas 50 peticiones de golpe. Esto provocaba que la web tardara en cargar porque no terminaba hasta procesar las 50 peticiones.
{.blog_intro}

He optimizado esto para que la web solo haga las peticiones necesarias; es decir, ahora solo carga lo que estás viendo. Por ejemplo, en este caso solo está cargando las 12 peticiones que necesita.

![Header](/blog/images/Characters_Loaded_Index_1.webp){.body_image}

Ahora, al momento de cargar, solo debe cargar como máximo un 20 % del contenido original, lo cual ha mejorado enormemente la carga del servidor. No obstante, el problema ahora es el tiempo que tarda en procesar las peticiones a la API. A la hora de servir la web he optado por la forma más barata de ponerlo en producción; esto ha resultado en que estoy usando un servidor con 0,5 GB de RAM y un hilo de procesador con baja disponibilidad. Por ello la API es tan lenta que tarda 6 segundos en procesar una petición; al ser 12 peticiones eso es más de un minuto para cargar el índice, en comparación con menos de 1 segundo que tarda en mi equipo.

![Header](/blog/images/Example_Remote_Server_1.webp){.body_image}

![Header](/blog/images/Example_LocalHost_Server_1.webp){.body_image}

He dejado probar a algunas personas la versión local y parece que ha gustado, pero no es algo que tendría expuesto permanentemente: primero por no revelar mi IP pública y segundo por no tener el equipo encendido todo el rato.

He estado haciendo números y para tener este equipo desplegado y con una disponibilidad aceptable me costaría aproximadamente 30–40 € al mes, un coste que veo excesivo sobre todo para algo que aún está en desarrollo y del que no sé cuánto tiempo me va a llevar; me gustaría terminarlo para marzo.

Comprar una Raspberry Pi 5 y autohostearlo con un proxy inverso cada vez me parece una mejor opción; no creo que esto escale lo suficiente como para necesitar un hosting dedicado. Y si al final es así supongo que será porque ha triunfado.

Intentaré seguir optimizando este proyecto en la medida de lo posible. Las imágenes ya no suponen un problema a nivel de carga, por lo menos no uno tan grande. Seguiré informando.

Adiós. Muchas gracias por leer esto.