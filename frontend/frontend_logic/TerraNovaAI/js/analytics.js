// FAKE AI THREAT LEVEL

const threatLevel =
    document.querySelector(".threat-level");

let level = 0;

const interval = setInterval(() => {

    level++;

    threatLevel.innerText = level + "%";

    if(level >= 92){
        clearInterval(interval);
    }

}, 50);