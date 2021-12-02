$(document).ready(
     function(){
     console.log("Ready!");
     var day_night = new Date().getHours();
     console.log(day_night);
     if (day_night > 12 && day_night <= 18) {
       /*$('.advance-link>img')*/
        
        $(".portrait").each(function(){
             console.log($(this).attr("href"));
             var img = $(this).find("img").attr("src");
             img.replace(".jpg","_party.jpg");
             $(this).find("img").attr('src',img);
        });
          
     }else{
     $(".portrait_image>img").attr('src','/images/member.jpg');
     }
          
     
      
});
