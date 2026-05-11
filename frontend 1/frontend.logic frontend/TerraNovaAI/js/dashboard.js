// SIDEBAR TOGGLE

const menuBtn = document.querySelector(".menu-btn");
const sidebar = document.querySelector(".sidebar");

menuBtn.addEventListener("click", () => {
    sidebar.classList.toggle("active");
});


// ANIMATED COUNTERS

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    counter.innerText = "0";

    const updateCounter = () => {

        const target = +counter.getAttribute("data-target");

        const current = +counter.innerText;

        const increment = target / 100;

        if(current < target){

            counter.innerText =
                `${Math.ceil(current + increment)}`;

            setTimeout(updateCounter, 20);

        } else {

            counter.innerText = target;
        }
    };

    updateCounter();
});


// ALERT SOUND

const alertBtn = document.querySelector(".alert-btn");

if(alertBtn){
    alertBtn.addEventListener("click", () => {

        const siren =
            new Audio("assets/sounds/alert.mp3");

        siren.play();

        alert("Emergency Alert Activated!");
    });
}