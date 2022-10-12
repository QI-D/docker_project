
function httpGet()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "http://localhost:8100/stats", false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

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
            getDate();
            dataDiv = document.getElementById('result-container');
            // Set current data text
            dataDiv.innerHTML = xhr.responseText;
        }
    }
    function getDate() {
        date = new Date().toString();

        document.getElementById('time-container').textContent
            = date;
    }
    (function () {
        getDate();
    })();