let colorConfig = { internalFillColor: '#222', internalStrokeColor: '#111', externalFillColor: '#222', externalStrokeColor: '#333' };
var cameraJoy = new JoyStick('cameraJoy', colorConfig);
var movementJoy = new JoyStick('movementJoy', colorConfig);

let lastCameraJoy = groupJoystickInfo(cameraJoy);
let lastMovementJoy = groupJoystickInfo(movementJoy);

let shouldSendData = true;
const robotData = {
    camera: {
        direction: 0
    },
    car: {
        acceleration: 0,
        automatic_mode: false,
        direction: 0,
        disco_mode: true
    }
};

setInterval(function () {

    //CAMERA JOYSTICK
    let currentCameraJoy = groupJoystickInfo(cameraJoy);
    if (!deepEqual(currentCameraJoy, lastCameraJoy)) {
        lastCameraJoy = currentCameraJoy;

        shouldSendData = true;

        console.log("Camera Joy: ", lastCameraJoy);
    }

    //MOVEMENT JOYSTICK
    let currentMovementJoy = groupJoystickInfo(movementJoy);
    currentMovementJoy.distance = Math.min(100.0, getDistance(movementJoy));
    if (!deepEqual(currentMovementJoy, lastMovementJoy)) {
        lastMovementJoy = currentMovementJoy;

        shouldSendData = true;;

        console.log("Movement Joy: ", lastMovementJoy);
    }

    if (shouldSendData) {
        robotData.camera.direction = lastCameraJoy.angle;

        robotData.car.acceleration = lastMovementJoy.distance;
        // -7 because the car rotation is a bit offset
        robotData.car.direction = lastMovementJoy.angle - 7;

        updateValue("/", robotData);
        shouldSendData = false;
    }

}, 50);



function groupJoystickInfo(joy) {
    return { angle: getAngle(joy) };
}

/**
 * Map degrees to range [-30, 30] (wheels left and right)
 * @param {*} deg 
 * @returns 
 */
function getAngle(joy) {
    // Remove unnecessary decimals
    xValue = Math.floor(joy.GetX());

    deg = (30 * xValue) / 100;

    return deg;
}


function getDistance(joy) {
    let distance = Math.sqrt(joy.GetX() * joy.GetX() + joy.GetY() * joy.GetY())

    // Going backwards
    if (joy.GetY() < 0) {
        distance = distance * -1;
    }

    return Math.floor(distance);
}

function deepEqual(x, y) {
    return (x && y && typeof x === 'object' && typeof y === 'object') ?
        (Object.keys(x).length === Object.keys(y).length) &&
        Object.keys(x).reduce(function (isEqual, key) {
            return isEqual && deepEqual(x[key], y[key]);
        }, true) : (x === y);
}

function activateAutomaticMode(e) {
    robotData.car.automatic_mode = !robotData.car.automatic_mode;
    if (robotData.car.automatic_mode) {
        e.style = "background-color: #76db29;"
    } else {
        e.style = ""
    }

    updateValue("/", robotData);
}