$(document).ready(
     function(){
     console.log("Ready!");
     var day_night = new Date().getHours();
     console.log(day_night);
     if (day_night > 12 && day_night <= 17) {
       /*$('.advance-link>img')*/
        
        $(".portrait").each(function(){
             console.log($(this).attr("href"));
             $(this).children(".portrait_image>img").attr('src',"/images/party_dog.jpg");
        });
          
     }else{
     $(".portrait_image>img").attr('src','/images/member.jpg');
     }
          
     
      
});
