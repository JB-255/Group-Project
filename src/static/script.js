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
const rError = document.getElementById("uname-error");

const closeButtons = document.querySelectorAll(".close-popup");

//puts up thing
loginBtn.addEventListener("click", () => {loginPopup.classList.add("show-popup");});
registerBtn.addEventListener("click", () => {registerPopup.classList.add("show-popup");});

//popup goes
closeButtons.forEach(button => {
    button.addEventListener("click", () => {
        loginPopup.classList.remove("show-popup");
        registerPopup.classList.remove("show-popup");
    });
});

loginSubmit.addEventListener("click", async () => {
    const uname = loginUsername.value;
    const pword = loginPassword.value;
    //calling the py function
    const response = await fetch("/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({uname, pword})
    });
    //hold
    const result = (await response.text()).trim();
    if (result == "Yay") {
        //removes the popup + buttons
        loginPopup.classList.remove("show-popup");  
        loginBtn.classList.add("hidden");
        registerBtn.classList.add("hidden");

    } else {
        //Error popup
        loginError.classList.remove("hidden");
    }
});

//same stuff as login
registerSubmit.addEventListener("click", async () => {
    const uname = registerUsername.value;
    const pword = registerPassword.value;
    const response = await fetch("/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({uname,pword})
    });
    const result = await response.text();
    if (result == "Yay") {
        registerPopup.classList.remove("show-popup");
        loginBtn.classList.add("hidden");
        registerBtn.classList.add("hidden");
    } if (result == "Un") {
        rError.classList.remove("hidden");
    }
})
