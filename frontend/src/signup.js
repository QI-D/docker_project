let signupBtn = document.getElementById("signup");

signupBtn.addEventListener('click', signup);

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

        location.href = "order.html"
    }
}

function signup(){
    username = document.getElementsByClassName('username')[0].value;
    password = document.getElementsByClassName('password')[0].value;

    signup_dict = {
        "username": username,
        "password": password
    }

    signup_str = JSON.stringify(signup_dict)
    console.log(signup_str)

    xhr = getXmlHttpRequestObject();
    xhr.onreadystatechange = sendDataCallback;
    // asynchronous requests
    xhr.open("POST", "http://localhost:8110/signup", true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    // Send the request over the network
    xhr.send(signup_str);
}
