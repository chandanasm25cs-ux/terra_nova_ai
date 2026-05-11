// LOADING SCREEN

window.addEventListener("load", () => {
    const loader = document.querySelector(".loader");

    setTimeout(() => {
        loader.style.opacity = "0";

        setTimeout(() => {
            loader.style.display = "none";
        }, 1000);

    }, 2500);
});


// SMOOTH SCROLL

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute("href"))
            .scrollIntoView({
                behavior: "smooth"
            });
    });
});


// BUTTON CLICK SOUND

const buttons = document.querySelectorAll("button");

buttons.forEach(button => {
    button.addEventListener("click", () => {

        const sound = new Audio("assets/sounds/click.mp3");

        sound.play();
    });
});


// HOVER SOUND

buttons.forEach(button => {
    button.addEventListener("mouseenter", () => {

        const hover = new Audio("assets/sounds/hover.mp3");

        hover.play();
    });
});


// PAGE NAVIGATION

const signInBtn = document.querySelector(".signin-btn");

if(signInBtn){
    signInBtn.addEventListener("click", () => {
        window.location.href = "login.html";
    });
}