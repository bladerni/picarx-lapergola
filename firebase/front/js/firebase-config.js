// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCswWkR6qrP4qxYuDQ5iB6huCRQQetAOyQ",
    authDomain: "erni-hackathon.firebaseapp.com",
    databaseURL: "https://erni-hackathon-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "erni-hackathon",
    storageBucket: "erni-hackathon.appspot.com",
    messagingSenderId: "164169323198",
    appId: "1:164169323198:web:a1b378470ca81d330244ef"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const database = firebase.database();