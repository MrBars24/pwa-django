var staticCacheName = 'pwadjango-v3';

self.addEventListener('install', function(event) {
    self.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName).then(function(cache) {
            return cache.addAll([
                '/offline',
                '/static/css/bootstrap.min.css',
                '/static/js/jquery-3.5.1.min.js',
                '/static/js/bootstrap.min.js',
                '/static/icons/google-icon.svg',
            ]);
        })
    );
});

self.addEventListener('fetch', event => {
    // Skip cross-origin requests, like those for Google Analytics.
    if (event.request.url.startsWith(self.location.origin)) {
      event.respondWith(
        caches.match(event.request).then(cachedResponse => {
          return cachedResponse || fetch(event.request);
        }).catch(function() {
          return fetch(event.request).then(function(response) {
            return response;
          }).catch(function() {
            return caches.match('/offline');
          });
        })
      );
    }
});