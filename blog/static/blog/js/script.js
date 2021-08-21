function funcop() {
    var x = document.getElementById("topnav");
    var icon = document.getElementsByClassName("icon");
    if (x.className === "top-nav") {
        x.className += " responsive";
        icon.className += "fas fa-bars"
    }
    else {
        x.className = "top-nav"
    }
}

function toggleOption() {
    var options = document.getElementById("opt");
    if (options.className === "options") {
        options.className += " list";
        console.log(options.className);
    }
    else {
        options.className = "options"
    }
}

function openTab(evn, btab) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName('tabcontent');
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(btab).style.display = "block";
    evn.currentTarget.className += " active";
}
