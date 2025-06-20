// Optional toast notification support
function showToast(message, type = 'success') {
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;
    document.body.appendChild(alert);

    setTimeout(() => {
        alert.remove();
    }, 3000);
}

// Example: showToast("User created!", "success");
document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('donationChart');
    if (ctx) {
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
                datasets: [{
                    label: 'USD Donations',
                    data: [500, 800, 1200, 900, 1500],
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16,185,129,0.1)',
                    tension: 0.3,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: false }
                }
            }
        });
    }
});

<!-- Chart.js CDN -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!-- Donations Line Chart -->
<script>
const ctx = document.getElementById('donationChart').getContext('2d');
new Chart(ctx, {
    type: 'line',
    data: {
        labels: {{ chart_labels | tojson }},
        datasets: [{
            label: 'Monthly Donations ($)',
            data: {{ chart_data | tojson }},
            fill: true,
            borderColor: '#4F46E5',  // Indigo tone to match your UI
            backgroundColor: 'rgba(79, 70, 229, 0.1)',
            tension: 0.4,
            pointBackgroundColor: '#6366F1',
            pointRadius: 4
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: true, labels: { color: '#374151' } }
        },
        scales: {
            x: {
                ticks: { color: '#6B7280' }
            },
            y: {
                beginAtZero: true,
                ticks: {
                    color: '#6B7280',
                    callback: value => '$' + value
                }
            }
        }
    }
});
</script>
