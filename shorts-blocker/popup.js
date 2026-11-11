const btn = document.getElementById("toggle");
const status = document.getElementById("status");

function render(enabled) {
  btn.textContent = enabled ? "Blocking: ON" : "Blocking: OFF";
  btn.className = enabled ? "on" : "off";
  status.textContent = enabled ? "Shorts are hidden." : "Shorts are visible.";
}

chrome.storage.local.get({ enabled: true }, (s) => render(s.enabled));

btn.addEventListener("click", () => {
  chrome.storage.local.get({ enabled: true }, (s) => {
    const enabled = !s.enabled;
    chrome.storage.local.set({ enabled }, () => render(enabled));
  });
});
