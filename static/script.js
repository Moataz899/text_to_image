document.getElementById('imageForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission
    const promptInput = document.getElementById('promptInput').value;
    
    if (promptInput) {
        document.getElementById('loading').style.display = 'block'; // Show loading
        this.submit(); // Submit the form
    } else {
        alert('Please enter a description!');
    }
});
