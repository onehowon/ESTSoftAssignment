var parentContainer = document.getElementById('parentContainer');

for(var i=0; i<10; i++){
    var article = document.createElement('article');
    article.className = 'parent';

    var figure = document.createElement('figure');

    var img = document.createElement('img');
    img.className = 'figImg';
    img.src = 'https://file.mk.co.kr/meet/neds/2021/07/image_readtop_2021_654175_16256093474708254.jpg';
    img.alt = '';

    var figcaption = document.createElement('figcaption');
    figcaption.className = 'figCap';
    figcaption.textContent = '유재석씨가 수상식에서 환하게 웃고 있다.';

    figure.appendChild(img);
    figure.appendChild(figcaption);

    article.appendChild(figure);

    parentContainer.appendChild(article);

}