   $(document).ready(function(){
     console.log("Ready!");
     function check_image() {
      var day_night = new Date().getHours();
      console.log($day_night);
      if (day_night > 12 && day_night <= 17) {
       /*$('.advance-link>img')*/
        $(".portrait_image>img").css('src',"images/party_dog.jpg");
      }
      /*else if (day_night > 12 && day_night < 21) {
             $("#gilidimage").css('background-image',"url('http://day-image-here.png')");
        }*/
       else {
            $(".portrait_image>img").css('src',"images/member.jpg");
       }*/ 
   setInterval(check_image,60000);    
   }
});
