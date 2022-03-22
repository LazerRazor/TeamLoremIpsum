
const getLocation=()=>{
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}

showPosition = (position) => {
    console.log(position.coords.latitude);
    console.log(position.coords.longitude);
    document.getElementById("lat").value = position.coords.latitude;
    document.getElementById("long").value = position.coords.longitude;
}