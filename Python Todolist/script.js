const nameListEl = document.getElementById("nameList");

function addNameItem(name) {
  const li = document.createElement("li");
  li.className = "name-item";
  li.innerHTML = `
    <div class="avatar">${name.charAt(0).toUpperCase()}</div>
    <div class="name-text">
      <div class="name">${name}</div>
      <div class="sub">Student • Batch 2025</div>
    </div>
  `;
  nameListEl.appendChild(li);
}

// Fetch names from backend
fetch("http://127.0.0.1:5000/names")
  .then(res => res.json())
  .then(data => {
    data.names.forEach(name => addNameItem(name));
  })
  .catch(err => console.error(err));
