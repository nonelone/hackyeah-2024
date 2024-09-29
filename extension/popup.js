//Set variable holding url for api
var base_url = "http://145.239.93.49:5000";
var api_url = base_url + "/api";

//give function to check-page button
document.getElementById('check-page').addEventListener('click', function() {
    //get the current tab
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        //send a alert with current tab url
        // alert(tabs[0].url);
        sendUrl(tabs[0].url);
    });
});

//function sending current url to api and recive response as raw text
function sendUrl(url) {
    //fetch data from api
    replaceBody("templates/loading.html");
    fetch(api_url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded' // lub 'text/plain' w zależności od API
        },
        body: `url=${encodeURIComponent(url)}`
    }).then(response => response.text())
    .then(data => {
        //possible data is insecure / bad_protocol / dangerous / success
        //for each case replace body with corresponding html
        switch(data) {
            case "insecure":
                replaceBody("templates/insecure.html");
                replaceUrl(base_url + "/protected/insecure");
                break;
            case "bad_protocol":
                replaceBody("templates/bad_protocol.html");
                replaceUrl(base_url + "/protected/bad_protocol");
                break;
            case "dangerous":
                replaceBody("templates/dangerous.html");
                replaceUrl(base_url + "/protected/dangerous");
                break;
            case "success":
                replaceBody("templates/success.html");
                break;
            default:
                document.body.innerHTML = "<h1>Error!</h1><p>Something went wrong!</p>";
        }
    });
}

//function replacing a url in browser tab
function replaceUrl(url) {
    //get current tab
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        //update url
        chrome.tabs.update(tabs[0].id, {url: url});
    });
}

//function reading content of html file and replacing body with it
function replaceBody(file) {
    //fetch file
    fetch(file)
    .then(response => response.text())
    .then(data => {
        //replace body with content of file
        document.body.innerHTML = data;
    });
}