var loginHTMLElement = document.getElementById( 'userlogin' );
var registerHTMLElement = document.getElementById( 'userregister' );
var logoutHTMLElement = document.getElementById( 'userlogout' );
var red='#dc3545'
var yellow='#ffc107'
var blue='#0d6efd'
var green='#28a745'


function toastStyling(toastHTMLElement)
{
   
    //var toastHTMLElement = document.getElementById( 'EpicToast' );

    //toastHTMLElement.style.position='absolute'
    toastHTMLElement.style.bottom='20px'
    toastHTMLElement.style.left='20px'
    toastHTMLElement.style.zIndex='3'

}


async function toastVisible(message,toastcolor)
{
    var option = {animation : true ,delay : 3000};
    var toastHTMLElement = document.getElementById( 'EpicToast' );
    toastHTMLElement.style.display='block'
    toastStyling(toastHTMLElement)
    document.getElementById("toasttext").innerHTML = message;
    toastHTMLElement.style.backgroundColor=toastcolor
    var toastElement = new bootstrap.Toast( toastHTMLElement, option );
     toastElement.show();
}


function toastDismiss()
{
    var toastHTMLElement = document.getElementById( 'EpicToast' );
    toastHTMLElement.style.display='none'

}

async function signup(e)
{
    e.preventDefault();
    const username=document.querySelector('#inputName').value
    const email=document.querySelector('#inputEmail').value
    const password=document.querySelector('#inputPassword').value
    console.log(email.value,password.value)

    try{
    const result=await firebase.auth().createUserWithEmailAndPassword(email,password)
    await firebase.auth().signOut()
    await result.user.updateProfile({
        displayName:username
    })
    await result.user.sendEmailVerification()
    toastVisible("Verification Email sent!",blue)

    //window.location.replace("./login")

    console.log(result)
    }
    catch(err){
        toastVisible(err.message,red)
        
    }
}


function isUserLoggedIn(e)
{
    var user=firebase.auth().currentUser
    if(user)
    {
        alert("PREDICT DIABETES")
    }
    else
    {
        toastVisible("Please login first to access the resources!",blue)
    }
}

async function login(e)
{

    e.preventDefault();
    const email=document.querySelector('#inputEmail').value
    const password=document.querySelector('#inputPassword').value
    try{
    const result=await firebase.auth().signInWithEmailAndPassword(email,password)
    console.log(result)
    var auth=firebase.auth()
    var user=auth.currentUser
    if(user!=null)
    {
        var user_verified=user.emailVerified

        if(user_verified==true)
        {
            
            toastVisible("Logged in successfully!",green)
                

        }
        else
        {
            toastVisible("Please verify email first!",red)
            await auth.signOut()
        }
    }
    else
    {
        toastVisible("Please login in firstly!",blue)
    }
   

    }
    catch(err){
        toastVisible(err.message,red)
        
    }
    
}


async function logout(e)
{
    e.preventDefault();
    try{
    const result=await firebase.auth().signOut()
    
    toastVisible("successfully signed out!",green)
    }
    catch(err)
    {alert(err.message)
    }
}

firebase.auth().onAuthStateChanged((user) => {
    if (user) {
        loginHTMLElement.style.display='none'
        registerHTMLElement.style.display='none'
        logoutHTMLElement.style.display='block'
    } else {
       

        loginHTMLElement.style.display='block'
        registerHTMLElement.style.display="block"
        logoutHTMLElement.style.display='none'
    }
  });





