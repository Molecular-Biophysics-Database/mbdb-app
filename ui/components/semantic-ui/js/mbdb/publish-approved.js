import axios from "axios";

const http = axios.create({
  withCredentials: true,
  xsrfCookieName: "csrftoken",
  xsrfHeaderName: "X-CSRFToken",
  headers: { "Content-Type": "application/json" },
});

const form = document.getElementById("publish-approved");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const button = form.querySelector("button");
  const error = document.getElementById("publish-approved-error");
  button.disabled = true;
  error.hidden = true;
  try {
    const created = await http.post(form.dataset.createUrl, {});
    await http.post(created.data.links.actions.submit, {});
    window.location.assign(form.dataset.recordUrl);
  } catch (e) {
    console.error("Error publishing the draft", e);
    error.hidden = false;
    button.disabled = false;
  }
});
