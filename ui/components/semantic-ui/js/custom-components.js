import "@less/components/custom-components.less";

// Landing page search: the select chooses where the query is sent
const landingSearch = document.getElementById("mbdb-landing-search");
landingSearch?.addEventListener("submit", () => {
  landingSearch.action = landingSearch.querySelector("select").value;
});
