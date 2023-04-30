var tableBody = document.getElementById("reservation-table-body");

function addRow(name, room, time) {
  var nameCell = document.createElement("td");
  var roomCell = document.createElement("td");
  var timeCell = document.createElement("td");

  nameCell.textContent = name;
  roomCell.textContent = room;
  timeCell.textContent = time;

  nameCell.style.textAlign = "center";
  roomCell.style.textAlign = "center";
  timeCell.style.textAlign = "center";

  var newRow = document.createElement("tr");

  newRow.appendChild(nameCell);
  newRow.appendChild(roomCell);
  newRow.appendChild(timeCell);

  tableBody.appendChild(newRow);

  console.log(newRow.rowIndex);
}

var reserveButton = document.getElementById("reserve-button");

var nameField = document.getElementById("name-field");
var roomField = document.getElementById("room-field");
var timeField = document.getElementById("time-field");

reserveButton.addEventListener("click", function() {
  
  //console.log(timeField.value)
  if(nameField.value.length != 0 && roomField.value.length != 0 && timeField.value.length != 0){
    addRow(nameField.value, roomField.value, timeField.value);    
  }

  nameField.value = ''
  roomField.value = ''
  timeField.value = ''
})


