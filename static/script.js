function switchForm(form) {
  document.getElementById("login-box").classList.toggle("hidden", form !== "login");
  document.getElementById("signup-box").classList.toggle("hidden", form !== "signup");
}

function handleLogin(event) {
  event.preventDefault();
  document.getElementById("auth-section").classList.add("hidden");
  document.getElementById("dashboard-section").classList.remove("hidden");
  return false;
}

function handleSignup(event) {
  event.preventDefault();
  alert("Sign up successful. Please log in.");
  switchForm("login");
  return false;
}

// Dashboard Logic
function toggleDashboard() {
  document.getElementById("dashboard").classList.toggle("show");
}

function toggleCodeBox() {
  showOnly("code-section");
}

function toggleQuestionBox() {
  showOnly("question-box");
}

function toggleToolBox() {
  showOnly("tool-box");
}

function showOnly(idToShow) {
  ["code-section", "question-box", "tool-box"].forEach(id =>
    document.getElementById(id).classList.add("hidden")
  );
  document.getElementById(idToShow).classList.remove("hidden");
}

function showSection(sectionId) {
  ["main-section", "profile", "settings", "contact"].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.classList.add("hidden");
  });
  document.getElementById(sectionId).classList.remove("hidden");
}

function sendCode() {
  const code = document.getElementById("code").value;
  fetch("/api/explain", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerHTML = marked.parse(data.explanation);
  });
}

function submitQuestion() {
  const question = document.getElementById("user-question").value;
  fetch("/api/question", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("question-response").innerHTML = marked.parse(data.answer);
  });
}

function toggleDarkMode() {
  const isLight = document.body.classList.toggle('light-mode');
  localStorage.setItem("theme", isLight ? "light" : "dark");
}

window.addEventListener("DOMContentLoaded", () => {
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "light") {
    document.body.classList.add("light-mode");
  }
});