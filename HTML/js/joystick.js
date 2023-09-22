let colorConfig = { internalFillColor: '#666', internalStrokeColor: '#444', externalFillColor: '#666', externalStrokeColor: '#444' };
var cameraJoy = new JoyStick('cameraJoy', colorConfig);
var movementJoy = new JoyStick('movementJoy', colorConfig);

let lastCameraJoy = groupJoystickInfo(cameraJoy);
let lastMovementJoy = groupJoystickInfo(movementJoy);

setInterval(function () {

    //CAMERA JOYSTICK
    let currentCameraJoy = groupJoystickInfo(cameraJoy);
    if (!deepEqual(currentCameraJoy, lastCameraJoy)) {
        lastCameraJoy = currentCameraJoy;

        updateValue("camera/direction", lastCameraJoy.angle);

        console.log("Camera Joy: ", lastCameraJoy);
    }

    //MOVEMENT JOYSTICK
    let currentMovementJoy = groupJoystickInfo(movementJoy);
    currentMovementJoy.distance = Math.min(100.0, getDistance(movementJoy));
    if (!deepEqual(currentMovementJoy, lastMovementJoy)) {
        lastMovementJoy = currentMovementJoy;

        updateValue("/car/acceleration", lastMovementJoy.distance);
        updateValue("/car/direction", lastMovementJoy.angle);

        console.log("Movement Joy: ", lastMovementJoy);
    }

}, 50);



function groupJoystickInfo(joy) {
    return { angle: getAngle(joy) };
}

function getAngle(joy) {
    let rad = Math.atan2(joy.GetY(), joy.GetX()); // In radians
    let deg = rad * (180 / Math.PI);

    return Math.floor(deg);
}

function getDistance(joy) {
    let distance = Math.sqrt(joy.GetX() * joy.GetX() + joy.GetY() * joy.GetY())
    return Math.floor(distance);
}

function deepEqual(x, y) {
    return (x && y && typeof x === 'object' && typeof y === 'object') ?
        (Object.keys(x).length === Object.keys(y).length) &&
        Object.keys(x).reduce(function (isEqual, key) {
            return isEqual && deepEqual(x[key], y[key]);
        }, true) : (x === y);
}