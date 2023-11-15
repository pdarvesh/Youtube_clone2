
const button = document.getElementById('signupBtn');
    console.log( "button" )

    // Add a click event listener to the button
    button.addEventListener('click', function() {
      // Redirect to the desired URL when the button is clicked
      window.location.href = '../index.html';
     }); 
    
var menuIcon = document.querySelector(".menu_icon");
var sidebar = document.querySelector(".sidebar");
var container = document.querySelector(".container");

menuIcon.onclick = function(){
    sidebar.classList.toggle("small-sidbar");
    container.classList.toggle("large_container");
}

    // Get the videoId from the query parameter
    const urlParams = new URLSearchParams(window.location.search);
    const videoId = urlParams.get('videoId');
    const categoryId = urlParams.get('categoryId');

    console.log("catgeor",categoryId)
    // Set the video source
    console.log(videoId)
    console.log("sssd")
    if (videoId) {
      const iframe = document.querySelector('iframe');
      iframe.src = `https://www.youtube.com/embed/${videoId}`;

    }


    


    // if(categoryId=='1'){
    //     console.log("1")
    //     let imagesource=`../images/education2.jpeg`s
    // }
