  const uri = 'http://localhost:8000/location/';
let todos = [];

function getItems() {
  fetch(uri)
    .then(response => response.json())
    .then(data => _displayItems(data))
    .catch(error => console.error('Unable to get items.', error));
}

function addItem() {
  const addNameTextbox = document.getElementById('add-name');
  const addNameTextbox2 = document.getElementById('add-name2');
  const addNameTextbox3 = document.getElementById('add-name3');

  const item = {
      locationId:addNameTextbox.value.trim(),
      description:addNameTextbox2.value.trim(),
      locationType:addNameTextbox3.value.trim()
  };
   fetch(uri, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(item)
  })
    .then(response => response.json())
    .then(() => {
      getItems();
      addNameTextbox.value = '';
      addNameTextbox2.value = '';
      addNameTextbox3.value = '';
    })
    .catch(error => console.error('Unable to add item.', error));
}

function deleteItem(id) {
  fetch(`${uri}${id}/`, {
    method: 'DELETE'
  })
  .then(() => getItems())
  .catch(error => console.error('Unable to delete item.', error));
}

function displayEditForm(id) {
  const item = todos.find(item => item.id === id);

  document.getElementById('edit-name').value = item.locationId;
  document.getElementById('edit-name2').value = item.description;
  document.getElementById('edit-name3').value = item.locationType;
  document.getElementById('edit-id').value = item.id;
  document.getElementById('editForm').style.display = 'block';
}

function updateItem() {
  const itemId = document.getElementById('edit-id').value;
  const item = {
    id: parseInt(itemId, 10),
    locationId: document.getElementById('edit-name').value.trim(),
    description: document.getElementById('edit-name2').value.trim(),
    locationType: document.getElementById('edit-name3').value.trim()
  };

  fetch(`${uri}${itemId}/`, {
    method: 'PUT',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(item)
  })
  .then(() => getItems())
  .catch(error => console.error('Unable to update item.', error));

  closeInput();

  return false;
}

function closeInput() {
  document.getElementById('editForm').style.display = 'none';
  // document.getElementById('editForm2').style.display = 'none';
  // document.getElementById('editForm3').style.display = 'none';
}

function _displayCount(itemCount) {
  const name = (itemCount === 1) ? 'to-do' : 'to-dos';

  document.getElementById('counter').innerText = `${itemCount} ${name}`;
}

function _displayItems(data) {
  const tBody = document.getElementById('todos');
  tBody.innerHTML = '';

  _displayCount(data.length);

  const button = document.createElement('button');

  data.forEach(item => {
    // let isCompleteCheckbox = document.createElement('input');
    // isCompleteCheckbox.type = 'checkbox';
    // isCompleteCheckbox.disabled = true;
    // isCompleteCheckbox.checked = item.isComplete;

    let editButton = button.cloneNode(false);
    editButton.innerText = 'Edit';
    editButton.setAttribute('onclick', `displayEditForm(${item.id})`);

    let deleteButton = button.cloneNode(false);
    deleteButton.innerText = 'Delete';
    deleteButton.setAttribute('onclick', `deleteItem(${item.id})`);

    let tr = tBody.insertRow();

    // let td1 = tr.insertCell(0);
    // td1.appendChild(isCompleteCheckbox);

    let td2 = tr.insertCell(0);
    let textNode = document.createTextNode(item.locationId);
    td2.appendChild(textNode);

    let td3 = tr.insertCell(1);
    let textNode2 = document.createTextNode(item.description);
    td3.appendChild(textNode2);

    let td4 = tr.insertCell(2);
    let textNode3 = document.createTextNode(item.locationType);
    td4.appendChild(textNode3);


    let td5 = tr.insertCell(3);
    td5.appendChild(editButton);

    let td6 = tr.insertCell(4);
    td6.appendChild(deleteButton);
  });

  todos = data;
}