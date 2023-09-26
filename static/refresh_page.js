let autoRefreshInterval;
let autoRefreshEnabled = false;

function toggleAutoRefresh() {
    autoRefreshEnabled = !autoRefreshEnabled;

    if (autoRefreshEnabled) {
        autoRefreshInterval = setInterval(() => {
            location.reload();
        }, 5000); // Refresh every 5 seconds
    } else {
        clearInterval(autoRefreshInterval);
    }
}

