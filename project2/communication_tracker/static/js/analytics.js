document.addEventListener('DOMContentLoaded', function () {
    fetch('/analytics/data/')
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('analyticsChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Frequency of Communication Methods',
                        data: data.data,
                        backgroundColor: ['#4CAF50', '#FF9800', '#2196F3', '#FF5722', '#9C27B0'],
                    }],
                },
            });
        });
});
