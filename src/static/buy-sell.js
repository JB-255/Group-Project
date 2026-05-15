const buyButton = document.getElementById("buy");
const buyError = document.getElementById("buy-error");

buy.addEventListener("click", async () => {
	const id = location.pathname.split("/")[2];

    const response = await fetch(`/do-buy/${id}`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
    });
    //waits until the function is finished
    const result = (await response.text()).trim();
    if (result == "Success") {
    	// redirect to home
    	location.href = "/";
    } else {
        //shows the error message
        //shows the error message
        buyError.classList.remove("hidden");
    }
});