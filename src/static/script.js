//connecting the variables to their html id
const loginBtn = document.getElementById("login-btn");
const loginPopup = document.getElementById("login-popup");
const loginSubmit = document.getElementById("login-submit");
const loginUsername = document.getElementById("login-username");
const loginPassword = document.getElementById("login-password");
const loginError = document.getElementById("login-error");

const registerBtn = document.getElementById("register-btn");
const registerPopup = document.getElementById("register-popup");
const registerSubmit = document.getElementById("register-submit");
const registerUsername = document.getElementById("register-username");
const registerPassword = document.getElementById("register-password");

const closeButtons = document.querySelectorAll(".close-popup");

//puts up the popup when the button is pressed
loginBtn.addEventListener("click", () => {loginPopup.classList.add("show-popup");});
registerBtn.addEventListener("click", () => {registerPopup.classList.add("show-popup");});

//when the x button is clicked, popup goes away
closeButtons.forEach(button => {
    button.addEventListener("click", () => {
        loginPopup.classList.remove("show-popup");
        registerPopup.classList.remove("show-popup");
    });
});

loginSubmit.addEventListener("click", async () => {
    //grabs the username and pword from the textboxes
    const username = loginUsername.value;
    const password = loginPassword.value;
    //calling the python function
    const response = await fetch("/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username, password})
    });
    //waits until the function is finished
    const result = (await response.text()).trim();
    if (result == "Success") {
        //removes the popup and the login/register buttons
        loginPopup.classList.remove("show-popup");  
        loginError.classList.add("hidden");
        loginBtn.classList.add("hidden");
        registerBtn.classList.add("hidden");

    } else {
        //shows the error message
        loginError.classList.remove("hidden");
    }
});

registerSubmit.addEventListener("click", async () => {
    const username = registerUsername.value;
    const password = registerPassword.value;
    const response = await fetch("/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({username,password})
    });
    const result = await response.text();
    registerPopup.classList.remove("show-popup");
    loginBtn.classList.add("hidden");
    registerBtn.classList.add("hidden");
})
