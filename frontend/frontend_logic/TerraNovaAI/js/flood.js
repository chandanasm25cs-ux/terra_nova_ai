document.addEventListener("DOMContentLoaded", () => {
    console.log("Flood JS Loaded");
});
const floodForm =
    document.getElementById("floodForm");

floodForm.addEventListener("submit", function(e){

    e.preventDefault();

    const country =
        document.getElementById("country").value;

    const state =
        document.getElementById("state").value;

    const district =
        document.getElementById("district").value;

    const waterLevel =
        document.getElementById("waterLevel").value;

    if(
        country === "" ||
        state === "" ||
        district === "" ||
        waterLevel === ""
    ){
        alert("Please fill all fields");
        return;
    }

    alert("Flood Report Submitted Successfully!");
    window.location.href = "dashboard.html";

    floodForm.reset();
});


// IMAGE PREVIEW

const imageInput =
    document.getElementById("floodImage");

const preview =
    document.getElementById("preview");

imageInput.addEventListener("change", () => {

    const file = imageInput.files[0];

    if(file){

        const reader = new FileReader();

        reader.onload = function(e){

            preview.src = e.target.result;
        };

        reader.readAsDataURL(file);
    }
});