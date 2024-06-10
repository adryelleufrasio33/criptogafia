document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const fileInput = document.getElementById('file');
    const submitButton = document.querySelector('button');
    const message = document.createElement('p');

    form.appendChild(message);

    form.addEventListener('submit', (event) => {
        if (!fileInput.files.length) {
            event.preventDefault();
            message.textContent = 'Por favor, selecione uma imagem para criptografar.';
            message.style.color = 'red';
        } else {
            submitButton.textContent = 'Criptografando...';
            submitButton.disabled = true;
        }
    });
});
