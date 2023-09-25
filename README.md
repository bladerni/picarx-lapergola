# La Pergola Team Hackathon Readme

Welcome to the La Pergola Team's GitHub repository for the hackathon! We are excited to share our journey as we work hard to complete the hackathon, assemble our critter, prepare the control site, and bring it to life! 🚀

## About Us

La Pergola Team is a group of enthusiastic individuals from Valencia ERNI's office who are passionate about technology and are committed to overcoming challenges. We believe in teamwork, dedication, and creativity to achieve our goals.

## Our Mission

Our mission for this hackathon is clear: plan our strategy, write our magic code, and make the best use of all the resources at our disposal. We're here to learn, innovate, and have fun while doing it!

## Challenges Faced

Every journey comes with its share of challenges, and we are no exception. We've encountered a few bumps along the road, such as:

- The first SD Card burning out, reminiscent of Valencian Fallas!
- Issues with package installations that tested our problem-solving skills.
- Formatted Raspberry PI: While trying to test the engines with voltage, we screwed something up and the Raspberry PI 4 died. We had to use one Raspberry PI 3 from one of our teammates!

But remember, La Pergola Team doesn't surrender! We believe in finding solutions for every problem that comes our way. With determination and teamwork, we overcomed these obstacles.

## Refueling with World Paella Day

During our intense coding sessions, we were fortunate enough to have some delicious food from the "World Paella Day" in the fridge. It's these small moments of respite that keep us energized and motivated to keep going. Let's tackle the challenge with renewed enthusiasm!

## Technology Stack

To make our critter come to life, we are using the following technology stack:

- **Firebase**: We have chosen Firebase as our real-time server to send commands to our Raspberry Picarx, enabling seamless communication between the control site and the critter.

- **Python**: Our codebase is primarily written in Python. We use Python to read from Firebase and control the engines of the car, ensuring precise movements and actions.

- **Vanilla JavaScript**: For the frontend of our control site, we have opted for vanilla JavaScript, providing a smooth and responsive user interface for controlling our critter.

- **GitHub actions**: We set up CI/CD to automatically deploy our website after every commit.

## Repository Structure

- **/HMTL**: Contains the frontend code. User interface where you can control the camera and movement of the robot through internet. There is also one button to enable line tracking mode.
- **Java/com.udpserver**: Java server we tested to stream the camera to internet (did not work)
- **/robot**: Houses the Python code responsible for interacting with Firebase and controlling the car.
    1. disco_mode_final.py: Makes the robot dance and move while playing a funny song
    2. handler.py: Listens to Firebase changes like camera angle or car movement. It also contains the line tracker implementation.

Thank you for joining us on this exciting journey as we bring our critter to life. Let's make this hackathon a success together! 💡🤖🌟

**La Pergola Team**
