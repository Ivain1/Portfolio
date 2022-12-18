function gotoPage(target,newTab=false) {
    //var myWindow = window.open(target);
    if (newTab == false) {
        //window.open(target,_self);
        window.location.href = target;
    } else {
        window.open(target);
    }
}