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
function gotoPage(page){
    //url = location.href;
    //console.log(url);
    switch(page) {
        case 1:
            //alert("page 1");
            window.location.href = "menu.html";
            break;
        case 2:
            //alert("page 2");
            window.location.href = "gallery.html";
            break;
        case 3:
            window.location.href = "content.html"
            break;
        case 4:
            window.location
            break;

        default:
            window.location.assign = "gallery.html";

    }

}

function populateMenu(){
    //alert("The page has loaded");
    document.getElementById('button1').innerHTML = "<img alt='H' src='static/IMG/home_icon.png'>";
    document.getElementById('button2').innerHTML = "<img alt='G' src='static/IMG/gal_icon.png'>";
    document.getElementById('button3').innerHTML = "<img alt='T' src='static/IMG/third_icon.png'>";
}
function sidebarExpand(self) {
    //numb = self.childElementCount;
    //self.style.transition = "width .5s";
    document.getElementById('button1').innerHTML = "Home";
    document.getElementById('button2').innerHTML = "Gallery";
    document.getElementById('button3').innerHTML = "Third";
    self.style.width = "10%";
    
}
function sidebarContract(self){
    self.style.width = "5rem";
    populateMenu();
}