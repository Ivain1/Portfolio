var img_count = Number(0);
const scrollTimeout = setTimeout(image_scroll,5000);
const clickTimeout = setTimeout(gal_button,2000);
function gal_button(thumb) {
    var galFullImg = document.getElementById("gal_main");
    galFullImg.src = thumb.src;
    }
function image_scroll() {
    var y = event.deltaY;
    var scrollUp = true;
    var target_name = 'thumb';
    if (y >= 0) {
        scrollUp = true;
    } else {
        scrollUp = false;
    }
    //alert(scrollUp);
    if (scrollUp == true) {
        if (img_count <= 4) {
            img_count += 1;
            //alert(img_count);
        }
        else {
            img_count = 1;
            setInterval(7);
            //alert(img_count);
        }
    } else {
        if (img_count >= 1) {
            img_count += -1;
            //alert(img_count);
        }
        else {
        img_count = 5;
            //alert(img_count);
        }
    }
    target_num = img_count.toString();
    //alert(target_num);
    target = target_name.concat(target_num);
        //alert(target);
    new_image = document.getElementById(target);
        //alert(new_image);
    old_image = document.getElementById("gal_main");    
    old_image.src = new_image.src;
}
