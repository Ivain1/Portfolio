var img_count = Number(0);
const scrollTimeout = setTimeout(image_scroll,5000);
const clickTimeout = setTimeout(gal_button,2000);

function gal_button(thumb) {
    var galFullImg = document.getElementById("gal_main");
    galFullImg.src = thumb.src;
    }
function cardHover(self) {
    self.getElementByTag('')
}

function image_scroll() {
        //alert(target);
    new_image = document.getElementById(target);
        //alert(new_image);
    old_image = document.getElementById("gal_main");    
    old_image.src = new_image.src;
}
function gotoPage(page){
    window.location.href= page;

}
