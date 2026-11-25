// Madinah Arabic Course - Progressive Web App Service Worker
const CACHE_NAME = 'madinah-arabic-supabase-v15';

const PRECACHE_ASSETS = [
  './',
  './index.html',
  './styles.css',
  './app.js',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-192.png',
  './icons/icon-maskable.png',
  './icons/icon.svg',
  './icons/screenshot-mobile.png',
  './icons/screenshot-desktop.png'
];

// All studio-grade Arabic male audio files (1.85 MB total)
const AUDIO_ASSETS = [
  "./audio/aud_0109be90f8.mp3",
  "./audio/aud_0155f0380e.mp3",
  "./audio/aud_01bf733965.mp3",
  "./audio/aud_03d6c88968.mp3",
  "./audio/aud_04c185a78d.mp3",
  "./audio/aud_0c283f4576.mp3",
  "./audio/aud_0ca750579e.mp3",
  "./audio/aud_0de29840c7.mp3",
  "./audio/aud_0e374a7107.mp3",
  "./audio/aud_0e78c302ff.mp3",
  "./audio/aud_0f52d578b8.mp3",
  "./audio/aud_0fcfdead28.mp3",
  "./audio/aud_17166ff2a9.mp3",
  "./audio/aud_1793747c4f.mp3",
  "./audio/aud_17c8cbb33d.mp3",
  "./audio/aud_19bdbd14fc.mp3",
  "./audio/aud_1b79b22892.mp3",
  "./audio/aud_1babcbb96a.mp3",
  "./audio/aud_1bdccf28c9.mp3",
  "./audio/aud_1d3480ff70.mp3",
  "./audio/aud_1d8ef4b45e.mp3",
  "./audio/aud_1f08ecd597.mp3",
  "./audio/aud_2196dff599.mp3",
  "./audio/aud_23433deaf4.mp3",
  "./audio/aud_2a9fcc62b1.mp3",
  "./audio/aud_2d26852aa6.mp3",
  "./audio/aud_2f41481a67.mp3",
  "./audio/aud_30ce8cc0ea.mp3",
  "./audio/aud_31756427b7.mp3",
  "./audio/aud_341754213a.mp3",
  "./audio/aud_384559cabb.mp3",
  "./audio/aud_3d1acfa1cc.mp3",
  "./audio/aud_408655bb08.mp3",
  "./audio/aud_430908c7a4.mp3",
  "./audio/aud_45f6538b4e.mp3",
  "./audio/aud_47f41d1d59.mp3",
  "./audio/aud_497b54314a.mp3",
  "./audio/aud_4b1a924717.mp3",
  "./audio/aud_4b734617b4.mp3",
  "./audio/aud_4df4c0d5b2.mp3",
  "./audio/aud_4e7bfd8e2d.mp3",
  "./audio/aud_4f8ed80d67.mp3",
  "./audio/aud_53016c9637.mp3",
  "./audio/aud_54049fdfa1.mp3",
  "./audio/aud_54d31612ee.mp3",
  "./audio/aud_590e3d72ff.mp3",
  "./audio/aud_5ab5dff0fb.mp3",
  "./audio/aud_5ca4f3ec9b.mp3",
  "./audio/aud_5d844ffd3a.mp3",
  "./audio/aud_634f3a3256.mp3",
  "./audio/aud_63db797e07.mp3",
  "./audio/aud_6495c0b819.mp3",
  "./audio/aud_64cbb6ca9c.mp3",
  "./audio/aud_6706fae2a2.mp3",
  "./audio/aud_6a72cd6f24.mp3",
  "./audio/aud_6c39c18acf.mp3",
  "./audio/aud_6ecc8aca8e.mp3",
  "./audio/aud_722aaa1a6e.mp3",
  "./audio/aud_727ace9f0d.mp3",
  "./audio/aud_733250507c.mp3",
  "./audio/aud_757ac2fe8f.mp3",
  "./audio/aud_7a4fe11db5.mp3",
  "./audio/aud_7cfeb5540d.mp3",
  "./audio/aud_7d0d9633ae.mp3",
  "./audio/aud_7db09dac3a.mp3",
  "./audio/aud_7e261f0188.mp3",
  "./audio/aud_7fc0904f28.mp3",
  "./audio/aud_808d9167f5.mp3",
  "./audio/aud_83dc734d4d.mp3",
  "./audio/aud_84b41f7cae.mp3",
  "./audio/aud_8856716253.mp3",
  "./audio/aud_891a85ce2d.mp3",
  "./audio/aud_8babd4aef8.mp3",
  "./audio/aud_8d2074f040.mp3",
  "./audio/aud_8d2bf29c0c.mp3",
  "./audio/aud_8d60b1400d.mp3",
  "./audio/aud_8fb1e36531.mp3",
  "./audio/aud_91360a0a71.mp3",
  "./audio/aud_92f161a8eb.mp3",
  "./audio/aud_93909a4cc0.mp3",
  "./audio/aud_94a8028344.mp3",
  "./audio/aud_94bff9fdf3.mp3",
  "./audio/aud_95fc82c942.mp3",
  "./audio/aud_96297b1663.mp3",
  "./audio/aud_97d3494cd6.mp3",
  "./audio/aud_9abb42a7bb.mp3",
  "./audio/aud_9c1c599a29.mp3",
  "./audio/aud_9c44457e9c.mp3",
  "./audio/aud_9d7dce31e7.mp3",
  "./audio/aud_9dfa14ecc0.mp3",
  "./audio/aud_a1a0efdd7f.mp3",
  "./audio/aud_a56ff2fa6c.mp3",
  "./audio/aud_a582813eb8.mp3",
  "./audio/aud_aa172409e6.mp3",
  "./audio/aud_aa53875937.mp3",
  "./audio/aud_acfccdb6a2.mp3",
  "./audio/aud_ad9475deec.mp3",
  "./audio/aud_ae038db14e.mp3",
  "./audio/aud_ae36b01b91.mp3",
  "./audio/aud_af3e58e502.mp3",
  "./audio/aud_b363b32eae.mp3",
  "./audio/aud_b3c57b322e.mp3",
  "./audio/aud_b540f2ee00.mp3",
  "./audio/aud_b97eaf4498.mp3",
  "./audio/aud_ba661b37f7.mp3",
  "./audio/aud_bc72062134.mp3",
  "./audio/aud_bea1d9d4f5.mp3",
  "./audio/aud_c2328f2808.mp3",
  "./audio/aud_c2bb02d8ee.mp3",
  "./audio/aud_c492c253b0.mp3",
  "./audio/aud_c4cae34a65.mp3",
  "./audio/aud_c693e4c7da.mp3",
  "./audio/aud_c937bfa37d.mp3",
  "./audio/aud_c970473aa6.mp3",
  "./audio/aud_cd55ca03da.mp3",
  "./audio/aud_ce4dcfab0b.mp3",
  "./audio/aud_cf177bb44c.mp3",
  "./audio/aud_d030974c84.mp3",
  "./audio/aud_d1007153ed.mp3",
  "./audio/aud_d184cb24f9.mp3",
  "./audio/aud_d29ecb44d0.mp3",
  "./audio/aud_d2b4b4acc2.mp3",
  "./audio/aud_d4c49c94cb.mp3",
  "./audio/aud_d53373ef80.mp3",
  "./audio/aud_d9d9ea2880.mp3",
  "./audio/aud_df5d2fb1fe.mp3",
  "./audio/aud_e07c3c4110.mp3",
  "./audio/aud_e1ae41b44c.mp3",
  "./audio/aud_e23745a0ff.mp3",
  "./audio/aud_e328e95503.mp3",
  "./audio/aud_e37bda96c5.mp3",
  "./audio/aud_e47aabdf00.mp3",
  "./audio/aud_ea6adf6265.mp3",
  "./audio/aud_ead2d86edb.mp3",
  "./audio/aud_ec402b6c36.mp3",
  "./audio/aud_ec4e3ec5e7.mp3",
  "./audio/aud_edbffd8a9a.mp3",
  "./audio/aud_eef6015c4b.mp3",
  "./audio/aud_f01f5b0399.mp3",
  "./audio/aud_f07bca6593.mp3",
  "./audio/aud_f49a8c05ee.mp3",
  "./audio/aud_f72b4f34ae.mp3",
  "./audio/aud_fce4167b42.mp3",
  "./audio/aud_fee378b08c.mp3",
  "./audio/aud_ffcde90479.mp3"
];

