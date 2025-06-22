function hideAllSections() {
  document.getElementById("code-section").classList.add("hidden");
  document.getElementById("question-box").classList.add("hidden");
  document.getElementById("tool-box").classList.add("hidden");
}

function toggleCodeBox() {
  const section = document.getElementById("code-section");
  const isVisible = !section.classList.contains("hidden");
  hideAllSections();
  if (!isVisible) section.classList.remove("hidden");
}

function toggleQuestionBox() {
  const section = document.getElementById("question-box");
  const isVisible = !section.classList.contains("hidden");
  hideAllSections();
  if (!isVisible) section.classList.remove("hidden");
}

function toggleToolBox() {
  const section = document.getElementById("tool-box");
  const isVisible = !section.classList.contains("hidden");
  hideAllSections();
  if (!isVisible) section.classList.remove("hidden");
}

function sendCode() {
  const code = document.getElementById("code").value;
  fetch("/api/explain", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ code })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").textContent = data.explanation;
    });
}

function submitQuestion() {
  const question = document.getElementById("user-question").value;
  fetch("/api/question", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("question-response").textContent = data.answer;
    });
}
