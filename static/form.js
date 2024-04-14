/*
document.querySelector('form').addEventListener('submit', function(event) {
    
    var select = document.getElementById('inputGroupSelect01');
    if (select.value === 'None') {
        event.preventDefault(); // prevent the form from submitting
        var toastElList = [].slice.call(document.querySelectorAll('.toast'))
        var toastList = toastElList.map(function(toastEl) {
            return new bootstrap.Toast(toastEl)
        });

        var toastHTMLElement = document.createElement("div");
        toastHTMLElement.classList.add("toast");
        toastHTMLElement.setAttribute("role", "alert");
        toastHTMLElement.setAttribute("aria-live", "assertive");
        toastHTMLElement.setAttribute("aria-atomic", "true");

        var toastBodyElement = document.createElement("div");
        toastBodyElement.classList.add("toast-body");
        toastBodyElement.textContent = "Please choose an option";

        toastHTMLElement.appendChild(toastBodyElement);
        document.body.appendChild(toastHTMLElement);

        var toast = new bootstrap.Toast(toastHTMLElement);
        toast.show();
    }
});
*/

document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting

    var select = document.getElementById('inputGroupSelect01');
    if (select.value === 'None') {
        var toastEl = document.getElementById('liveToast');
        var toast = new bootstrap.Toast(toastEl);
        // Show the toast
        toast.show();
    }
});