// Install: Pre-cache core app shell immediately & download audio in background
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[SW] Pre-caching offline app shell');
      return cache.addAll(PRECACHE_ASSETS);
    }).then(() => {
      // Background cache all audio files (1.85 MB total) so playback is instant & offline
      caches.open(CACHE_NAME).then((cache) => {
        return Promise.allSettled(
          AUDIO_ASSETS.map((url) =>
            fetch(url).then((res) => {
              if (res.ok) return cache.put(url, res);
            }).catch(() => {})
          )
        );
      });
    }).then(() => self.skipWaiting())
  );
});

// Activate: Clean up old caches & take control immediately
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            console.log('[SW] Removing old cache:', cache);
            return caches.delete(cache);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch: Dedicated Cache-First for Audio & Fonts, Stale-While-Revalidate for app assets
self.addEventListener('fetch', (event) => {
  const req = event.request;
  const url = new URL(req.url);

  if (req.method !== 'GET') return;

  // 1. Audio Files: CACHE-FIRST for Instant 0ms Voice Playback on GitHub Pages
  if (url.pathname.includes('/audio/') || url.pathname.endsWith('.mp3')) {
    event.respondWith(
      caches.match(req).then((cached) => {
        if (cached) return cached;
        // If not in cache yet, fetch via standard GET and store in cache
        return fetch(req).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(req, clone));
          }
          return networkResponse;
        });
      })
    );
    return;
  }

  // 2. Google Fonts & CDNs: Cache-First
  if (url.origin.includes('fonts.googleapis.com') || url.origin.includes('fonts.gstatic.com') || url.origin.includes('cdn.jsdelivr.net')) {
    event.respondWith(
      caches.match(req).then((cached) => {
        if (cached) return cached;
        return fetch(req).then((res) => {
          if (!res || res.status !== 200) return res;
          const clone = res.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(req, clone));
          return res;
        });
      })
    );
    return;
  }

  // 3. App Shell & Assets: Stale-While-Revalidate
  event.respondWith(
    caches.match(req).then((cachedResponse) => {
      const fetchPromise = fetch(req).then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(req, responseToCache);
          });
        }
        return networkResponse;
      }).catch((err) => {
        console.log('[SW] Fetch failed; returning cached if available:', err);
      });

      return cachedResponse || fetchPromise;
    })
  );
});
