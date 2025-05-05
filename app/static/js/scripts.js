document.addEventListener('DOMContentLoaded', function() {
    const addImageForm = document.getElementById('add-image-form');
    const addWordForm = document.getElementById('add-word-form');
    const adminLoginForm = document.getElementById('admin-login-form');

    if (addImageForm) {
        addImageForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(addImageForm);
            fetch('/admin/add-image', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                addImageForm.reset();
            })
            .catch(error => console.error('Error:', error));
        });
    }

    if (addWordForm) {
        addWordForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(addWordForm);
            fetch('/admin/add-word', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                addWordForm.reset();
            })
            .catch(error => console.error('Error:', error));
        });
    }

    if (adminLoginForm) {
        adminLoginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(adminLoginForm);
            fetch('/admin/login', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/admin';
                } else {
                    alert(data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    }
});