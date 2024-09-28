document.getElementById('helloBtn').addEventListener('click', function() {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        const currentTab = tabs[0];
        if (currentTab) {
            document.getElementById('message').textContent = currentTab.url;
          } else {
            document.getElementById('message').textContent = 'Unable to get URL';
          }
        });    
    }
);