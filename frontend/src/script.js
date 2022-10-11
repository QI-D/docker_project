let makeExpenseBtn = document.getElementById("place-order");
let signupBtn = document.getElementById("sign-up");
let loginBtn = document.getElementById("login");

makeExpenseBtn.addEventListener('click', makeExpense);
// signupBtn.addEventListener('click', signup);
// loginBtn.addEventListener('click', login);

var xhr = null;

getXmlHttpRequestObject = function () {
    if (!xhr) {
        // Create a new XMLHttpRequest object 
        xhr = new XMLHttpRequest();
    }
    return xhr;
};

function dataCallback() {
    // Check response is ready or not
    if (xhr.readyState == 4 && xhr.status == 200) {
        console.log("User data received!");
        dataDiv = document.getElementById('result-container');
        // Set current data text
        dataDiv.innerHTML = xhr.responseText;
    }
}

function sendDataCallback() {
    // Check response is ready or not
    if (xhr.readyState == 4 && xhr.status == 201) {
        console.log("Data creation response received!");
        dataDiv = document.getElementsByClassName('sent-data-container');
        // Set current data text
        dataDiv.innerHTML = xhr.responseText;
    }
}

function uuidv4() {
    return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
      (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
  }

function makeExpense(event) {
    order_id = uuidv4()
    item_id = document.getElementsByClassName('item-id')[0].value;
    item_name = document.getElementsByClassName('item-name')[0].value;
    quantity = document.getElementsByClassName('quantity')[0].value;
    price = document.getElementsByClassName('price')[0].value;
    expense_dict = {"order_id": order_id,
                    "item_id": item_id,
                    "item_name": item_name,
                    "quantity": parseInt(quantity),
                    "price": parseFloat(price),
                    "timestamp": Date.now()}

    expense_str = JSON.stringify(expense_dict)
    console.log("Sending data: " + expense_str);

    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = sendDataCallback;
    // asynchronous requests
    xhr.open("POST", "http://localhost:8080/expense", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    // Send the request over the network
    xhr.send(expense_str);

    document.getElementsByClassName('item-id')[0].value = "";
    document.getElementsByClassName('item-name')[0].value = "";
    document.getElementsByClassName('quantity')[0].value = "";
    document.getElementsByClassName('price')[0].value = "";
}

// function signup(){
//     location.href = "signup.html"
// }

// function login(){
//     location.href = "login.html"
// }
