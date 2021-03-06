var CACHE_NAME = 'my-site-cache-v1'; /* Nombre del Cache*/
var urlsToCache = [ /* URLS que se dejaran en el cache */
    '/',
    '/static/css/estilos.css',
    '/static/img/imagen_slider_1.png',
    '/static/img/imagen_slider_2.png',
    '/static/img/imagen_slider_3.png',
    '/static/img/Logo.png',
    '/static/img/PortadaContacto.jpg',
];

self.addEventListener('install', function(event) { /* Instalacion */
    // Perform install steps
    event.waitUntil(
        caches.open(CACHE_NAME) /* Apertura del cache definido en la variable CACHE_NAME */
        .then(function(cache) {
            console.log('Opened cache');
            return cache.addAll(urlsToCache); /* se agregan todas las urls definidas al cache de la pagina web  */
        })
    );
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                .filter(cacheName => (cacheName !== CACHE_NAME))
                .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

self.addEventListener('fetch', function(event) { /* peticion */
    event.respondWith(
        fetch(event.request) /* Hace una peticion */
        .then(function(result) { /* Una vez pedida la peticion, entrega un resultado */
            return caches.open(CACHE_NAME) /* luego se retornar la apertura del cache definido en la variable CACHE_NAME */
                .then(function(c) { /* Funcion que retorna el cache como paratro */
                    c.put(event.request.url, result.clone())
                        /* se utiliza el metodo put del parametro definido para que al momento de que se entregue una respuesta (IMAGEN/ARCHIVOS/URL), este se clone y
                         se guarde como resultado  */
                    return result; /* retorna el resultado */
                })

        })
        .catch(function(e) { /* si hay algun fallo, se introduce un catch */
            return caches.match(event.request) /* se retorna del cache, lo que el usuario pidio */
        })
    );
});