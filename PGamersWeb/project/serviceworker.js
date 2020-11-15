var CACHE_NAME = 'my-site-cache-v1'; /* Nombre Cache*/
var urlsToCache = [ /* URL cache */
    '/',
    '/static/css/estilos.css',
    '/static/img/Contacto.jpg',
];

self.addEventListener('install', function(event) { /* Instalacion */
    // Perform install steps
    event.waitUntil(
        caches.open(CACHE_NAME)
        .then(function(cache) {
            console.log('Opened cache');
            return cache.addAll(urlsToCache);
        })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(

        fetch(event.request)
        .then((result) => {
            return caches.open(CACHE_NAME)
                .then(function(c) {
                    c.put(event.request.url, result.clone())
                    return result;
                })

        })
        .catch(function(e) {
            return caches.match(event.request)
        })



    );
});