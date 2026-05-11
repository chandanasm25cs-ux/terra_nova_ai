const earthquakeForm =
    document.getElementById("earthquakeForm");

earthquakeForm.addEventListener("submit", function(e){

    e.preventDefault();

    const country =
        document.getElementById("country").value;

    const structuralDamage =
        document.getElementById("damage").value;

    if(country === "" || structuralDamage === ""){
        alert("Please fill all fields");
        return;
    }

    alert("Earthquake Report Submitted!");

    earthquakeForm.reset();
});