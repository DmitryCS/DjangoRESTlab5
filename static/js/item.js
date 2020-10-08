const uri = 'http://localhost:8000/inventory/item/';
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
    // isComplete: false,
    itemType: addNameTextbox.value.trim(),
    quality: addNameTextbox2.value.trim(),
    owner: addNameTextbox3.value.trim(),
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

  document.getElementById('edit-name').value = item.itemType;
  document.getElementById('edit-name2').value = item.quality;
  document.getElementById('edit-name3').value = item.owner;
  document.getElementById('edit-id').value = item.id;
  document.getElementById('editForm').style.display = 'block';
}

function updateItem() {
  const itemId = document.getElementById('edit-id').value;
  const item = {
    id: parseInt(itemId, 10),
    itemType: document.getElementById('edit-name').value.trim(),
    quality: document.getElementById('edit-name2').value.trim(),
    owner: document.getElementById('edit-name3').value.trim()
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
    let textNode = document.createTextNode(item.itemType);
    td2.appendChild(textNode);

    let td3 = tr.insertCell(1);
        // const item2 = {
        //   'player_id': document.getElementById('add-name3').value.trim()
        // };
        // fetch('http://localhost:8000/player/temp3/', {
        // method: 'POST',
        // headers: {
        //   'Accept': 'application/json',
        //   'Content-Type': 'application/json'
        // },
        // body: JSON.stringify(item2)
        // })
        // .then(response => response.json())
        // .then(() => {
        //   let textNode2 = document.createTextNode(response.json().player_id);
        //   td3.appendChild(textNode2);
        // })
        // .catch(error => console.error('Unable to add item.', error));
    let textNode2 = document.createTextNode(item.quality);
    td3.appendChild(textNode2);

    let td4 = tr.insertCell(2);
    let textNode3 = document.createTextNode(item.owner);
    td4.appendChild(textNode3);

    let td5 = tr.insertCell(3);
    td5.appendChild(editButton);

    let td6 = tr.insertCell(4);
    td6.appendChild(deleteButton);
  });

  todos = data;
}