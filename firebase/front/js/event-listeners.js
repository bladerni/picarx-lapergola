// Acceleration
let counter = 0;
const accelerationButton = document.getElementById("accelerationButton");
accelerationButton.addEventListener("click", () => {
    database.ref("/car/acceleration").set(counter++);
});

// Car direction
let carDirection = 0;
const carDirectionButton = document.getElementById("carDirectionButton");
carDirectionButton.addEventListener("click", () => {
    database.ref("/car/direction").set(carDirection++);
});

// Disco mode
let discoMode = false;
const discoModeButton = document.getElementById("discoModeButton");
discoModeButton.addEventListener("click", () => {
    discoMode = !discoMode;
    database.ref("/car/disco_mode").set(discoMode);
});

// Camera direction
let cameraDirection = 0;
const cameraDirectionButton = document.getElementById("cameraDirectionButton");
cameraDirectionButton.addEventListener("click", () => {
    database.ref("/camera/direction").set(cameraDirection++);
});

// Car automatic mode
let automaticMode = false;
const automaticModeButton = document.getElementById("automaticModeButton");
automaticModeButton.addEventListener("click", () => {
    automaticMode = !automaticMode;
    database.ref("/car/automatic_mode").set(automaticMode);
});