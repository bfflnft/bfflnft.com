var nft1 = document.getElementById("nft1");
var nft2 = document.getElementById("nft2");

var nft_urls = [
    "./res/nft/psycho.png",
    "./res/nft/squid.png",
    "./res/nft/chef.png",
    "./res/nft/titan.png",
    "./res/nft/bb.png",
    "./res/nft/papap.png",
    "./res/nft/scooter.png"
]
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

window.setInterval(() => {
    let i1 = getRandomInt(nft_urls.length);
    let i2 = getRandomInt(nft_urls.length);

    while(i2 == i1) i2 = getRandomInt(nft_urls.length);

    nft1.src = nft_urls[i1];
    nft2.src = nft_urls[i2];
}, 3000);