// Dashboard.js - JavaScript functionality for the IoT Dashboard

// Format timestamp to a more readable format
function formatTimestamp() {
    document.querySelectorAll('.sensor-timestamp').forEach(timestamp => {
        const rawTime = timestamp.textContent.replace('Updated: ', '');
        
        // Create a Date object from the ISO string
        const date = new Date(rawTime);
        
        // Format the date and time in a more readable format
        const formattedTime = date.toLocaleString('en-US', {
            month: 'short',
            day: 'numeric',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
        
        timestamp.innerHTML = `<i class="far fa-clock"></i> Updated: ${formattedTime}`;
    });
}

// Add visual indicator for sensor values
function addValueIndicators() {
    // Temperature indicator (normal range: 18-25°C)
    const tempCard = document.querySelector('.sensor-card.temperature');
    if (tempCard) {
        const tempValue = parseFloat(tempCard.querySelector('.sensor-value').textContent);
        if (tempValue < 18) {
            tempCard.classList.add('cold');
            tempCard.querySelector('.card-body').insertAdjacentHTML('afterbegin', 
                '<div class="status-indicator cold"><i class="fas fa-snowflake"></i> Cold</div>');
        } else if (tempValue > 25) {
            tempCard.classList.add('hot');
            tempCard.querySelector('.card-body').insertAdjacentHTML('afterbegin', 
                '<div class="status-indicator hot"><i class="fas fa-fire"></i> Hot</div>');
        } else {
            tempCard.classList.add('normal');
            tempCard.querySelector('.card-body').insertAdjacentHTML('afterbegin', 
                '<div class="status-indicator normal"><i class="fas fa-check"></i> Normal</div>');
        }
    }
    
    // Humidity indicator (normal range: 30-60%)
    const humidityCard = document.querySelector('.sensor-card.humidity');
    if (humidityCard) {
        const humidityValue = parseFloat(humidityCard.querySelector('.sensor-value').textContent);
        if (humidityValue < 30) {
            humidityCard.classList.add('dry');
            humidityCard.querySelector('.card-body').insertAdjacentHTML('afterbegin', 
                '<div class="status-indicator dry"><i class="fas fa-sun"></i> Dry</div>');
        } else if (humidityValue > 60) {
            humidityCard.classList.add('humid');
            humidityCard.querySelector('.card-body').insertAdjacentHTML('afterbegin', 
                '<div class="status-indicator humid"><i class="fas fa-cloud-rain"></i> Humid</div>');
        } else {
            humidityCard.classList.add('normal');
            humidityCard.querySelector('.card-body').insertAdjacentHTML('afterbegin', 
                '<div class="status-indicator normal"><i class="fas fa-check"></i> Normal</div>');
        }
    }
    
    // CO2 indicator (normal range: 400-1000 ppm)
    const co2Card = document.querySelector('.sensor-card.co2');
    if (co2Card) {
        const co2Value = parseFloat(co2Card.querySelector('.sensor-value').textContent);
        if (co2Value < 400) {
            co2Card.classList.add('low');
            co2Card.querySelector('.card-body').insertAdjacentHTML('afterbegin', 
                '<div class="status-indicator low"><i class="fas fa-arrow-down"></i> Low</div>');
        } else if (co2Value > 1000) {
            co2Card.classList.add('high');
            co2Card.querySelector('.card-body').insertAdjacentHTML('afterbegin', 
                '<div class="status-indicator high"><i class="fas fa-exclamation-triangle"></i> High</div>');
        } else {
            co2Card.classList.add('normal');
            co2Card.querySelector('.card-body').insertAdjacentHTML('afterbegin', 
                '<div class="status-indicator normal"><i class="fas fa-check"></i> Normal</div>');
        }
    }
}

// Update the countdown timer for auto-refresh
function updateRefreshCountdown() {
    let countdown = 60; // 60 seconds
    const countdownDisplay = document.getElementById('refresh-countdown');
    
    if (countdownDisplay) {
        const interval = setInterval(() => {
            countdown--;
            countdownDisplay.textContent = countdown;
            
            if (countdown <= 0) {
                clearInterval(interval);
            }
        }, 1000);
    }
}

// Initialize the dashboard when the DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    formatTimestamp();
    addValueIndicators();
    updateRefreshCountdown();
    
    // Add refresh countdown to the page
    const container = document.querySelector('.dashboard-header');
    if (container) {
        container.insertAdjacentHTML('beforeend', 
            '<div class="refresh-info">Auto-refresh in <span id="refresh-countdown">60</span> seconds</div>');
        updateRefreshCountdown();
    }
}); 