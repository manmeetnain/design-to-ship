const incidents = {
  "INC-248": { copy: "Checkout requests are failing after the latest API deployment. Revenue-impacting traffic is affected in three regions.", owner: "Priya S.", started: "13:41 UTC", affected: "Checkout API" },
  "INC-247": { copy: "Image-processing jobs in the EU region are completing above the expected latency budget.", owner: "Mateo R.", started: "13:29 UTC", affected: "Media workers" },
  "INC-245": { copy: "Webhook retry volume is increasing for two tenants while successful delivery remains stable elsewhere.", owner: "Unassigned", started: "12:58 UTC", affected: "Webhook delivery" }
};

const detailTitle = document.querySelector("#detail-title");
const detailCopy = document.querySelector(".detail-copy");
const detailValues = document.querySelectorAll(".detail-panel dd");
const detailStatus = document.querySelector("#detail-status");
const liveRegion = document.querySelector("#status-message");

document.querySelectorAll(".incident-select").forEach((button) => {
  button.addEventListener("click", () => {
    const id = button.dataset.incident;
    const incident = incidents[id];
    document.querySelectorAll(".incident").forEach((row) => row.classList.remove("is-selected"));
    document.querySelectorAll(".incident-select").forEach((item) => item.removeAttribute("aria-current"));
    button.closest(".incident").classList.add("is-selected");
    button.setAttribute("aria-current", "true");
    detailTitle.textContent = id;
    detailCopy.textContent = incident.copy;
    detailValues[0].textContent = incident.owner;
    detailValues[1].textContent = incident.started;
    detailValues[2].textContent = incident.affected;
    detailStatus.textContent = button.closest(".incident").dataset.acknowledged === "true" ? "Acknowledged" : "Unacknowledged";
  });
});

document.querySelectorAll(".acknowledge").forEach((button) => {
  button.addEventListener("click", () => {
    const row = button.closest(".incident");
    row.dataset.acknowledged = "true";
    button.textContent = "Acknowledged";
    button.disabled = true;
    const priority = row.querySelector(".priority");
    priority.textContent = "Acknowledged";
    priority.className = "priority acknowledged";
    if (row.classList.contains("is-selected")) detailStatus.textContent = "Acknowledged";
    liveRegion.textContent = `${button.dataset.ack} acknowledged`;
  });
});

document.querySelector("#priority-filter").addEventListener("change", (event) => {
  const selected = event.target.value;
  document.querySelectorAll(".incident").forEach((row) => {
    row.hidden = selected !== "all" && row.dataset.priority !== selected;
  });
});

