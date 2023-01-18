
    import { initializeApp } from "https://www.gstatic.com/firebasejs/9.15.0/firebase-app.js";
    import {getAuth,createUserWithEmailAndPassword,signInWithEmailAndPassword,signOut,sendSignInLinkToEmail} from "https://www.gstatic.com/firebasejs/9.15.0/firebase-auth.js";
    import {getDatabase, set, ref, update} from "https://www.gstatic.com/firebasejs/9.15.0/firebase-database.js";
    const firebaseConfig = {
        apiKey: "AIzaSyC20zl0qAiDDzhX3S4vi5jBfr8cROz_DfA",
        authDomain: "diabetes-predictor-3b0b7.firebaseapp.com",
        databaseURL: "https://diabetes-predictor-3b0b7-default-rtdb.firebaseio.com",
        projectId: "diabetes-predictor-3b0b7",
        storageBucket: "diabetes-predictor-3b0b7.appspot.com",
        messagingSenderId: "17055668058",
        appId: "1:17055668058:web:eeda14d7b417d11f15c563"
      };
      const app = initializeApp(firebaseConfig);
      const auth = getAuth();
      const database = getDatabase(app);
      
      const actionCodeSettings = {
      url: 'https://www.example.com/finishSignUp?cartId=1234',
      // This must be true.
      handleCodeInApp: true,
      iOS: {
        bundleId: 'com.example.ios'
      },
      android: {
        packageName: 'com.example.android',
        installApp: true,
        minimumVersion: '12'
      },
      dynamicLinkDomain: 'example.page.link'
      };


      submitData.addEventListener('click', (e) => {
    
       var username=document.getElementById("inputName").value
       var email=document.getElementById("inputEmail").value
       var password=document.getElementById("inputPassword").value
    
    //sign up user
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            
            const user = userCredential.user;
            set(ref(database, 'users/' + user.uid), {
                username: username,
                email: email,
                password: password
            })
                .then(() => {
                  sendSignInLinkToEmail(auth, email, actionCodeSettings)
                  .then(() => {
                
                      alert("Mail Sent!")
                  })
                  .catch((error) => {
                    const errorCode = error.code;
                    const errorMessage = error.message;
                    alert("Email verification Error "+errorMessage)
                  });
                  window.location.replace("./login")
    
                })
                .catch((error) => {
                    alert("savinf into database error "+error);
                });
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            alert("Creating user error "+errorMessage);
        });

     
    });

