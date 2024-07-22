document.addEventListener('DOMContentLoaded', function() {
    // Modal
    var modal = document.getElementById('add-list-modal');
    var btn = document.getElementById('add-list-btn');
    var span = document.getElementsByClassName('close')[0];

    btn.onclick = function() {
        modal.style.display = 'block';
    }

    span.onclick = function() {
        modal.style.display = 'none';
    }

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }

    // Form submission
    var addListForm = document.getElementById('add-list-form');

    addListForm.addEventListener('submit', function(event) {
        event.preventDefault();

        var listTitleInput = document.getElementById('list-title');
        var listTitle = listTitleInput.value.trim();

        if (listTitle !== '') {
            // Here you would typically send an AJAX request to the server to add the list
            // For demonstration purposes, we're just logging the list title
            console.log('New list title:', listTitle);

            // Close the modal after adding the list (for demonstration)
            modal.style.display = 'none';
            listTitleInput.value = ''; // Clear input field
        } else {
            alert('Please enter a list title.');
        }
    });
});
