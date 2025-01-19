// const form = document.getElementById("my_form");

function validationForm(event) {
    event.preventDefault(); // Prevent the default form submission behavior
            
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    
    console.log("Email:", email);
    console.log("Password:", password);

}