const MESSAGE = "Go and study your Quran or your dev!";
const ROOT_CLASS = "sb-on";
const OVERLAY_ID = "sb-overlay";

let enabled = true;

function isShortsPage() {
  return location.pathname.startsWith("/shorts");
}

function showOverlay() {
  if (document.getElementById(OVERLAY_ID) || !document.body) return;
  const box = document.createElement("div");
  box.id = OVERLAY_ID;
  box.innerHTML = `
    <h1></h1>
    <p>Shorts are blocked.</p>
    <a href="/">Back to YouTube</a>`;
  box.querySelector("h1").textContent = MESSAGE;
  document.body.appendChild(box);
  // Stop the Short from playing behind the overlay.
  document.querySelectorAll("video").forEach((v) => v.pause());
}

function hideOverlay() {
  document.getElementById(OVERLAY_ID)?.remove();
}

function apply() {
  document.documentElement.classList.toggle(ROOT_CLASS, enabled);
  if (enabled && isShortsPage()) showOverlay();
  else hideOverlay();
}

// Load state ASAP (document_start) so there is no flash of Shorts.
chrome.storage.local.get({ enabled: true }, (s) => {
  enabled = s.enabled;
  apply();
});

// React to the popup toggle without reloading the page.
chrome.storage.onChanged.addListener((changes) => {
  if (changes.enabled) {
    enabled = changes.enabled.newValue;
    apply();
  }
});

// YouTube is a single-page app: re-check on its navigation events,
// plus a light interval as a safety net (also keeps paused video paused).
window.addEventListener("yt-navigate-finish", apply);
window.addEventListener("popstate", apply);
setInterval(() => {
  if (enabled && isShortsPage()) {
    showOverlay();
    document.querySelectorAll("video").forEach((v) => !v.paused && v.pause());
  }
}, 500);
