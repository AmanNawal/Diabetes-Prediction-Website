

function navigateToAcetone(e){

    var user=firebase.auth().currentUser
    if(user)
    {
        window.location="./acetone"
    }
    else
    {
        toastVisible("Please login first to access the resources!",blue)
    }
}



function navigateToPrediction(e){

    var user=firebase.auth().currentUser
    if(user)
    {
        window.location="./normalprediction"
    }
    else
    {
        toastVisible("Please login first to access the resources!",blue)
    }
    
}