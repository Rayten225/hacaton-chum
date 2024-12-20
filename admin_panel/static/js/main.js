// burger menu
const burgerButton = document.querySelector('.burger-button');
const burgerMenu = document.querySelector('.burger-menu')
let body = document.querySelector('body');

function toggleBurger() {
    burgerButton.classList.toggle('active')
    burgerMenu.classList.toggle('active')
    body.classList.toggle('lock');
}

burgerButton.addEventListener('click', toggleBurger)

// ----------------------------------------карта

document.addEventListener('DOMContentLoaded', function () {
    var objects = document.getElementsByClassName('object');
    var places = document.getElementsByClassName('place');
    var selectedObject = null;
    var infoBlock = document.querySelector('.info');
    var totalCostBlock = document.querySelector('.total-cost');
    var placedObjects = []; // массив для хранения идентификаторов объектов, размещенных в местах
    var totalCost = 0; // общая стоимость всех добавленных объектов
    let qeryvoit = [];

    function restoreObjects() {
        var objectsContainer = document.querySelector('.objects');

        for (var i = 0; i < objects.length; i++) {
            var object = objects[i];
            objectsContainer.appendChild(object);
        }
    }

    function updateTotalCost() {
        totalCostBlock.textContent = 'Общая стоимость: ' + totalCost.toFixed(2) + " млн.";
        
        // Проверка на превышение общей стоимости
        if (totalCost > 75) {
            totalCostBlock.style.color = 'red'; // подсвечиваем красным
        } else {
            totalCostBlock.style.color = 'black'; // сбрасываем цвет
        }
    }

    for (var j = 0; j < places.length; j++) {
        var place = places[j];
        place.addEventListener('click', function () {
            if (this.childElementCount === 0 || !this.hasAttribute('data-id')) {
                if (selectedObject) {
                    var data = JSON.parse(selectedObject.getAttribute('data-object'));
                    var img = document.createElement('img');
                    img.src = data.image;
                    img.onload = function() {
                        var placeWidth = this.parentElement.offsetWidth;
                        var placeHeight = this.parentElement.offsetHeight;
                        var imgAspectRatio = this.width / this.height;
                        var placeAspectRatio = placeWidth / placeHeight;
                        let tag = data.name
                        document.cookie = `tag=${tag}`
                        if (imgAspectRatio > placeAspectRatio) {
                            this.style.width = '100%';
                            this.style.height = '100%';
                        } else {
                            this.style.width = 'auto';
                            this.style.height = '100%';
                        }
                    };
                    this.appendChild(img);
                    this.setAttribute('data-id', data.id); // устанавливаем атрибут data-id у места
                    placedObjects.push(data.id); // добавляем идентификатор объекта в массив размещенных объектов
                    document.querySelector('.message').textContent = '';
                    let voit = data.id;
                    qeryvoit.push(voit);

                    var cross = document.createElement('span');
                    cross.innerHTML = "❌";
                    cross.setAttribute('title', `${data.name}`);
                    cross.classList.add('delete');
                    this.appendChild(cross);

                    cross.addEventListener('click', function(e) {
                        e.stopPropagation();
                        var parentElement = this.parentElement; // сохраняем ссылку на родительский элемент
                        parentElement.removeChild(this.previousElementSibling); // удаляем изображение
                        parentElement.removeChild(this); // удаляем кнопку удаления
                        parentElement.removeAttribute('data-id'); // удаляем атрибут data-id у места
                        

                        // Удаляем информацию об этом объекте из блока .info
                        var objectName = data.name;
                        var infoObjects = document.querySelectorAll('.info p');
                        for (var k = 0; k < infoObjects.length; k++) {
                            var infoObjectName = infoObjects[k].textContent.split(':')[1].split(',')[0].trim();
                            if (infoObjectName === objectName) {
                                infoBlock.removeChild(infoObjects[k]);
                                break;
                            }
                        }

                        var index = placedObjects.indexOf(data.id);
                        var voitIndex = qeryvoit.indexOf(data.id);
                        if (index !== -1) {
                            placedObjects.splice(index, 1); // удаляем идентификатор объекта из массива
                            qeryvoit.splice(voitIndex, 1);
                            totalCost -= parseFloat(data.price.substring(1)); // уменьшаем общую стоимость
                            document.cookie = `data-id=${qeryvoit}`          
                            updateTotalCost(); // обновляем значение счетчика
                        }
                        restoreObjects(); // восстанавливаем объекты в раздел objects
                    });

                    infoBlock.style.display = 'block';
                    var infoObjects = document.querySelectorAll('.info p');
                    var objectExistsInInfo = false;
                    for (var k = 0; k < infoObjects.length; k++) {
                        var infoObjectName = infoObjects[k].textContent.split(':')[1].split(',')[0].trim();
                        if (infoObjectName === data.name) {
                            objectExistsInInfo = true;
                            break;
                        }
                    }
                    if (!objectExistsInInfo) {
                        var infoText = document.createElement('p');
                        infoText.textContent = 'Добавлен объект: ' + data.name + ', Цена: ' + data.price;
                        infoBlock.appendChild(infoText);
                        totalCost += parseFloat(data.price.substring(1)); // увеличиваем общую стоимость
                        updateTotalCost(); // обновляем значение счетчика
                    }

                    selectedObject = null;
                } else {
                    document.querySelector('.message').textContent = 'Сначала выберите объект для перемещения!';
                }
            } else if (this.hasAttribute('data-id')) {
                document.querySelector('.message').textContent = 'В это место уже добавлен объект!';
                selectedObject = null;
            } else {
                document.querySelector('.message').textContent = 'Место уже занято!';
                selectedObject = null;
            }
            document.cookie = `data-id=${qeryvoit}`
        });
    }

    for (var i = 0; i < objects.length; i++) {
        var object = objects[i];
        object.addEventListener('click', function (event) {
            event.stopPropagation();
            var data = JSON.parse(this.getAttribute('data-object'));
            if (!placedObjects.includes(data.id)) { // проверяем, нет ли уже такого объекта в размещенных объектах
                if (selectedObject !== this) {
                    selectedObject = this;
                }
            } else {
                document.querySelector('.message').textContent = 'Этот объект уже размещен в месте!';
                selectedObject = null;
            }
        });
    }
    
    // Обработчик нажатия на кнопку
     //  modal window
     var modal = document.querySelector(".modal");
     var trigger = document.querySelector(".trigger");
     var closeButton = document.querySelector(".close-button");
     let body = document.querySelector('body');
     function toggleModal() {
         modal.classList.toggle("show-modal");
         body.classList.toggle('lock');
     }
 
     function windowOnClick(event) {
         if (event.target === modal) {
             toggleModal();
         }
     }
     // Обработчик нажатия на кнопку
     trigger.addEventListener('click', function () {
         // Проверяем, превышает ли общая стоимость 75
         if (totalCost > 75) {
             document.querySelector('.message').textContent = 'Поменяйте сумму';
         }else if (totalCost == 0) {
            document.querySelector('.message').textContent = 'Выберите объекты';
         }else {
             trigger.addEventListener("click", toggleModal);
             closeButton.addEventListener("click", toggleModal);
             window.addEventListener("click", windowOnClick);
         }
     });
 });

// media

const swiper = document.querySelector(".objects");
const swiper_galary = document.querySelector(".galary__blocks");

function updateSlidesPerView() {
    if (window.innerWidth < 895) {
        swiper.setAttribute("slides-per-view", "1");
        swiper_galary.setAttribute("slides-per-view", "1");
        swiper.setAttribute("pagination-type", "none");
    } else if (window.innerWidth < 1335) {
        swiper.setAttribute("slides-per-view", "2");
        swiper_galary.setAttribute("slides-per-view", "2");
        swiper.setAttribute("pagination-type", "fraction");
    } else {
        swiper.setAttribute("slides-per-view", "3");
        swiper_galary.setAttribute("slides-per-view", "2");
        swiper.setAttribute("pagination-type", "none");
    }
}
// Вызываем функцию при загрузке страницы
updateSlidesPerView();
// Добавляем обработчик изменения размера окна
window.addEventListener("resize", updateSlidesPerView);

// обводка обяекта
var slides = document.querySelectorAll('.object');

// Добавляем обработчик клика для каждого блока
slides.forEach(function(slide) {
  slide.addEventListener('click', function() {
    slides.forEach(function(s) {
      s.classList.remove('selected');
    });
    slide.classList.add('selected');
  });
});