
const t = new Date();
const y = t.getFullYear();
const m = t.getMonth();
const d = t.getDate();
const h = t.getHour();
let dayList = ["Maandag","Dinsday", "Woensdag", "Donderdag", "Vrijdag","Zaterdag","Zondag"];
let monthList = ["Januari","Februari","Maart","April","Mei","Juni","Juli","Augustus","September","Oktober","November","December"];
const myDay = dayList[t.getDay()];
const myMonth = monthList[m];

if (m == 5 && d == 13) {
    //Verjaardag Iris
}
if (m == 11 && d == 11) {
    //Verjaardag Bert
}
if (m == 12 && d == 31) {
    //Oudejaarsag
}
if (m == 0 && d == 1) {
    //Nieuwjaarsdag
}
if (m == 1 && d == 26){
    //Verjaardag Jorn
}
if (m == 5 && d == 22){
    //Verjaardag Eline
}

function setDate(){
    const t = new Date();
    const y = t.getFullYear();
    const m = t.getMonth();
    const d = t.getDate();
    const h = t.getHour();
    let dayList = ["Maandag","Dinsday", "Woensdag", "Donderdag", "Vrijdag","Zaterdag","Zondag"];
    let monthList = ["Januari","Februari","Maart","April","Mei","Juni","Juli","Augustus","September","Oktober","November","December"];
    const myDay = dayList[t.getDay()];
    const myMonth = monthList[m];

    if (m == 5 && d == 13) {
        //Verjaardag Iris
    }
    if (m == 11 && d == 11) {
        //Verjaardag Bert
    }
    if (m == 12 && d == 31) {
        //Oudejaarsag
    }
    if (m == 0 && d == 1) {
        //Nieuwjaarsdag
    }
    if (m == 1 && d == 26){
        //Verjaardag Jorn
    }
    if (m == 5 && d == 22){
        //Verjaardag Eline
    }
    var e = document.getElementById('Date').innerHTML = 'Test 2';
}
function pickImgNum(date) {
    if (date.getMonth == 0,2,4,6,7,9,11){
        //31 days
    } else if (date.getMonth == 1){
        //february, 28 days
    } else {
        //30 days
    }
}
function setImage(path,date) {
    var imgNum = pickImgNum(date);
    var i = document.getElementByID("gal-img");
    i.src = path + 'image' + imgNum + '.jpg'
}
setDate();
