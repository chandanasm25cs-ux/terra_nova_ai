const registerForm = document.getElementById("registerForm");

registerForm.addEventListener("submit", function(e){

    e.preventDefault();

    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if(username === "" || email === "" || password === ""){
        alert("Please fill all fields");
        return;
    }

    const userData = {
        username,
        email,
        password
    };

    localStorage.setItem("terraNovaUser", JSON.stringify(userData));

    alert("Registration Successful!");

    window.location.href = "login.html";
});