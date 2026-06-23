const http = require("http");
const fs = require("fs");
const path = require("path");

let PORT = parseInt(process.argv[2], 10) || 3000;

const MIME = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".gif": "image/gif",
  ".svg": "image/svg+xml",
  ".ico": "image/x-icon",
  ".webp": "image/webp",
  ".woff": "font/woff",
  ".woff2": "font/woff2",
  ".ttf": "font/ttf",
};

const ROOT = __dirname;

const server = http.createServer((req, res) => {
  // Strip query string and decode
  let urlPath = decodeURIComponent(req.url.split("?")[0]);

  // Serve home.html when root / is requested
  if (urlPath === "/" || urlPath === "") {
    urlPath = "/home.html";
  }

  // Resolve safely within ROOT to prevent path traversal
  const filePath = path.join(ROOT, path.normalize(urlPath));
  if (!filePath.startsWith(ROOT)) {
    res.writeHead(403);
    res.end("403 Forbidden");
    return;
  }

  fs.stat(filePath, (err, stats) => {
    let target = filePath;
    if (!err && stats.isDirectory()) {
      target = path.join(filePath, "index.html");
    }
    fs.readFile(target, (readErr, data) => {
      if (readErr) {
        res.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
        res.end("404 File not found");
        return;
      }
      const ext = path.extname(target).toLowerCase();
      res.writeHead(200, {
        "Content-Type": MIME[ext] || "application/octet-stream",
        // Prevent the browser from caching during development so edits always show
        "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
        "Pragma": "no-cache",
        "Expires": "0",
      });
      res.end(data);
    });
  });
});

server.on("error", (e) => {
  console.error(`Error starting server: ${e.message}`);
  process.exit(1);
});

server.listen(PORT, () => {
  console.log(`Serving static web server on port ${PORT}...`);
  console.log(`URL: http://localhost:${PORT}`);
});
