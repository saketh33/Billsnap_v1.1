count = 0;

function refreshSwipers(count) {
    [...Array(count + 1).keys()].forEach(function(c) {
        swp1 = new Swiper('.swiper' + c, { direction: 'horizontal', loop: false, navigation: { nextEl: '.swipperNext' + c, prevEl: '.swipperPrev' + c } })
    })
}

function openPost(postid) {
    console.log(postid);
}

function displayPost(postid, authorname, authorpfp, createdOn, images, title, description) {
    out = "<div class='post_box'><div class='avater_section'><div class='profile'><img src='" + authorpfp + "' alt='profile' /><div class='name'><p>" + authorname + "</p></div></div></div><div class='para'><p>" + description + "</p></div><div class='swiper swiper" + count + "'><div class='swiper-wrapper'>";
    images.forEach(function(imagelink) {
        out += "<div class='swiper-slide'><img onclick='openPost(\"" + postid + "\")' src='" + imagelink + "' loading='lazy'></div>";
    })
    out += "</div><div class='swiper-button-prev swipperPrev" + count + "'></div><div class='swiper-button-next swipperNext" + count + "'></div></div>";
    out += "<div class='postTitle'>" + title + "</div><div class='postedOn'>" + createdOn + '</div>';
    document.getElementById("postsArea").innerHTML += out;
    refreshSwipers(count);
    count += 1;
}

fetch("{% url 'all_posts' %}").then(response => response.json()).then(data => {
    Object.keys(data).forEach(function(key) {
        displayPost(key, data[key]['author'], data[key]['authorPfp'], data[key]['createdOn'], data[key]['images'], data[key]['title'], data[key]['description'])
    })
})